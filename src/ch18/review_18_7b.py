"""Write a program that simulates rolling a six-sided die.
There should be one button with the text "Roll".
When the user clicks the button, a random integer from 1 to 6 should be displayed."""
import tkinter as tk
import random

def die_roll():
    lbl["text"] = str(random.randint(1, 6))


window = tk.Tk()
window.title("Six-Sided Die")

window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

btn = tk.Button(master=window, text="Roll", command=die_roll)
btn.grid(row=0, column=0, sticky="nsew")

lbl = tk.Label(master=window)
lbl.grid(row=1, column=0, sticky="nsew")

window.mainloop()
