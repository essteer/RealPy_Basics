"""Write a program that displays a single button with the default background color
and black text that reads 'Click me'. When the user clicks the button,
the button background should change to a color randomly selected from the following list:
["red", "orange", "yellow", "blue", "green", "indigo", "violet"]"""
import tkinter as tk
import random

colours = ["red", "orange", "yellow", "blue", "green", "indigo", "violet"]

def change_colour():
    btn["bg"] = random.choice(colours)


window = tk.Tk()
window.title("Random Colour Button")

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

btn = tk.Button(master=window, text="Click me", command=change_colour)
btn.grid(row=0, column=0, sticky="nsew")

window.mainloop()
