import argparse
from PIL import Image
import os

def make_square(image_path):
    # Open the image
    image = Image.open(image_path)

    # Make the image square
    x, y = image.size
    size = max(x, y)

    square_image = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    square_image.paste(image, (int((size - x) / 2), int((size - y) / 2)))

    # Create the output path by adding "_bw" to the original filename
    output_filename = os.path.basename(os.path.splitext(image_path)[0]) + "_square.png"
    print(output_filename)
    output_path = os.path.join(os.path.dirname(image_path), output_filename)
    print(output_path)

    # Save the black and white image
    square_image.save(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Makes image square.")
    parser.add_argument("image_path", help="Path to the input directory containing images.")

    args = parser.parse_args()

    # Call the function to convert images in the input directory and save them in the output directory
    make_square(args.image_path)
