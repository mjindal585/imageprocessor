# Example Python Program for thresholding
from PIL import Image
import math
import time
import tkinter
from tkinter import filedialog
import os


# Method to process the red band
def pixelProcRed(intensity):
    return 0

# Method to process the blue band
def pixelProcBlue(intensity):
    return intensity

# Method to process the green band
def pixelProcGreen(intensity):
    return 0


# Create an image object
root=tkinter.Tk()
root.withdraw()

def blueband():
    print(":: Welcome To Blue Band Detection ::")
    time.sleep(0.5)
    print("Select File Path")
    time.sleep(1)
    path = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*"))) # Your image path 
    print(path)

    imageObject = Image.open(path)
    

    # Split the red, green and blue bands from the Image

    multiBands = imageObject.split()

    

    # Apply point operations that does thresholding on each color band

    redBand  = multiBands[0].point(pixelProcRed)
    greenBand  = multiBands[1].point(pixelProcGreen)
    blueBand  = multiBands[2].point(pixelProcBlue)

    blueBand.show()
   

    # Create a new image from the thresholded red, green and blue brands
    newImage = Image.merge("RGB", (redBand, greenBand, blueBand))
    

    # Display the merged image after thresholding
    newImage.show()

    print("Type exit to terminate")



if __name__ == '__main__' : 
	
	# Calling main function 
	blueband() 
