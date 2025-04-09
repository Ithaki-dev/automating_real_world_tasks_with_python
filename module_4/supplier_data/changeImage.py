#!/usr/bin/env python3
from PIL import Image
import os

current_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_path, 'images')
image_path_new = os.path.join(current_path, 'images_new')

for f in os.listdir(image_path):
    if f.endswith('.jpg'):
        im = Image.open(os.path.join(image_path, f)).convert('RGB')
        # resize the image to 600x400 pixels
        im = im.resize((600, 400))
        # save the image in the new directory
        try:
            os.makedirs(image_path_new)
        except FileExistsError:
            pass
        im.save(os.path.join(image_path_new, f))
        # print the image name
        print(f'Image {f} has been resized and saved to {image_path_new}')