from turtle import*
import tkinter as tk
import ctypes
from tkinter.simpledialog import askstring


x = -300
y = 300
length = 0
root = tk.Tk()
name = askstring("askstring", "Enter some Text")

print(name)

index = 0
stack = []

while index < len(name):
   letter = name[index]
   num = ord(letter)
   stack.append(num)
   index += 1

pensize(10)   
bgcolor("black")
speed(100)

def space():
    penup()
    lt(45)
    fd(24)
    pendown()
def position():
    penup()
    goto(x,y)
    pendown()
def finish():
    begin_fill()
    circle(10, steps = 4)
    end_fill()
    space()
def newPos():
    penup()
    goto(x,y-100)
    pendown()
def space_button():
    color("black")
    rt(45)
    fillcolor("black")
    finish()
def letter_q():
    color("#A4C639")
    rt(45)
    fillcolor("#A4C639")
    finish()
def letter_w():
    color("#F0F8FF")
    rt(45)
    fillcolor("#F0F8FF")
    finish()
def letter_e():
    color("#FFC1CC")
    rt(45)
    fillcolor("#FFC1CC")
    finish()
def letter_r():
    color("#E9967A")
    rt(45)
    fillcolor("#E9967A")
    finish()
def letter_t():
    color("salmon")
    rt(45)
    fillcolor("salmon")
    finish()
def letter_y():
    color("darkslateblue")
    rt(45)
    fillcolor("darkslateblue")
    finish()
def letter_u():
    color("thistle")
    rt(45)
    fillcolor("thistle")
    finish()
def letter_i():
    color("#79443B")
    rt(45)
    fillcolor("#79443B")
    finish()
def letter_o():
    color("cornflowerblue")
    rt(45)
    fillcolor("cornflowerblue")
    finish()
def letter_p():
    color("greenyellow")
    rt(45)
    fillcolor("greenyellow")
    finish()
def letter_a():
    color("dimgray")
    rt(45)
    fillcolor("dimgray")
    finish()
def letter_s():
    color("darkgreen")
    rt(45)
    fillcolor("darkgreen")
    finish()
def letter_d():
    color("darkred")
    rt(45)
    fillcolor("darkred")
    finish()
def letter_f():
    color("red")
    rt(45)
    fillcolor("red")
    finish()
def letter_g():
    color("peachpuff")
    rt(45)
    fillcolor("peachpuff")
    finish()
def letter_h(): 
    color("#7FFFD4")
    rt(45)
    fillcolor("#7FFFD4")
    finish()
def letter_j():
    color("blue")
    rt(45)
    fillcolor("blue")
    finish()
def letter_k():
    color("orange")
    rt(45)
    fillcolor("orange")
    finish()
def letter_l():
    color("DarkCyan")
    rt(45)
    fillcolor("DarkCyan")
    finish()
def letter_m():
    color("DarkViolet")
    rt(45)
    fillcolor("DarkViolet")
    finish()
def letter_n():
    color("gold")
    rt(45)
    fillcolor("gold")
    finish()
def letter_b():
    color("LightBlue")
    rt(45)
    fillcolor("LightBlue")
    finish()
def letter_v():
    color("navy")
    rt(45)
    fillcolor("navy")
    finish()
def letter_c():
    color("sienna")
    rt(45)
    fillcolor("sienna")
    finish()
def letter_x():
    color("tan")
    rt(45)
    fillcolor("tan")
    finish()
def letter_z():
    color("pink")
    rt(45)
    fillcolor("pink")
    finish()
def num_1():
    color("#5d7865")
    rt(45)
    fillcolor("#5d7865")
    finish()
def num_2():
    color("#efda07")
    rt(45)
    fillcolor("#efda07")
    finish()
def num_3():
    color("#833337")
    rt(45)
    fillcolor("#833337")
    finish()
def num_4():
    color("#a040c6")
    rt(45)
    fillcolor("#a040c6")
    finish()
def num_5():
    color("#758b44")
    rt(45)
    fillcolor("#758b44")
    finish()
def num_6():
    color("#79593f")
    rt(45)
    fillcolor("#79593f")
    finish()
