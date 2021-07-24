#!/usr/bin/python
from PIL import Image, ImageGrab
import sys
from io import BytesIO
import win32clipboard

# Configure
MAX_SIZE=7999999
DENOMINATOR=7500000 # Should be ~0.5mb to 1mb less than your MAX_SIZE

img = ImageGrab.grabclipboard()

if image is None:
	print("Image is NoneType")
	exit()

# Get size of image
img_file = BytesIO()
img.save(img_file, 'bmp')
img_file_size_png = img_file.tell()
img_file.close()

if img_file_size_png < MAX_SIZE:
	print("Clipboard image not too large")
	exit()

# Determine new width & resize
w, h = img.size
percentage = img_file_size_png / DENOMINATOR
newWidth = int(w / percentage)
widthpercent = (newWidth / float(w))
height = int((float(h) * float(widthpercent)))
img = img.resize((newWidth, height), Image.ANTIALIAS)

# Force new image onto the clipboard
output = BytesIO()
img.convert('RGB').save(output, 'BMP')
data = output.getvalue()[14:]
output.close()

win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
win32clipboard.CloseClipboard()