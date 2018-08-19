
# coding: utf-8

from tkinter import *

from tkinter import ttk

def calculate(*args):
    try:
        value=float(feet.get())
        meters.set((0.3048*value*10000.0+0.5)/10000.0)
    except ValueError:
        pass

root=Tk()
root.title("Feet to Meters")

mainframe=ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0,row=0,sticky(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

feet=StringVar()
meters=StringVar()

ttk.Button(mainframe,text="Calculate",command=calculate).grid(column=3,row=3,sticky=W)

root.mainloop()