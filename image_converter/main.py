from PIL import Image
import os
# Current phat to the image file
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "bride.jpg")
# Open the image file and rotate it by 45 degrees
im = Image.open(image_path)
im.rotate(45).show()
