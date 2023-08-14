import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import random
import string
import tkinter.messagebox

def generate_password():
    password_length = int(length_entry.get())
    password_characters = ""
    if include_uppercase.get():
        password_characters += string.ascii_uppercase
    if include_symbols.get():
        password_characters += string.punctuation
    password_characters += string.ascii_lowercase
    password = "".join(random.choice(password_characters) for _ in range(password_length))
    generated_password.set(password)
    result_label.config(text="Generated Password: " + password)

def copy_to_clipboard():
    password = generated_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        tkinter.messagebox.showinfo("Copied", "Password copied to clipboard!")


root = tk.Tk()
root.title("Password Generator")
root.geometry('400x450')

style = ThemedStyle(root)
style.set_theme("clam")


frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

title_label = ttk.Label(frame, text="Password Generator", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, columnspan=2, pady=10)

username_label = ttk.Label(frame, text="User Name:")
username_label.grid(row=1, column=0, sticky='w', pady=10)

username_entry = ttk.Entry(frame)
username_entry.grid(row=1, column=1, pady=10)

length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(row=2, column=0, sticky='w', pady=10)

length_entry = ttk.Entry(frame)
length_entry.grid(row=2, column=1, pady=10)

include_uppercase = tk.BooleanVar()
uppercase_checkbox = ttk.Checkbutton(frame, text="Include Uppercase Letters", variable=include_uppercase)
uppercase_checkbox.grid(row=3, columnspan=2, sticky='w', pady=5)

include_symbols = tk.BooleanVar()
symbols_checkbox = ttk.Checkbutton(frame, text="Include Symbols", variable=include_symbols)
symbols_checkbox.grid(row=4, columnspan=2, sticky='w', pady=5)

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=5, columnspan=2, pady=15)

generated_password = tk.StringVar()
result_label = ttk.Label(frame, textvariable=generated_password, font=("Helvetica", 12, "italic"))
result_label.grid(row=6, columnspan=2, pady=15)

copy_button = ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=7, columnspan=2, pady=15)


root.mainloop()