#!/usr/bin/env python3

import os
import subprocess
from csv import reader
import json

# this script is run from the terminal that has ssh'd into a Local WordPress terminal
# via "Open Site Shell". It is run with like so:
# $ ./../../../../../kyle/Github/wordpress-scripts/shell/import-posts.py

# You can run system/wp commands like this:
# os.system('wp user list')

basePath = "./../../../../../kyle/Github/wordpress-scripts"

# the posts.csv file comes from an online JSON to CSV conversion after running
# the all-blog-post.graphql query in the GatsbyJS.org wwww site
# 0 fields_slug
# 1 fields_excerpt
# 2 frontmatter_author_id
# 3 frontmatter_date
# 4 frontmatter_title
# 5 frontmatter_canonicalLink
# 6 frontmatter_publishedAt
# 7 frontmatter_tags
# 8 frontmatter_image_id
# 9 frontmatter_image_relativePath
# 10 frontmatter_imageTitle
# 11 rawBody

with open('./../../../../../kyle/Github/wordpress-scripts/posts.json') as f:
    posts = json.load(f)

print()

for post in posts['data']['allMdx']['nodes']:
    author = post['frontmatter']['author']['id'].replace(" ", "")
    title = post['frontmatter']['title']
    print(f'Processing post {title}...')

    print(f'Searching for author "{author}" in post:')
    # awk the user list from WP to find the proper author ID as a string
    author_id = subprocess.check_output(
        f"awk -v author='{author}' '{{ if($2 == author) {{ print $1 }} }}' './../../../../../kyle/Github/wordpress-scripts/shell/authors.txt'", shell=True, universal_newlines=True).strip()
    print(f'Author ID found for "{author}": {author_id}')

# with open(f'{basePath}/posts.csv', 'r') as read_obj:
#     # pass the file object to reader() to get the reader object
#     csv_reader = reader(read_obj)
#     header = next(csv_reader)

#     # Iterate over each row in the csv using reader object
#     for row in csv_reader:
#         post_slug = row[0]
#         post_author = row[2]
#         post_title = row[4]
#         post_tags = row[7]
#         post_raw_body = row[11]
#         # row variable is a list that represents a row in csv
#         print(f'Processing post {post_title}...')
#         # find the author of the post from authors.txt
#         # txt file created like this: $ wp user list > ./../../../../../kyle/Github/wordpress-scripts/shell/authors.txt
#         print(f'Searching for author "{post_author}" in post:')
#         # remove space from name to match username in awk output
#         # ie "Kyle Mathew" -> "KyleMathews"
#         author_name = post_author.replace(" ", "")

#         # awk the user list from WP to find the proper author ID as a string
#         author_id = subprocess.check_output(
#             f"awk -v author='{author_name}' '{{ if($2 == author) {{ print $1 }} }}' './../../../../../kyle/Github/wordpress-scripts/shell/authors.txt'", shell=True, universal_newlines=True).strip()
#         print(f'Author ID found for "{post_author}": {author_id}')
#         # print(author_id == '3')
#         # print(int(author_id) == 3)

#         # post creation
#         # os.system(
#         #     f'wp post create --post_author={author_id} --post_title="{post_title}"')

#         # print(f'{post_slug} {post_author} {post_tags}')
#         # print(f'{post_raw_body}')
#         # print("------")

print("done")
