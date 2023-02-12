"""Three basic elements:
1) an Entry widget called ent_temperature to enter the Fahrenheit value.
2) a Label widget called lbl_result to display the Celsius result.
3) a Button widget called btn_convert that reads the value from the Entry Widget,
converts it from Fahrenheit to Celsius,
and sets the text of the Label widget to the result when clicked."""
import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value from Fahrenheit to Celsius
    and insert the result into lbl_result"""
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


# Set up the window
window = tk.Tk()
window.title("Temperature Converter")

# Create the Fahrenheit entry frame with an Entry widget and Label
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Lay out the temperature Entry and Label in frm_entry using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Set up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, padx=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()
