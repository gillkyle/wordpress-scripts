#!/usr/bin/env python3

import os
import subprocess
from csv import reader
import json

# this script is run from the terminal that has ssh'd into a Local WordPress terminal
# via "Open Site Shell". It is run like so (matching your local machine's path to the clone):
# $ ./../../../../../kyle/Github/wordpress-scripts/shell/import-posts.py

# You can run system/wp commands like this:
# os.system('wp user list')

basePath = "./../../../../../kyle/Github/wordpress-scripts"

with open('./../../../../../kyle/Github/wordpress-scripts/single-post.json') as f:
    posts = json.load(f)

for post in posts['data']['allMdx']['nodes']:
    # access and normalize the data from JSON
    excerpt = post['fields']['excerpt']
    slug = post['fields']['slug'].replace("/blog/", "")
    author = post['frontmatter']['author']['id'].replace(" ", "")
    title = post['frontmatter']['title']
    date = post['frontmatter']['date']
    seo_title = post['frontmatter']['seoTitle']
    canonical_link = post['frontmatter']['canonicalLink']
    published_at = post['frontmatter']['publishedAt']
    content = post['rawBody']
    tags = ', '.join(post['frontmatter']['tags'])

    print(f'Processing post {title}...')

    print(f'Searching for author "{author}" in post:')
    # awk the user list from WP to find the proper author ID as a string
    author_id = subprocess.check_output(
        f"awk -v author='{author}' '{{ if($2 == author) {{ print $1 }} }}' './../../../../../kyle/Github/wordpress-scripts/shell/authors.txt'", shell=True, universal_newlines=True).strip()
    print(f'Author ID found for "{author}": {author_id}')

    # create the post by instantiating the wp command in the shell, passing in the proper variables
    post_id = subprocess.check_output(
        f'wp post create --post_author={author_id} --post_date={date} --post_status="publish" --post_title="{title}" --post_excerpt="{excerpt}" --tags_input="{tags}" --published_at="{published_at}" --porcelain', shell=True, universal_newlines=True).strip()
    print(f'The post id is {post_id}')

    # add meta fields that come from ACF
    if seo_title:
        os.system(f'wp post meta set {post_id} seo_title "{seo_title}"')
    if excerpt:
        os.system(f'wp post meta set {post_id} text "{excerpt}"')
    if published_at:
        os.system(f'wp post meta set {post_id} published_at "{published_at}"')
    if canonical_link:
        os.system(
            f'wp post meta set {post_id} canonical_link "{canonical_link}"')

print("done")
