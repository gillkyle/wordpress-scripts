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

# load the starters queried from GraphiQL on .org
with open('./../../../../../kyle/Github/wordpress-scripts/starters.json') as f:
    starters_data = json.load(f)

starters = starters_data['data']['allStartersYaml']['nodes']

# load the starters on WP to compare with the ones from .org
with open('./../../../../../kyle/Github/wordpress-scripts/wp-starters.json') as f:
    wp_starters = json.load(f)

# nice, inefficient loop within a loop to filter down to the right data from both files
for wp_starter in wp_starters:
    for starter in starters:
        starter_title = starter['repo'].replace("https://github.com/", "")
        wp_starter_title = wp_starter['post_title']
        if starter_title == wp_starter_title:
            site_id = wp_starter["ID"]
            # check if site has screenshot
            if starter["childScreenshot"] is not None:
                # get image path
                path = starter["childScreenshot"]["screenshotFile"]["publicURL"]
                image_url = "https://gatsbyjs.org" + path

                # upload image and get ID
                image_id = subprocess.check_output(
                    f"wp media import {image_url} --porcelain", shell=True).decode("utf-8").strip()

                # update site's featured image field to be image ID
                os.system(
                    f"wp post meta update {site_id} screenshot {image_id}")
                print(
                    f"Updated {starter_title}'s screenshot with image {image_id}\n")
            else:
                print(f"Skipping {starter_title} due to no screenshot\n")
