#!/usr/bin/python3
import math
import sys
from PIL import Image
import os

inputFilename = sys.argv[1]
outputFilename = os.path.splitext(inputFilename)[0] + ".img"

image = Image.open(inputFilename).convert('L')

bitsPerRow = math.ceil(image.width/8) * 8
paddingBits = bitsPerRow - image.width
outputFile = open(outputFilename, "wb")

outputFile.write(bytes((image.width,)))
outputFile.write(bytes((image.height,)))

for row in range(image.height):
	outputByte = ""
	bitCounter = 0
	for column in range(image.width):
		pixel = image.getpixel((column,row))
		if bitCounter > 7:
			outputFile.write(bytes((int(outputByte,2),)))
			outputByte = ""
			bitCounter = 0
		if pixel > 128:
			outputByte += "0"
		else:
			outputByte += "1"
		bitCounter += 1
	for i in range(0, paddingBits):
		outputByte += "0"
	outputFile.write(bytes((int(outputByte,2),)))

outputFile.close()
