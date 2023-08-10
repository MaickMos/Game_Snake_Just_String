from tkinter import *
from tkinter import messagebox as MessageBox
import tkinter as tk
import time
import random
from pynput import keyboard as kb
import threading

#Tamaño
largo=70
alto=40
out = []
salida=""
snake = largo*4+6
presnake = [snake-1,snake-1,snake-1]
size=2
vel=0.1
numvel=1
aux=0
teclaG = kb.KeyCode.from_char('d')

#Crear mapa de juego
def Crear():
    #0 Espacio libre
    #1 Barrera
    #2 Snake
    #3 Huevo
    #4 Salto de linea
    for i in range(largo):
        out.append(1)

    for i in range(alto-2):
        out.append(4)
        out.append(1)

        for i in range(largo-2):
            out.append(0)

        out.append(1)
    out.append(4)

    for i in range(largo):
        out.append(1)

#Posicion Huevo
def PosEgg():
    global out
    global egg
    b=1
    while b==1:
        egg=random.randrange(len(out))
        #acoplamiento
        if out[egg]==0:
            out[egg]=3
            b=0
        else:
            print("Re Ubicando el huevo...")

#Posicion Serpiente
def PosSnake(teclaa):
    global snake
    global out
    global size
    global vel
    global numvel
    global aux
    if teclaa == kb.KeyCode.from_char('w'):
        #print(presnake[size])
        out[presnake[size]]=0
        for i in range(size):
            presnake[size-i]=presnake[size-i-1]
        presnake[0]=snake
        snake=snake-largo-1
            
    if teclaa == kb.KeyCode.from_char('s'):
        out[presnake[size]]=0
        for i in range(size):
            presnake[size-i]=presnake[size-i-1]
        presnake[0]=snake
        snake=snake+largo+1

    if teclaa == kb.KeyCode.from_char('a'):
        out[presnake[size]]=0
        for i in range(size):
            presnake[size-i]=presnake[size-i-1]
        presnake[0]=snake
        snake=snake-1

    if teclaa == kb.KeyCode.from_char('d'):
        out[presnake[size]]=0
        for i in range(size):
            presnake[size-i]=presnake[size-i-1]
        presnake[0]=snake
        snake=snake+1
    
    #print("Pos Snake en: "+str(snake))
    #acoplamiento
    if out[snake]==0:
        out[snake]=2
    else:
        #aumentar tamaño 
        if out[snake]==3:
            out[snake]=2
            size=size+1
            presnake.append(snake)
            print("Aumento de tamaño a "+str(len(presnake)+1))
            print("Size :"+str(size))
            aux=aux+1
            if(aux==5):
                numvel=numvel+1
                aux=0

            vel=0.1/numvel
            print("vel: "+str(vel)+" numvel :"+str(numvel))
            PosEgg()
        else:
            #Mensaje error
            print("Perdiste xd")
            test()
            root.quit()
            exit()

    #Graficar serpiente
    for i in range(size):
       out[presnake[i]]=2
    #out[presnake.pop()]=2
        

def Matriz():
    num=0
    for i in range(len(out)):
        if out[i]==4:
            print("")
        else:
            print(num,end=',')
        num=num+1

root = Tk()
root.title("Snake")
var = StringVar()
var.set("0")
pun = StringVar()
pun.set("Puntuacion: 0")
labvel = StringVar()
labvel.set("Velocidad : 1")

def change():
    global numvel
    numvel=numvel+1

def test():
    MessageBox.showinfo("GAME OVER", "Perdiste") # título, mensaje

label = Label(root,textvariable=var,font=("Times New Roman",10))
label.pack()

labelpun = Label(root,textvariable=pun,font=("Times New Roman",10))
labelpun.pack(anchor=NW)

labelvel = Label(root,textvariable=labvel,font=("Times New Roman",10))
labelvel.pack(anchor=SE)

Button(root, text = "Aumentar velocidad", command=change).pack()


#Codificacion
def ActuSalida():
    global salida
    salida=""
    for i in range(len(out)):
        if out[i]==0:
            salida=salida+"   "
        if out[i]==1:
            salida=salida+"█"
        if out[i]==2:
            salida=salida+"Ø"
        if out[i]==3:
            salida=salida+"* "
        if out[i]==4:
            salida=salida+"\n"
    var.set(salida)
    pun.set("Puntuacion: "+str(size-2))
    labvel.set("Velocidad : "+str(numvel))

def pulsa(tecla):
    global teclaG
    if tecla == kb.KeyCode.from_char('w') or tecla == kb.KeyCode.from_char('d') or tecla == kb.KeyCode.from_char('s') or tecla == kb.KeyCode.from_char('a'):
        teclaG=tecla


def bucle():
    while True:
        PosSnake(teclaG)
        ActuSalida()
        time.sleep(vel)

Crear()
PosEgg()
PosSnake(teclaG)
ActuSalida()


escuchador = kb.Listener(pulsa)
escuchador.start()

hilo1 = threading.Thread(target=bucle)
hilo1.start()
root.mainloop()