from turtle import*
from tkinter import*
import ctypes



bgcolor("black")
speed(100)
pensize(10)
def space():
    penup()
    lt(45)
    fd(24)
    pendown()
def position():
    penup()
    goto(-300,300)
    pendown()
def letter_a():
    color("dimgray")
    rt(45)
    fillcolor("dimgray")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()

position()

def cipher():
    data = text_area.get("1.0",END)

    As,Ts,Cs,Gs, = 0,0,0,0

    for x in data:
        if 'a' == x:
            As+=1
            letter_a()
        elif x == 'T':
            Ts+=1
        elif x =='C':
            Cs+=1
        elif x == 'G':
            Gs+=1
    result.set('Num As: '+str(As)+' Num of Ts: '+str(Ts)+' Num Cs: '+str(Cs)+' Num Gs: '+str(Gs))

window = Tk()

frame=Frame(window)
frame.pack()

text_area = Text(frame)
text_area.pack()

result = StringVar()
result.set('Num As: 0 Num of Ts: 0 Num Cs: 0 Num Gs: 0')
label=Label(window,textvariable=result)
label.pack()

button=Button(window,text="Count", command=cipher)
button.pack()

window.mainloop()
