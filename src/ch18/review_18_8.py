import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value from Fahrenheit to Celsius
    and insert the result into lbl_result"""
    fahrenheit = ent_fahrenheit.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_celsius_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

def celsius_to_fahrenheit():
    """Convert the value from Celsius to Fahrenheit
    and insert the result into lbl_result"""
    celsius = ent_celsius.get()
    fahrenheit = (float(celsius) / (5/9)) + 32
    lbl_fahrenheit_result["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"


window = tk.Tk()
window.title("Temperature Converter")

frm_fahrenheit = tk.Frame(master=window)
ent_fahrenheit = tk.Entry(master=frm_fahrenheit, width=10)
lbl_fahrenheit = tk.Label(master=frm_fahrenheit, text="\N{DEGREE FAHRENHEIT}")

ent_fahrenheit.grid(row=0, column=0, sticky="e")
lbl_fahrenheit.grid(row=0, column=1, sticky="w")

btn_fahrenheit_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius)
lbl_celsius_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}", width=10)

frm_fahrenheit.grid(row=0, column=0, padx=10, pady=3)
btn_fahrenheit_convert.grid(row=0, column=1, padx=10, pady=3)
lbl_celsius_result.grid(row=0, column=2, padx=10, pady=3)

frm_celsius = tk.Frame(master=window)
ent_celsius = tk.Entry(master=frm_celsius, width=10)
lbl_celsius = tk.Label(master=frm_celsius, text="\N{DEGREE CELSIUS}")

ent_celsius.grid(row=0, column=0, sticky="e")
lbl_celsius.grid(row=0, column=1, sticky="w")

btn_celsius_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=celsius_to_fahrenheit)
lbl_fahrenheit_result = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}", width=10)

frm_celsius.grid(row=1, column=0, padx=10, pady=3)
btn_celsius_convert.grid(row=1, column=1, padx=10, pady=3)
lbl_fahrenheit_result.grid(row=1, column=2, padx=10, pady=3)

window.mainloop()
