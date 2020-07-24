#!/usr/bin/env python3

import os
import subprocess
from csv import reader
import json

# this script is run from the terminal that has ssh'd into a Local WordPress terminal
# via "Open Site Shell". It is run like so (matching your local machine's path to the clone):
# $ ./../../../../../kyle/Github/wordpress-scripts/shell/import-starters.py

# You can run system/wp commands like this:
# os.system('wp user list')

basePath = "./../../../../../kyle/Github/wordpress-scripts"

with open('./../../../../../kyle/Github/wordpress-scripts/starters.json') as f:
    starters = json.load(f)

starters_created = 0

for starter in starters['data']['allStartersYaml']['nodes']:
    print(starter)
    # access and normalize the data from JSON
    description = starter['description']
    features = starter['features']
    repoo = starter['repo']
    tags = starter['tags']
    url = starter['url']
    featured = starter['fields']['featured']
    if tags:
        tags = ', '.join(tags)
    starters_created += 1


print(f'{starters_created} successfully created.')

# # access and normalize the data from JSON
# excerpt = starter['fields']['excerpt']
# slug = starter['fields']['slug'].replace("/blog/", "")
# # author = starter['frontmatter']['author']['id'].replace(" ", "")
# title = starter['frontmatter']['title']
# date = starter['frontmatter']['date']
# seo_title = starter['frontmatter']['seoTitle']
# canonical_link = starter['frontmatter']['canonicalLink']
# published_at = starter['frontmatter']['publishedAt']
# # content = starter['rawBody']
# tags = starter['frontmatter']['tags']
# if tags:
#     tags = ', '.join(tags)

# print(f'Processing starter {title}...')

# print(f'Searching for author "{author}" in starter:')
# # awk the user list from WP to find the proper author ID as a string
# author_id = subprocess.check_output(
#     f"awk -v author='{author}' '{{ if($2 == author) {{ print $1 }} }}' './../../../../../kyle/Github/wordpress-scripts/shell/authors.txt'", shell=True, universal_newlines=True).strip()
# print(f'Author ID found for "{author}": {author_id}')

# if not author_id:
#     print(
#         f'WARNING Failed to find an author {author} for {title}, verify manually that an author gets assigned')

# # create the post by instantiating the wp command in the shell, passing in the proper variables
# try:
#     post_id = subprocess.check_output(
#         f'wp post create --post_author={author_id} --post_date={date} --post_status="publish" --post_title="{title}" --post_excerpt="{excerpt}" --tags_input="{tags}" --published_at="{published_at}" --post_name="{slug}" --porcelain', shell=True, universal_newlines=True).strip()
#     print(f'The post id is {post_id}')
# except:
#     print('Something failed creating the base post')

# # add meta fields that come from ACF
# if seo_title:
#     os.system(f'wp post meta set {post_id} seo_title "{seo_title}"')
# if excerpt:
#     os.system(f'wp post meta set {post_id} text "{excerpt}"')
# if published_at:
#     os.system(f'wp post meta set {post_id} published_at "{published_at}"')
# if canonical_link:
#     os.system(
#         f'wp post meta set {post_id} canonical_link "{canonical_link}"')
