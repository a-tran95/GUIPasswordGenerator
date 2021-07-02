import tkinter as tk
from tkinter import *
import random

letterbank_lower = 'abcdefghijklmnopqrstuvwxyz'
letterbank_upper = letterbank_lower.upper()
numberbank = '1234567890'
symbolbank = '!@#$%^&*()-=_+`~{}|[];:<>,./?'

def passgen(is_lower,is_upper,is_num,is_sym,length):

    # Character bank containing all available characters
    thebank = [letterbank_lower,letterbank_upper,numberbank,symbolbank]

    # Characters that have not been checked are removed from the character bank
    if is_lower == False:
        thebank.remove(letterbank_lower)
    if is_upper == False:
        thebank.remove(letterbank_upper)
    if is_num == False:
        thebank.remove(numberbank)
    if is_sym == False:
        thebank.remove(symbolbank)
    if len(thebank) == 0:
        text_box.delete('1.0', END)
        text_box.insert(INSERT, "ERROR: NO CHARACTERS AVAILABLE")
        return()

    # Randomly generates a password according to constraints
    password_arr = [random.choice(random.choice(thebank)) for p in range(0,int(length))]
    password_str = "".join(password_arr)
    text_box.delete('1.0',END)
    text_box.insert(INSERT, password_str)

# Creating new window
window = tk.Tk()
window.title("Password Generator")

# Establishing variables to check characters and length
is_lower = IntVar()
is_upper = IntVar()
is_num = IntVar()
is_sym = IntVar()
length_options = list(range(1,26))
length = tk.StringVar()
length.set(length_options[0])

# Establishing Widgets
tk.Checkbutton(window, text = "Lower Case Letters", variable = is_lower).grid(row= 0, sticky = W)
tk.Checkbutton(window, text = "Upper Case Letters", variable = is_upper).grid(row= 1, sticky = W)
tk.Checkbutton(window, text = "Numbers", variable = is_num).grid(row= 2, sticky = W)
tk.Checkbutton(window, text = "Symbols", variable = is_sym).grid(row= 3, sticky = W)
tk.Label(window, text= "Length").grid(row = 4, sticky = W)
tk.OptionMenu(window, length, *length_options).grid(row = 4, sticky = E)
text_box = tk.Text(window, width = 30, height = 1)
text_box.grid(row = 6)
genbutton = tk.Button(window, text="Generate!", command = lambda: passgen(is_lower.get(),is_upper.get(),is_num.get(),is_sym.get(),length.get()))
genbutton.grid(row = 5)

window.mainloop()