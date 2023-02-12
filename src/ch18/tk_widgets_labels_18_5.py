import tkinter as tk

# window = tk.Tk()
# message = tk.Label(
#     text="Hello, Tkinter",
#     foreground="white",
#     background="black")
# message.pack()
# window.mainloop()

window = tk.Tk()
message = tk.Label(
    text="Hello, Tkinter",
    bg="#34A2FE")  # use fg and bg as shorthand for foreground / background
message.pack()

window.mainloop()

window = tk.Tk()
message = tk.Label(
    text="Hello, Tkinter",
    fg="#cfc5b9",
    bg="#225e7d",
    width=10,
    height=10
)
message.pack()

window.mainloop()
