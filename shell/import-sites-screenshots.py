#!/usr/bin/env python3

# wp post list --format=json --fields=main_url,ID --post_type=sites
# then clear out stuff to match the python dict

import json
import subprocess
import os

with open("./../../../../../kyle/Github/wordpress-scripts/screenshots.json") as f:
    result = json.load(f)
    sites = result["data"]["allSitesYaml"]["nodes"]

with open("./../../../../../kyle/Github/wordpress-scripts/ids_sites_dict.txt") as f:
    ids_urls = eval(f.read())

for site in sites:
    url = site["main_url"]
    print(f"Trying {url}")

    site_id = ids_urls[url]

    # check if site has screenshot
    if site["childScreenshot"] != "null":
        # get image path
        image_name = site["childScreenshot"]["screenshotFile"]["publicURL"].split(
            "/")[3]
        image_url = "./../../../../../kyle/Github/wordpress-scripts/local-images/" + image_name

        # upload image and get ID
        image_id = subprocess.check_output(
            f"wp media import {image_url} --porcelain", shell=True).decode("utf-8").strip()

        # update site's featured image field to be image ID
        os.system(f"wp post meta update {site_id} screenshot {image_id}")
        print(f"Updated {url}'s screenshot with image {image_id}\n")

    else:
        print(f"Skipping {url} {site_id} due to no screenshot\n")
