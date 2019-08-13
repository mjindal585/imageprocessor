from PIL import Image, ImageDraw , ImageFont
from PIL import ImageFilter
import math
import time
import tkinter
from tkinter import filedialog
import os


root=tkinter.Tk()
root.withdraw()
def gery():

    print(":: Welcome To Gray Scale Convertor ::")
    time.sleep(0.5)
    print("Select File Path")
    time.sleep(1)
    path = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*"))) # Your image path 
    print(path)

    

    # Create an Image Object

    image2 = Image.open(path).convert('LA')
    idraw = ImageDraw.Draw(image2)
    text = "\N{COPYRIGHT SIGN}"+"mjindal585"

    font = ImageFont.truetype("arial.ttf", size=12)

    idraw.text((10, 10), text, font=font)
        
                
                
    savepath = input("Enter destination path (with file name and extension) : ")   
    print(savepath) 

    image2.save(savepath)    

    image2.show()


    print("Type exit to terminate")
    



if __name__ == '__main__' : 
	
	# Calling main function 
	gery() 

