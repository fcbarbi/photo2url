#!/usr/local/bin/python

# photo2url.py 
# fcbarbi 10 Aug 2017 

# EXAMPLE: 
# $ python3 ./photo2url.py
# Will use tool 'Tesseract (sh)'
# Available languages: eng, osd
# Will use lang 'eng'
# urls in image  IMG_0320.JPG  are:  ['www.operettensommer.ch']

# TODO: 
# detect if image should rotate 
# choose OCR language
# improve url detection in scanned text 

#import os
#os.getcwd()

# image to scan 
read_image = "IMG_0320.JPG"
#read_image = "IMG_0321.JPG"

# PIL = Python Imaging Library
# http://pillow.readthedocs.io/en/3.4.x/reference/Image.html
from PIL import Image
#import sys

img0 = Image.open(read_image)

# TODO how can we know that we should rotate the image?
# http://effbot.org/imagingbook/image.htm
# list(im.getdata())
# im.size (4032, 3024)

#if img.height()<img.width(): 
img = img0.rotate(-90) # "IMG_0320.JPG"
#img = img0  # "IMG_0321.JPG"
img.show() 

# install OCR library
# Optical Character Recognition (OCR) 
# https://github.com/tesseract-ocr/
# brew install tesseract

# pyocr is a python wrapper for Tesseract and Cuneiform
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# List avaibale languages
langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
# TODO user should be able to choose best fit  
lang = langs[0]
print("Will use lang '%s'" % (lang))
# Orientation and script detection (OSD) 

# Add OCR support to German (deu), French (fre), Portuguese (por) and Italian (ita) 
# https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc#languages

# perform the ocr and generate one string with all the text in the image 
builder = pyocr.builders.TextBuilder()
scannedtext = tool.image_to_string( im, lang=lang, builder=builder )

print( 'scanned text is ',scannedtext )

# Parse the scanned text for possible URLs
# https://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
import re

def PickURLS( text ):
  set1 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text )
  set2 = re.findall('www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text )
  return (set1 + set2)

urls = PickURLS( scannedtext ) 

# TODO analyze the scanned text to improve URL pattern recongition 
# example: "AC C 0 www accobrands. com" should return "www.accobrands.com"
print( 'urls in image ',read_image,' are: ', urls )

# urls in image  IMG_0320.JPG  are:  ['www.operettensommer.ch']
# urls in image  IMG_0321.JPG  are:  ['www accobrands.']






