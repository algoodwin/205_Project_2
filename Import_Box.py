from tkinter import Tk
#import tkinter.messagebox
from tkinter.simpledialog import askstring

root = Tk()
string = askstring("askstring", "Enter Text")

print(string)
