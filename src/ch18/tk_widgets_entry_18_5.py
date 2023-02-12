import tkinter as tk

window = tk.Tk()

label = tk.Label(text="Name")
entry = tk.Entry(fg="yellow", bg="blue", width=50)
label.pack()
entry.pack()

# # name = entry.get()
# # name
# # 'Real Python'
# entry.delete(0)
# # 'eal Python'
# entry.delete(0, 4)
# # 'Python'
# entry.delete(0, tk.END)
# # ''

# entry.insert(0, "Python")
# entry.insert(0, "Real ")

window.mainloop()
