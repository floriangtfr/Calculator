from main import *

def addition():
    zahl1 = e1.get()
    zahl2 = e2.get()
    erg = int(zahl1) + int(zahl2)
    e1.delete(0,30)
    e2.delete(0,30)
    label = Label(fenster, text=erg)
    label.place(x=55, y=45)

def subtraction():
    zahl1 = e1.get()
    zahl2 = e2.get()
    erg = int(zahl1) - int(zahl2)
    e1.delete(0,30)
    e2.delete(0,30)
    label = Label(fenster, text=erg)
    label.place(x=55, y=45)

def multiplication():
    zahl1 = e1.get()
    zahl2 = e2.get()
    erg = int(zahl1) * int(zahl2)
    e1.delete(0,30)
    e2.delete(0,30)
    label = Label(fenster, text=erg)
    label.place(x=55, y=45)

def division():
    zahl1 = e1.get()
    zahl2 = e2.get()
    erg = int(zahl1) / int(zahl2)
    e1.delete(0,30)
    e2.delete(0,30)
    label = Label(fenster, text=erg)
    label.place(x=55, y=45)

def exit():
    fenster.quit()