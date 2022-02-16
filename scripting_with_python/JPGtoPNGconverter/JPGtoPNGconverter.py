# Program that converts all JPG files in a specified directory to PNG files in specified directory.
# Terminal arguments: python JPGtoPNGconverter.py <JPG images folder name> <PNG output folder name>
# Terminal example: python JPGtoPNGconverter.py JPGimages PNGoutput

import os
import sys
from PIL import Image

try:
    # Get the name of the folder containing the JPG images.
    jpg_directory = sys.argv[1]
    if not os.path.exists(jpg_directory):
        print("Error: The JPG images folder does not exist.")
        exit()
    # Get the name of the folder where the PNG images will be saved.
    png_directory = sys.argv[2]
    if not os.path.exists(png_directory):
        print(f"No directory '{png_directory}' found. Creating directory.")
        os.makedirs(png_directory)
    # Get a list of all the JPG files in the specified directory.
    for file in os.scandir(jpg_directory):
        jpg_img = Image.open(file.path)
        # Save the JPG image as a PNG image in png_directory.
        png_img = jpg_img.convert('RGB')
        png_img.save(png_directory + '/' + file.name[:-3] + 'png', 'png')
except IndexError:
    print(
        """
        ERROR: Please enter valid terminal arguments.
        
        Terminal arguments: python JPGtoPNGconverter.py <JPG images folder name> <PNG output folder name>
        Terminal example: python JPGtoPNGconverter.py JPGimages PNGoutput
        """)
    exit()
