from PIL import Image , ImageDraw, ImageFont
import math
import time
import tkinter
from tkinter import filedialog
import os



def medianfilter():        
        root=tkinter.Tk()
        root.withdraw()
        print(":: Welcome To Median Filtering ::")
        time.sleep(0.5)
        print("Select File Path")
        time.sleep(1)
        path = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*"))) # Your image path 
        print(path)
        img = Image.open(path)
        members = [(0,0)] * 9
        newimg = Image.new("RGB",(img.width,img.height),"white")
        for i in range(1,img.width-1):
         for j in range(1,img.height-1):
                members[0] = img.getpixel((i-1,j-1))
                members[1] = img.getpixel((i-1,j))
                members[2] = img.getpixel((i-1,j+1))
                members[3] = img.getpixel((i,j-1))
                members[4] = img.getpixel((i,j))
                members[5] = img.getpixel((i,j+1))
                members[6] = img.getpixel((i+1,j-1))
                members[7] = img.getpixel((i+1,j))
                members[8] = img.getpixel((i+1,j+1))
                members.sort()
                newimg.putpixel((i,j),(members[4]))
        
        idraw = ImageDraw.Draw(newimg)
        text = "\N{COPYRIGHT SIGN}"+"mjindal585"
        font = ImageFont.truetype("arial.ttf", size=12)
        idraw.text((0, 0), text, font=font)

        destpath = input("Enter Destination Path : ")
        print(destpath)
        newimg.save(destpath)

        print("Type exit to terminate")

if __name__ == '__main__' : 
	
	# Calling main function 
	medianfilter() 