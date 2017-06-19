#!/usr/bin/env python

from PIL import Image

im = Image.open("image.jpg")
print(im.__class__)
im.show()
