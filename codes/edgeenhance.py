# import image module

from PIL import Image

from PIL import ImageFilter

from PIL import ImageDraw, ImageFont
import math
import time
import tkinter
from tkinter import filedialog
import os


root=tkinter.Tk()
root.withdraw()

def edgeenhance():
    print(":: Welcome To Edge Enhancement ::")
    time.sleep(0.5)
    print("Select File Path")
    time.sleep(1)

    path = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*"))) # Your image path 
    print(path)

    

    # Open an already existing image

    imageObject = Image.open(path)

    

    # Apply edge enhancement filter

    edgeEnahnced = imageObject.filter(ImageFilter.EDGE_ENHANCE)

    

    # Apply increased edge enhancement filter

    moreEdgeEnahnced = imageObject.filter(ImageFilter.EDGE_ENHANCE_MORE)

    

    # Show original image - before applying edge enhancement filters

    imageObject.show() 

    

    # Show image - after applying edge enhancement filter

    edgeEnahnced.show()

    

    # Show image - after applying increased edge enhancement filter

    moreEdgeEnahnced.show()

    print("Type exit to terminate")



if __name__ == '__main__' : 
	
	# Calling main function 
	edgeenhance() 
