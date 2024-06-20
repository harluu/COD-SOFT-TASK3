import tkinter as tk
from tkinter import messagebox
import random
import stringimport tkinter as tk

def add_to_display(value):
    current = display_var.get()
    if current == "Error":
        display_var.set("")
    display_var.set(current + value)

def clear_display():
    display_var.set("")

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="pink")

display_var = tk.StringVar(root, "")

display = tk.Entry(root, textvariable=display_var, font=("Helvetica", 24), justify="right", bg="white")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0

for text in button_texts:
    if text == 'C':
        tk.Button(root, text=text, font=("Helvetica", 16), bg="gray", command=clear_display).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == '=':
        tk.Button(root, text=text, font=("Helvetica", 16), bg="gray", command=calculate).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(root, text=text, font=("Helvetica", 16), bg="gray", command=lambda t=text: add_to_display(t)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()


def generate_password():
    length = length_entry.get()
    
    if not length.isdigit():
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return
    
    length = int(length)
    
    if length <= 0:
        messagebox.showerror("Error", "Please enter a positive number for length.")
        return
    
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    
    if not is_strong_password(password):
        messagebox.showwarning("Warning", "Generated password may not be strong. Consider increasing length.")
    
    password_display.config(state="normal")
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, password)
    password_display.config(state="disabled")

def is_strong_password(password):
    # You can define your own criteria for a strong password here
    # For simplicity, we'll just check if the length is at least 8 characters
    return len(password) >= 8

def reset_password():
    length_entry.delete(0, tk.END)
    password_display.config(state="normal")
    password_display.delete(1.0, tk.END)
    password_display.config(state="disabled")

root = tk.Tk()
root.title("Password Generator")

# Colorful Background
background_color = "blue"  
root.configure(background=background_color)

username_label = tk.Label(root, text="Username:", bg=background_color)
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

length_label = tk.Label(root, text="Password Length:", bg=background_color)
length_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="red", fg="black")
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")

reset_button = tk.Button(root, text="Reset", command=reset_password, bg="yellow", fg="black")
reset_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

password_display_label = tk.Label(root, text="Generated Password:", bg=background_color)
password_display_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

password_display = tk.Text(root, height=1, width=30, state="disabled")
password_display.grid(row=4, column=1, padx=10, pady=5, sticky="we")

root.mainloop()
