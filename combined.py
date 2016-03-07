from turtle import*
import tkinter as tk
import ctypes
from tkinter.simpledialog import askstring



index = 0
stack = []
name = input("Enter some text! ")
while index < len(name):
   letter = name[index]
   num = ord(letter)
   stack.append(num)
   index += 1


#class typing():
#    def
bgcolor("black")
speed(100)
def space():
    penup()
    lt(45)
    fd(24)
    pendown()
def position():
    penup()
    goto(-300,300)
    pendown()
pensize(10)
def space_button():
    color("black")
    rt(45)
    fillcolor("black")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()

def letter_q():
    color("#A4C639")
    rt(45)
    fillcolor("#A4C639")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_w():
    color("#F0F8FF")
    rt(45)
    fillcolor("#F0F8FF")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_e():
    color("#FFC1CC")
    rt(45)
    fillcolor("#FFC1CC")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_r():
    color("#E9967A")
    rt(45)
    fillcolor("#E9967A")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_t():
    color("salmon")
    rt(45)
    fillcolor("salmon")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_y():
    color("darkslateblue")
    rt(45)
    fillcolor("darkslateblue")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_u():
    color("thistle")
    rt(45)
    fillcolor("thistle")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_i():
    color("#79443B")
    rt(45)
    fillcolor("#79443B")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_o():
    color("cornflowerblue")
    rt(45)
    fillcolor("cornflowerblue")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_p():
    color("greenyellow")
    rt(45)
    fillcolor("greenyellow")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_a():
    color("dimgray")
    rt(45)
    fillcolor("dimgray")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_s():
    color("darkgreen")
    rt(45)
    fillcolor("darkgreen")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_d():
    color("darkred")
    rt(45)
    fillcolor("darkred")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_f():
    color("red")
    rt(45)
    fillcolor("red")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_g():
    color("peachpuff")
    rt(45)
    fillcolor("peachpuff")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()

def letter_h(): 
    color("#7FFFD4")
    rt(45)
    fillcolor("#7FFFD4")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_j():
    color("blue")
    rt(45)
    fillcolor("blue")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()

def letter_k():
    color("orange")
    rt(45)
    fillcolor("orange")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
    
def letter_l():
    color("DarkCyan")
    rt(45)
    fillcolor("DarkCyan")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_m():
    color("DarkViolet")
    rt(45)
    fillcolor("DarkViolet")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_n():
    color("gold")
    rt(45)
    fillcolor("gold")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_b():
    color("LightBlue")
    rt(45)
    fillcolor("LightBlue")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_v():
    color("navy")
    rt(45)
    fillcolor("navy")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()

def letter_c():
    color("sienna")
    rt(45)
    fillcolor("sienna")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_x():
    color("tan")
    rt(45)
    fillcolor("tan")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def letter_z():
    color("pink")
    rt(45)
    fillcolor("pink")
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space() 

listen()
position()
for x in range (0, len(stack)):
    if (stack[x] == 97):
        letter_a()
    if (stack[x] == 98):
        letter_b()
    if (stack[x] == 99):
        letter_c()
    if (stack[x] == 100):
        letter_d()
    if (stack[x] == 101):
        letter_e()
    if (stack[x] == 102):
        letter_f()
    if (stack[x] == 103):
        letter_g()
    if (stack[x] == 104):
        letter_h()
    if (stack[x] == 105):
        letter_i()
    if (stack[x] == 106):
        letter_j()
    if (stack[x] == 107):
        letter_k()
    if (stack[x] == 108):
        letter_l()
    if (stack[x] == 109):
        letter_m()
    if (stack[x] == 110):
        letter_n()
    if (stack[x] == 111):
        letter_o()
    if (stack[x] == 112):
        letter_p()
    if (stack[x] == 113):
        letter_q()
    if (stack[x] == 114):
        letter_r()
    if (stack[x] == 115):
        letter_s()
    if (stack[x] == 116):
        letter_t()
    if (stack[x] == 117):
        letter_u()
    if (stack[x] == 118):
        letter_v()
    if (stack[x] == 119):
        letter_w()
    if (stack[x] == 120):
        letter_x()
    if (stack[x] == 121):
        letter_y()
    if (stack[x] == 122):
        letter_z()


               
               
#def first():
#    letter_h()
"""listen()
position()
onkey(letter_a, "a")
onkey(letter_b, "b")
onkey(letter_c, "c")
onkey(letter_d, "d")
onkey(letter_e, "e")
onkey(letter_f, "f")
onkey(letter_g, "g")
onkey(letter_h, "h")
onkey(letter_i, "i")
onkey(letter_j, "j")
onkey(letter_k, "k")
onkey(letter_l, "l")
onkey(letter_m, "m")
onkey(letter_n, "n")
onkey(letter_o, "o")
onkey(letter_p, "p")
onkey(letter_q, "q")
onkey(letter_r, "r")
onkey(letter_s, "s")
onkey(letter_t, "t")
onkey(letter_u, "u")
onkey(letter_v, "v") 
onkey(letter_w, "w")
onkey(letter_x, "x")
onkey(letter_y, "y")
onkey(letter_z, "z")
onkey(space_button, "space")
"""
