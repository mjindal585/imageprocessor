import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
import tkinter
from tkinter import filedialog
import os

root=tkinter.Tk()
root.withdraw()
def threshold():
    print(":: Welcome To Thresholding ::")
    time.sleep(0.5)
    print("Select File Path")
    time.sleep(1)
    path = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*"))) # Your image path 
    print(path)

    img = cv2.imread(path,0)
    img = cv2.medianBlur(img,5)

    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,11,2)

    titles = ['Original Image', 'Global Thresholding',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]

    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

    print("Type exit to terminate")


if __name__ == '__main__' : 
	
	# Calling main function 
	threshold() 
