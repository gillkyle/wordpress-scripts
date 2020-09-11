#!/usr/bin/env python3

import json
import subprocess
import os

with open("../screenshots.json") as f:
    result = json.load(f)
    sites = result["data"]["allSitesYaml"]["nodes"]

for site in sites:
    url = site["main_url"]
    print(f"Trying {url}")
    # check if site has screenshot
    if site["childScreenshot"] != "null":
        # get image path
        path = site["childScreenshot"]["screenshotFile"]["publicURL"]
        image_url = "http://localhost:8000" + path
        os.system(f"curl -O {image_url}")
