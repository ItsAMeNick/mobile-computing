import argparse
from PIL import Image
import os

def convert_to_black_and_white(input_path, output_path):
    # Open the image
    image = Image.open(input_path)

    # Convert the image to grayscale
    bw_image = image.convert("L")

    # Save the black and white image
    bw_image.save(output_path)

def convert_images_in_directory(input_directory, output_directory):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Iterate through each file in the input directory
    for filename in os.listdir(input_directory):
        input_path = os.path.join(input_directory, filename)

        # Check if the file is an image
        if input_path.lower().endswith(('.jpg')):
            # Create the output path by adding "_bw" to the original filename
            output_filename = os.path.splitext(filename)[0] + "_bw" + os.path.splitext(filename)[1]
            output_path = os.path.join(output_directory, output_filename)

            # Convert the image to black and white
            convert_to_black_and_white(input_path, output_path)

            print(f"Converted {filename} to black and white")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images in a directory to black and white.")
    parser.add_argument("input_directory", help="Path to the input directory containing images.")

    args = parser.parse_args()

    # Call the function to convert images in the input directory and save them in the output directory
    convert_images_in_directory(args.input_directory, args.input_directory + "/gray")
