#PNGTOICO
#Filip Rokita
#www.filiprokita.com

import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image

root = tk.Tk()
root.title("PNGTOICO")
root.geometry("300x100")

def getFile():
    filetypes = (
        ("png", "*.png"),
        ("All files", "*.*")
    )
    global pngImgPath
    global icoImgPath
    pngImgPath = fd.askopenfilename(title="Open File", initialdir="./", filetypes=filetypes)
    icoImgPath = pngImgPath+".ico"
    convertB["state"] = tk.NORMAL

def convert():
    img = Image.open(pngImgPath)
    img.save(icoImgPath)


getFileB = tk.Button(text="Open File", width="10", command=getFile); getFileB.pack()
convertB = tk.Button(text="Convert", width="10", command=convert, state=tk.DISABLED); convertB.pack()
authorL = tk.Label(text="www.filiprokita.com"); authorL.pack(pady="10")


root.mainloop()