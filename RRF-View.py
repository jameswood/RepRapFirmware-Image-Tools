#!/usr/bin/python3
import math
import sys

inputFile = open(sys.argv[1], "rb")
print("opening ", sys.argv[1])
contents = inputFile.read()
byteCount = 0
imageBytes = ''

for char in contents:
	if byteCount == 0: width=char
	elif byteCount == 1: height = char
	else:
		imageBytes += "{:08b}".format(char)
	byteCount += 1

bitsPerRow = math.ceil(width/8) * 8

print(" width: ", width)
print("height: ", height)
print("padded bits per row: ", bitsPerRow)

bitNumber = 1
row = 0
for bit in imageBytes:
	if bit == '0': bit = '◻︎'
	if bit == '1': bit = '◼︎'
	if bitNumber - (bitsPerRow * row) <= width:
		print(bit, end='')
	if bitNumber % bitsPerRow == 0:
		print()
		row += 1
	bitNumber += 1
