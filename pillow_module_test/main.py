from PIL import Image
import os
# Current phat to the image file
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "bride.jpg")
new_image_path = os.path.join(current_path, "new_bride.jpg")
# Open the image file and rotate it by 45 degrees
im = Image.open(image_path)
# Rotate the image by 45 degrees
# im.rotate(45).show()
# Resize the image to 50% of its original size
# im = im.resize((400,600)).show()
# Save the image in PNG format
new_img = im.resize((900,1000)).rotate(180).save(new_image_path)