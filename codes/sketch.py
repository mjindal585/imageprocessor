import cv2
import numpy as np

# function to generate sketch
def sketch(image):
    #convert image to grayscale
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    #clean up image using Gaussian blur
    img_gray_blur=cv2.GaussianBlur(img_gray,(5,5),0)
    
    #exract edges
    canny_edges=cv2.Canny(img_gray_blur,10,70)
    
    #bineries the image
    ret,mask=cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return mask
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow('Live Sketch',sketch(frame))
    if cv2.waitKey(1) == 13:  #13 is the Enter value on the keyboard
        break
        
#release the camera and close window
cap.release()
cv2.destroyAllWindows()


print("Type exit to terminate")


