# USAGE
# python detect_blur.py --images images

# import the necessary packages
from imutils import paths
import argparse
import cv2

from PIL import Image
from PIL import ImageFilter
import math
import time
import tkinter
from tkinter import filedialog
import os

def variance_of_laplacian(image):
    	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()


root=tkinter.Tk()
root.withdraw()

print(":: Welcome To Blurness Scale Detection ::")
time.sleep(0.5)
print("Select File Path")
time.sleep(1)
path = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*"))) # Your image path 
print(path)
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)
text = "Not Blurry"

		# if the focus measure is less than the supplied threshold,
		# then the image should be considered "blurry"
if (fm < 100):
		text = "Blurry"

		# show the image
cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.imshow("Image", image)
key = cv2.waitKey(0)

print("Type exit to terminate")

