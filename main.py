from tkinter import *

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

fenster = Tk()
fenster.title('Calculator')
fenster.geometry('124x150')

e1 = Entry(fenster)
e2 = Entry(fenster)
erg_label = Label(fenster, text='Ergebnis:', width='6')
e1.place(x=0, y=0)
e2.place(x=0, y=20)
erg_label.place(x=0, y=45)

plus = Button(fenster, text='+',width='3', command=addition)
minus = Button(fenster, text='-',width='3', command=subtraction)
multiply = Button(fenster, text='x',width='3', command=multiplication)
divide = Button(fenster, text='÷',width='3', command=division)
plus.place(x=0, y=70)
minus.place(x=31, y=70)
multiply.place(x=62, y=70)
divide.place(x=93, y=70)

exit_button = Button(fenster, text='Exit',width='5', command=exit)
exit_button.place(x=38, y=110)


fenster.mainloop()