def num_7():
    color("#68b06d")
    rt(45)
    fillcolor("#68b06d")
    finish()
def num_8():
    color("#cdf1e3")
    rt(45)
    fillcolor("#cdf1e3")
    finish()
def num_9():
    color("#5511ab")
    rt(45)
    fillcolor("#5511ab")
    finish()
def num_0():
    color("#f36052")
    rt(45)
    fillcolor("#f36052")
    finish()
def spec_tilda():
    color("#4840f9")
    rt(45)
    fillcolor("#4840f9")
    finish()
def spec_accent():
    color("#31b440")
    rt(45)
    fillcolor("#31b440")
    finish()
def spec_exclam():
    color("#8cf390")
    rt(45)
    fillcolor("#8cf390")
    finish()
def spec_at():
    color("#fb452e")
    rt(45)
    fillcolor("#fb452e")
    finish()
def spec_pound():
    color("#741210")
    rt(45)
    fillcolor("#741210")
    finish()
def spec_dollar():
    color("#a833dd")
    rt(45)
    fillcolor("#a833dd")
    finish()
def spec_percent():
    color("#2546fb")
    rt(45)
    fillcolor("#2546fb")
    finish()
def spec_up():
    color("#67b97f")
    rt(45)
    fillcolor("#67b97f")
    finish()
def spec_amp():
    color("#a10c0f")
    rt(45)
    fillcolor("#a10c0f")
    finish()
def spec_star():
    color("#dbdb6a")
    rt(45)
    fillcolor("#dbdb6a")
    finish()
def spec_openp():
    color("#f3899e")
    rt(45)
    fillcolor("#f3899e")
    finish()
def spec_closep():
    color("#9bcaff")
    rt(45)
    fillcolor("#9bcaff")
    finish()
def spec_minus():
    color("#0ea933")
    rt(45)
    fillcolor("#0ea933")
    finish()
def spec_underscore():
    color("#e72656")
    rt(45)
    fillcolor("#e72656")
    finish()
def spec_plus():
    color("#9edc59")
    rt(45)
    fillcolor("#9edc59")
    finish()
def spec_equal():
    color("#71412d")
    rt(45)
    fillcolor("#71412d")
    finish()
def spec_openb():
    color("#c050a5")
    rt(45)
    fillcolor("#c050a5")
    finish()
def spec_openc():
    color("#3cf700")
    rt(45)
    fillcolor("#3cf700")
    finish()
def spec_closeb():
    color("#9b1dfa")
    rt(45)
    fillcolor("#9b1dfa")
    finish()
def spec_closec():
    color("#d80bce")
    rt(45)
    fillcolor("#d80bce")
    finish()
def spec_line():
    color("#a6dcd2")
    rt(45)
    fillcolor("#a6dcd2")
    finish()
def spec_backslash():
    color("#f29ea7")
    rt(45)
    fillcolor("#f29ea7")
    finish()
def spec_colon():
    color("#5c46dd")
    rt(45)
    fillcolor("#5c46dd")
    finish()
def spec_semicolon():
    color("#6f978d")
    rt(45)
    fillcolor("#6f978d")
    finish()
def spec_quote():
    color("#c725f6")
    rt(45)
    fillcolor("#c725f6")
    finish()
def spec_apos():
    color("#ba9208")
    rt(45)
    fillcolor("#ba9208")
    finish()
def spec_opencar():
    color("#1da7e0")
    rt(45)
    fillcolor("#1da7e0")
    finish()
def spec_comma():
    color("#e9da83")
    rt(45)
    fillcolor("#e9da83")
    finish()
def spec_closecar():
    color("#b6582f")
    rt(45)
    fillcolor("#b6582f")
    finish()
def spec_period():
    color("#0a99ab")
    rt(45)
    fillcolor("#0a99ab")
    finish()
def spec_question():
    color("#dda6ce")
    rt(45)
    fillcolor("#dda6ce")
    finish()
def spec_fslash():
    color("#88e089")
    rt(45)
    fillcolor("#88e089")
    finish()

listen()
position()

