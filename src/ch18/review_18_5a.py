import tkinter as tk

window = tk.Tk()

# page 571
reliefs = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE
}
frm = tk.Frame()
for relief_name, relief in reliefs.items():
    btn = tk.Button(master=frm, text=relief_name, relief=relief)
    btn.pack(side="left")
frm.pack()

# page 568
# frm_a = tk.Frame()
# frm_b = tk.Frame()
# # frm_a.pack()
# frm_b.pack()
# frm_a.pack()
# lbl_a = tk.Label(master=frm_a, text="I'm in Frame A")
# lbl_b = tk.Label(master=frm_b, text="I'm in Frame B")
# lbl_a.pack()
# lbl_b.pack()

# page 567
# frm = tk.Frame()
# frm.pack()

# page 559
# txt = tk.Text()
# txt.pack()
# txt.insert("1.0", "Hello")
# txt.insert("2.0", "\nWorld")
# txt.delete("1.0")
# txt.delete("1.0", "1.4")
# txt.delete("1.0")
# txt.delete("1.0", tk.END)
# txt.insert("1.0", "Hello")
# # txt.insert("2.0", "World")
# txt.insert("2.0", "\nWorld")

# page 554
# lbl = tk.Label(text="Name")
# ent = tk.Entry()
# lbl.pack()
# ent.pack()
# ent.insert("0", "Real Python")

# page 552
# btn = tk.Button(
#     text="Click me!",
#     bg="blue",
#     fg="yellow",
#     width=25,
#     height=10
# )
# btn.pack()

# page 551
# label = tk.Label(text="Hello, Tkinter", bg="black", fg="white", width=10, height=10)
# label.pack()

window.mainloop()
