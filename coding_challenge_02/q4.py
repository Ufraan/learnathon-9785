#Python Program to Convert Decimal to Binary, Octal and Hexadecimal

#made custom window using tkinter and ttk modules for better look and flexibility

import tkinter as tk
from tkinter import ttk

BACKGROUND_COLOR = "#222222"
FOREGROUND_COLOR = "#FFFFFF"
BUTTON_COLOR = "#444444"
FONT = "Helvetica"

def convert():
    decimal_value = 0
    from_base = from_var.get()
    to_base = to_var.get()
    
    try:
        if from_base == "Decimal":
            decimal_value = int(entry_decimal.get())
        elif from_base == "Binary":
            decimal_value = int(entry_decimal.get(), 2)
        elif from_base == "Octal":
            decimal_value = int(entry_decimal.get(), 8)
        elif from_base == "Hexadecimal":
            decimal_value = int(entry_decimal.get(), 16)
    except ValueError:
        label_result.config(text="Invalid input", fg="red")
        return
    
    if to_base == "Decimal":
        result = str(decimal_value)
    elif to_base == "Binary":
        result = bin(decimal_value)
    elif to_base == "Octal":
        result = oct(decimal_value)
    elif to_base == "Hexadecimal":
        result = hex(decimal_value)
    
    label_result.config(text=f"Result: {result}", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, font=(FONT, 12))

root = tk.Tk()
root.title("Number Converter")
root.configure(bg=BACKGROUND_COLOR)

style = ttk.Style()
style.theme_use('clam')  
style.configure('TCombobox', fieldbackground=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR, background=BACKGROUND_COLOR, font=(FONT, 12))
style.map('TCombobox', fieldbackground=[('readonly', BACKGROUND_COLOR)])

heading_label = tk.Label(root, text="Number Converter", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, font=(FONT, 16, "bold"))
heading_label.pack(pady=10)

# Create and place widgets
label_decimal = tk.Label(root, text="Enter a Number:", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, font=(FONT, 12))
label_decimal.pack()

entry_decimal = tk.Entry(root, bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font=(FONT, 12))
entry_decimal.pack()

from_label = tk.Label(root, text="Convert from:", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, font=(FONT, 12))
from_label.pack()

from_var = tk.StringVar(root)
from_dropdown = ttk.Combobox(root, textvariable=from_var, values=["Decimal", "Binary", "Octal", "Hexadecimal"], state="readonly", font=(FONT, 12))
from_dropdown.current(0)
from_dropdown.pack()

to_label = tk.Label(root, text="Convert to:", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, font=(FONT, 12))
to_label.pack()

to_var = tk.StringVar(root)
to_dropdown = ttk.Combobox(root, textvariable=to_var, values=["Decimal", "Binary", "Octal", "Hexadecimal"], state="readonly", font=(FONT, 12))
to_dropdown.current(0)
to_dropdown.pack()

convert_button = tk.Button(root, text="Convert", command=convert, bg=BUTTON_COLOR, fg=FOREGROUND_COLOR, font=(FONT, 12))
convert_button.pack(pady=10)

label_result = tk.Label(root, text="", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, font=(FONT, 12))
label_result.pack()

root.mainloop()
