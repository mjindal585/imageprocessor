from PIL import Image
from PIL import ImageFilter
import math
import time
import tkinter
from tkinter import filedialog
import os


root=tkinter.Tk()
root.withdraw()

def smooth():
    print(":: Welcome To Smooth Image ::")
    time.sleep(0.5)
    print("Select File Path")
    time.sleep(1)
    path = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*"))) # Your image path 
    print(path)    

    # Create an Image Object

    image = Image.open(path)

    

    # Apply SMOOTH filters

    smoothenedImage = image.filter(ImageFilter.SMOOTH)

    moreSmoothenedImage = image.filter(ImageFilter.SMOOTH_MORE)

    

    # Display the original image and the smoothened Images

    image.show()

    smoothenedImage.show()

    moreSmoothenedImage.show()


    print("Type exit to terminate")


if __name__ == '__main__' : 
	
	# Calling main function 
	smooth() 



