#from tkinter import *
#from tkinter import messagebox as MessageBox
#import tkinter as tk

#root = Tk()
#root.title("Snake")

#def change():
    

#Button1(root, text = "Cerrar", command=quit).pack()
#Button2(root, text = "Cambiar Texto", command=change).pack()
#texto = tk.StringVar()
#label = Label(root,text="pls work",font=("Times New Roman",10)).pack()
#root.mainloop()

from tkinter import *

root = Tk()
var = StringVar()
var.set('123456')

l = Label(root, textvariable = var)
l.pack()

def change():
    var.set("654")

Button(root, text = "Cambiar Texto", command=change).pack()

#t = Entry(root, textvariable = var)
#t.pack()

root.mainloop() # the window is now displayed