import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

fields = [
    "First Name: ", "Last Name: ",
    "Address Line 1: ", "Address Line 2: ",
    "City: ", "State/Province: ",
    "Postal Code: ", "Country: "
]

field_frame = tk.Frame(
    master=window,
    relief=tk.SUNKEN,
    borderwidth=5
)
field_frame.columnconfigure(1, minsize=300)

for i in range(len(fields)):
    lbl = tk.Label(master=field_frame, text=fields[i])
    lbl.grid(row=i, column=0, sticky="E")
    ent = tk.Entry(master=field_frame)
    ent.grid(row=i, column=1, sticky="EW")

field_frame.grid(row=0, column=0)

btn_frame = tk.Frame(
    master=window,
    relief=tk.FLAT,
    borderwidth=2
)
btn_frame.grid(row=1)

btn_submit = tk.Button(master=btn_frame, text="Submit", padx=10)
btn_submit.pack(side=tk.RIGHT, padx=5, pady=5)

btn_clear = tk.Button(master=btn_frame, text="Clear", padx=10)
btn_clear.pack(side=tk.RIGHT, padx=5, pady=5)

btn_frame.grid(row=1, column=0, sticky="E")

window.mainloop()
