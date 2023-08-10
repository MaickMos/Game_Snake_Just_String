from tkinter import *
from tkinter import messagebox as MessageBox
import time
import random

def  Actu():
    out=""
    #Barrera
    for i in range(100):
        out=out+"▄"

    for i in range(40):
        out=out+"\n"
        out=out+"█"

        for i in range(98):
            out=out+"   "

        out=out+"█"
    out=out+"\n"
    for i in range(100):
        out=out+"▀"
    #print(len(out))
    Egg=random.randrange(12080)
    print(Egg)
    return out

def window():
    MessageBox.showinfo("Snake","Snake2")

root = Tk()
root.title("Snake")
#root.geometry("520x900")

label = Label(root,text=Actu(),font=("Times New Roman",10)).pack()
#label.config(font=("Verdana",12))

Button(root, text = "Cerrar", command=quit).pack()


root.mainloop()