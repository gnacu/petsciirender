# Breakout each individual character from PNG image containing C64 character
# set into individual GIF character images.
#
# You must install ImageMagick before using this script.
# The "magick" command must be in the current path.
#
# Usage: python breakout-charset.py --help
#
# Examples:
#     python breakout-charset.py --input-file charset-standard256-upper.png --convert-png --output-path standard256-upper --column-row-count 32x8
#     python breakout-charset.py --input-file c64studio-export.png --convert-png --output-path standard256-custom --column-row-count 16x16
#
# Tested with ImageMagick version 7.1.1-37

import sys
import os
import subprocess
import re
import argparse

argumentParser = argparse.ArgumentParser(description="Breakout each individual character from image containing C64 character set into individual character images.")
argumentParser.add_argument("--input-file", type=str, required=True, help="Specify the black and white input image file containing C64 character set (specify --column-row-count if not 16x16) of 8x8 pixels per character.")
argumentParser.add_argument("--output-path", type=str, required=True, help="Specify the output directory path (must already exist) where individual GIF images for each character will be generated (named 0.gif, ..., 255.gif).", default=None)
argumentParser.add_argument("--column-row-count", type=str, required=False, help="Specify the character column and row count of the input file (e.g. 16x16 for C64 Studio, 32x8 for included example files).", default="16x16")
argumentParser.add_argument("--convert-png", action="store_true", required=False, help="Convert PNG image to GIF before processing.", default=False)
args = argumentParser.parse_args()

gifInputFile = re.sub("\\.[a-zA-Z]+$", ".gif", args.input_file)

if args.convert_png:
    # refer to: https://www.imagemagick.org/discourse-server/viewtopic.php?t=3037
    print("magick convert " + args.input_file + " -background black -flatten " + gifInputFile)
    subprocess.run("magick convert " + args.input_file + " -background black -flatten " + gifInputFile)

# refer to: https://imagemagick.org/Usage/crop/
print("magick " + gifInputFile + " -crop " + args.column_row_count + "@ +repage +adjoin " + args.output_path + "/char.gif")
subprocess.run("magick " + gifInputFile + " -crop " + args.column_row_count + "@ +repage +adjoin " + args.output_path + "/char.gif")

files = os.listdir(args.output_path)
for file in files:
    newName = re.sub("char-", "", file)
    print("rename " + args.output_path + "/" + file + " to " + args.output_path + "/" + newName)
    os.rename(args.output_path + "/" + file, args.output_path + "/" + newName)

