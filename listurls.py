# listurls.py
# fcbarbi Aug 2017 

import re
#import ocr

def PickURLS( text ):
  set1 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text )
  set2 = re.findall('www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text )
  return (set1 + set2)

demo1 = '<p>Hello World</p><a href="http://example.com">More Examples</a><a href="http://example2.com">Even More Examples</a>'

demo2 = 'This is a simple example of text with embedded urls http://example1.com/catalog?prod=123 in different formats, such as HTTPS as in https://example2.com or simply www.example3.com or http://www.example4.com'

# list1 = PickURLS(demo1)
# type(list1) # <class 'list'>

if __name__ == "__main__":

    image = ""
    text = ocr( image )
    urls = PickURLS( text ) 

	return urls 
