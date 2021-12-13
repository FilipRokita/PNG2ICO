#PNGTOICO
#Filip Rokita
#www.filiprokita.com



#import
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image



#def
def open():
    global imgPath; imgPath = filedialog.askopenfilename(title="Open File", initialdir="./", filetypes=[("png", "*.png")])
    convB["state"] = NORMAL


def conv():
    ico = Image.open(imgPath)
    ico.save(imgPath+".ico")



#main
root = Tk()
root.title("PNGTOICO")
root.geometry("300x100")
root.resizable(False, False)


openB = Button(text="Open File", command=open, width=10); openB.pack()
convB = Button(text="Convert", command=conv, state=DISABLED, width=10); convB.pack()
authorL = Label(text="www.filiprokita.com"); authorL.pack()


root.mainloop()