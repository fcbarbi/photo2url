
# App challenge "Photo2Url"

This is just an example to show how to develop a complete simple app using Python on the backend to interpret the content of an image.

## Motivating our challenge

QR codes are handy when you look for something online but unfortunately they are not avaiable and you have to type in URLs on the street. So, why not develop an app to avoid all this typing hustle?

__"Your mission Dan/Jim, should you choose/decide to accept it,..."__ (1)

Develop an app that receives a picture and lists all the URLs in it. The front end is an app (iPhone or Android) that captures the image with the phone camera and opens a window with a list of candidate URLs. The back end is done in Python3 with an image library (PIL or pillow) and an OCR library (pyocr).

(1) https://en.wikiquote.org/wiki/Mission:_Impossible
This is how in the Mission Impossible series (aired on TV in 1970s) the recorded messaged challenged the protagonist to accept the mission. After the recording was heard, the tape self-destructed itself in flames... 

-----------------------------------------------------------------

## Part I. Solution steps

This is my first proposal to split the tasks in front and back-ends:  

1. Capture/select the image from a library or a capture it with the pone camera
2. OCR it into a list of strings
3. Filter the strings that can be URLs, strings those starting with "http://", "https://" or "www."
4. Display URLs to be clicked by the user

### Step 1

We have to collect the image of capture it from the camera on the phone. Let's see if there is a gentle way to start it:

https://developers.google.com/web/fundamentals/native-hardware/capturing-images/

### Step 2

It looks simple to call an OCR using this python library:

https://github.com/openpaperwork/pyocr

### Step 3

According to this tip, it's easy to fish URLs using regular expressions...

https://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python

```{python}
import re

demo1 = '<p>Hello World</p><a href="http://example.com">More Examples</a><a href="http://example2.com">Even More Examples</a>'

demo2 = 'This is a simple example of text with embedded urls http://example1.com/catalog?prod=123 in different formats, such as HTTPS as in https://example2.com or simply www.example3.com or http://www.example4.com'

def PickURLS( text ):
  set1 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text )
  set2 = re.findall('www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text )
  return (set1 + set2)

>>> PickURLS(demo1)
['http://example.com', 'http://example2.com']

>>> PickURLS(demo2)
['http://example1.com', 'https://example2.com', 'http://www.example4.com', 'www.example3.com', 'www.example4.com']
```

### Step 4

TBD according to the app platform chosen. More on this later...

## Part II. Back-end in Python

The file 'photo2url.py' shows the processing in the backend. You can use the example images to test the routine.
Before that install the OCR library and the python wrapper:

```
brew install tesseract

sudo pip3 install pyocr
```

If you check that you have _PIL_ (Python Imaging Library) or _pillow_ installed to handle images, you can do so with

```
pip3 list
pip3 install PIL
```
