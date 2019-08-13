import gery
import hide
import os
import tkinter as tk

  
def service_func(*args):
    print ("service function")
    print(var.get())

    if(var.get()=="Steganography"):
        os.system("start /B start cmd.exe @cmd /k python ./codes/hide.py")
        print("Starting hide.py")
    elif(var.get()=="Live Sketch"):
        os.system("start /B start cmd.exe @cmd /k python ./codes/sketch.py")
        print("Starting sketch.py")
    elif(var.get()=="Live Movement Detection"):
        os.system("start /B start cmd.exe @cmd /k python ./codes/movementdetection.py")
        print("Starting movementdetection.py")    
    elif(var.get()=="Threshold"):
        os.system("start /B start cmd.exe @cmd /k python ./codes/threshold.py")
        print("Starting threshold.py")
    elif(var.get()=="Median Filter"):
        os.system("start /B start cmd.exe @cmd /k python ./codes/medianfilter.py")
        print("Starting medianfilter.py")
    elif(var.get()=="Edge Enhancement"):
        os.system("start /B start cmd.exe @cmd /k python ./codes/edgeenhance.py")
        print("Starting edgeenhance.py")
    elif(var.get()=="Blurness Detection"):
        os.system("start /B start cmd.exe @cmd /k python ./codes/detect_blur.py")
        print("Starting detect_blur.py")
    elif(var.get()=="Red Band Detection"):
        os.system("start /B start cmd.exe @cmd /k python ./codes/redband.py")
        print("Starting redband.py")
    elif(var.get()=="Blue Band Detection"):
        os.system("start /B start cmd.exe @cmd /k python ./codes/blueband.py")
        print("Starting blueband.py")
    elif(var.get()=="Green Band Detection"):
        os.system("start /B start cmd.exe @cmd /k python ./codes/greenband.py")
        print("Starting greenband.py")
    elif(var.get()=="Grey Scale Conversion"):
        os.system("start /B start cmd.exe @cmd /k python ./codes/gery.py")
        print("Starting gery.py")
    elif(var.get()=="Sober Image Conversion"):
        os.system("start /B start cmd.exe @cmd /k python ./codes/sober.py")
        print("Starting sober.py")

root = tk.Tk()
root.title("Image Processor")

# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("410x410".format(positionRight, positionDown))

options = [
    "Please Select an option to begin",
    "Steganography",
    "Live Sketch",
    "Live Movement Detection",
    "Threshold",
    "Median Filter",
    "Edge Enhancement",
    "Blurness Detection",
    "Red Band Detection",
    "Blue Band Detection",
    "Green Band Detection",
    "Grey Scale Conversion",
    "Sober Image Conversion"    
]

if __name__ == '__main__':
    # service.py executed as script
    # do something
    
    label_1 = tk.Label(root,text="Welcome",font="Times 32")
    label_1.pack()

    label_2 = tk.Label(root,text="",font="Times 32")
    label_2.pack()


    var = tk.StringVar(root)
    var.set(options[0])
    var.trace("w",service_func)

    dropDownMenu = tk.OptionMenu(root,var,options[0],options[1],options[2],options[3],options[4],options[5],options[6],options[7],options[8],options[9],options[10],options[11],options[12])
    dropDownMenu.pack()

    root.mainloop()

    service_func()
    
    