for x in range (0, len(stack)):
   count = 0
   if (stack[x] == 97 or stack[x] == 65): 
        letter_a()
        count += 1
   if (stack[x] == 98 or stack[x] == 66):
        letter_b()
   if (stack[x] == 99 or stack[x] == 67):
        letter_c()
   if (stack[x] == 100 or stack[x] == 68):
        letter_d()
   if (stack[x] == 101 or stack[x] == 69):
        letter_e()
   if (stack[x] == 102 or stack[x] == 70):
        letter_f()
   if (stack[x] == 103 or stack[x] == 71):
        letter_g()
   if (stack[x] == 104 or stack[x] == 72):
        letter_h()
   if (stack[x] == 105 or stack[x] == 73):
        letter_i()
   if (stack[x] == 106 or stack[x] == 74):
        letter_j()
   if (stack[x] == 107 or stack[x] == 75):
        letter_k()
   if (stack[x] == 108 or stack[x] == 76):
        letter_l()
   if (stack[x] == 109 or stack[x] == 77):
        letter_m()
   if (stack[x] == 110 or stack[x] == 78):
        letter_n()
   if (stack[x] == 111 or stack[x] == 79):
        letter_o()
   if (stack[x] == 112 or stack[x] == 80):
        letter_p()
   if (stack[x] == 113 or stack[x] == 81):
        letter_q()
   if (stack[x] == 114 or stack[x] == 82):
        letter_r()
   if (stack[x] == 115 or stack[x] == 83):
        letter_s()
   if (stack[x] == 116 or stack[x] == 84):
        letter_t()
   if (stack[x] == 117 or stack[x] == 85):
        letter_u()
   if (stack[x] == 118 or stack[x] == 86):
        letter_v()
   if (stack[x] == 119 or stack[x] == 87):
        letter_w()
   if (stack[x] == 120 or stack[x] == 88):
        letter_x()
   if (stack[x] == 121 or stack[x] == 89):
        letter_y()
   if (stack[x] == 122 or stack[x] == 90):
        letter_z()

#NUMBERS
   if (stack[x] == 48):
        num_0()
   if (stack[x] == 49):
        num_1()
   if (stack[x] == 50):
        num_2()
   if (stack[x] == 51):
        num_3()
   if (stack[x] == 52):
        num_4()
   if (stack[x] == 53):
        num_5()
   if (stack[x] == 54):
        num_6()
   if (stack[x] == 55):
        num_7()
   if (stack[x] == 56):
        num_8()
   if (stack[x] == 57):
        num_9()
        
#SPECIAL CHARACTERS
   if (stack[x] == 126):
        spec_tilda()
   if (stack[x] == 96):
        spec_accent()
   if (stack[x] == 33):
        spec_exclam()
   if (stack[x] == 64):
        spec_at()
   if (stack[x] == 35):
        spec_pound()
   if (stack[x] == 36):
        spec_dollar()
   if (stack[x] == 37):
        spec_percent()
   if (stack[x] == 94):
        spec_up()
   if (stack[x] == 38):
        spec_amp()
   if (stack[x] == 42):
        spec_star()
   if (stack[x] == 40):
        spec_openp()
   if (stack[x] == 41):
        spec_closep()
   if (stack[x] == 45):
        spec_minus()
   if (stack[x] == 95):
        spec_underscore()
   if (stack[x] == 43):
        spec_plus()
   if (stack[x] == 61):
        spec_equal()
   if (stack[x] == 91):
        spec_openb()
   if (stack[x] == 123):
        spec_openc()
   if (stack[x] == 93):
        spec_closeb()
   if (stack[x] == 125):
        spec_closec()
   if (stack[x] == 58):
        spec_colon()
   if (stack[x] == 59):
        spec_semicolon()
   if (stack[x] == 34):
        spec_quote()
   if (stack[x] == 39):
        spec_apos()
   if (stack[x] == 60):
        spec_opencar()
   if (stack[x] == 44):
        spec_comma()
   if (stack[x] == 62):
        spec_closecar()
   if (stack[x] == 63):
        spec_question()
   if (stack[x] == 46):
        spec_period()
   if (stack[x] == 47):
        spec_fslash()
   if (stack[x] == 92):
        spec_backslash()
   if (stack[x] == 124):
        spec_line()
