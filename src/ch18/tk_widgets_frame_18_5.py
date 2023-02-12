import tkinter as tk

# window = tk.Tk()
#
# frame_a = tk.Frame()
# frame_b = tk.Frame()
#
# label_a = tk.Label(master=frame_a, text="I'm in Frame A")
# label_a.pack()
#
# label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# label_b.pack()
#
# frame_b.pack()  # whichever is packed first will appear first
# frame_a.pack()
#
# window.mainloop()

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    # 1
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    # 2
    frame.pack(side=tk.LEFT)
    # 3
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()
