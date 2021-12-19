#PNGTOICO
#Filip Rokita
#www.filiprokita.com



#import
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image



#def
def open():
    global imgPath; imgPath = filedialog.askopenfilename(title='Open File', initialdir='./', filetypes=[('png', '*.png')])
    convertB.configure(state=tk.NORMAL)


def conv():
    ico = Image.open(imgPath)
    ico.save(imgPath[:-4]+'.ico')



#main
root = tk.Tk()
root.title('PNGTOICO')
root.geometry('300x100')
root.resizable(False, False)


openB = tk.Button(root, text='Open', command=open, width=10); openB.pack()
convertB = tk.Button(root, text='Convert', command=conv, state=tk.DISABLED, width=10); convertB.pack()
authorL = tk.Label(root, text='www.filiprokita.com'); authorL.pack(pady=10)


root.mainloop()