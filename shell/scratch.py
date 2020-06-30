#!/usr/bin/env python3

import os
import subprocess
from csv import reader
import json

with open('./../../../../../kyle/Github/wordpress-scripts/posts.json') as f:
    posts = json.load(f)

print()

for post in posts['data']['allMdx']['nodes']:
    print(post['frontmatter']['title'])
