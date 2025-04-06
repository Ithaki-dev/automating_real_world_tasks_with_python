# This is an script that fix the images in the Module 1 certificate practice.
from PIL import Image
import os

# Image directory path
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# Create a new directory to store the fixed images
new_image_path = os.path.join(current_path, "fixed_images")


# Loop through all the images in the directory

for image in os.listdir(image_path):
    if '.' not in image[0]:
        img = Image.open(os.path.join(image_path, image))
        # Resize, rotate and save in JPG format
        img = img.resize((900, 1000)).rotate(180).convert("RGB")
        # Save the image in the new directory
        if not os.path.exists(new_image_path):
            os.makedirs(new_image_path)
        img.save(os.path.join(new_image_path, image.split(".")[0] + ".jpg"), "JPEG")
        print(f"Processed and saved {image} to {new_image_path}")
        img.close()  # Close the image file to free up resources
# This script resizes, rotates and saves images in a new directory.
