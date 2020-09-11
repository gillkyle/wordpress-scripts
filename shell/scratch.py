#!/usr/bin/env python3

import os
import subprocess
from csv import reader
import json

with open('./../../../../../kyle/Github/wordpress-scripts/starters.json') as f:
    starters = json.load(f)

print()

for starter in starters['data']['allStartersYaml']['nodes']:
    image_path = starter['childScreenshot']['screenshotFile']['publicURL'].split(
        "/")[3]

    os.system(
        f"cp {starter['childScreenshot']['screenshotFile']['absolutePath']} ./../../../../../kyle/Github/wordpress-scripts/local-images/{image_path}")
