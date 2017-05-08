#!/usr/bin/env

from PIL import Image
import binascii
import sys

def binstrToascii(binstr):
    str = ""
    for i in range(0,len(binstr),8):
             str+=chr(int(binstr[i:i+8],2))
    return str



image = Image.open( sys.argv[1] )

hidden = ""

for y in range(image.height):
	for x in range(image.width):
		rgb = map(lambda i: i&1, image.getpixel((x,y)))
		hidden = hidden + str(rgb[2])+str(rgb[1])+str(rgb[0])


print binstrToascii(hidden)


image.close()
