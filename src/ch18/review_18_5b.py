import tkinter as tk

# 2
window = tk.Tk()
btn = tk.Button(
    text="Click here",
    width=50,
    height=25,
    bg="white",
    fg="blue"
)
btn.pack()
window.mainloop()

# 3
window = tk.Tk()
ent = tk.Entry(fg="black", bg="white", width=40)
ent.pack()
ent.insert(0, "What is your name?")
window.mainloop()
