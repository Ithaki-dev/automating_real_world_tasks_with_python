import PIL

def resize_image(image_path, output_path, width, height):
    # Load the image
    image = PIL.Image.open(image_path)
    # Resize the image
    resized_image = image.resize((width, height))
    # Save the resized image
    resized_image.save(output_path)
    print(f"Image resized and saved to {output_path}")
    return resized_image
