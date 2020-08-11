from PIL import Image
import sys
import os

#img  = Image.open(path)      
# On successful execution of this statement, 
# an object of Image type is returned and stored in img variable) 
   
try:  
    img  = Image.open("/home/captain/Pictures/hacker.jpeg")
except IOError: 
    pass

img.show()
# Use the above statement within try block, as it can  
# raise an IOError if file cannot be found,  
# or image cannot be opened