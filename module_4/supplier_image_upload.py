#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

current_path = os.path.dirname(os.path.abspath(__file__))
new_images_path = os.path.join(current_path, 'images_new')

url = "http://localhost/upload/"
for f in os.listdir(new_images_path):
    # Check if the file is a JPEG image
    if f.endswith(".jpeg"):
        with open(new_images_path + f, 'rb') as opened:
            r = requests.post(url, files={'file': opened})