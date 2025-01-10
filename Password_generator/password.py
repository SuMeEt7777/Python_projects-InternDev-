import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4 characters.")
        return

    characters = ""
    if include_uppercase.get():
        characters += string.ascii_uppercase
    if include_lowercase.get():
        characters += string.ascii_lowercase
    if include_digits.get():
        characters += string.digits
    if include_special.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Generated Password: {password}")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text").replace("Generated Password: ", ""))
    root.update()  # Now it stays on the clipboard after the program closes
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Initialize the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Header label
header_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

# Password length selection
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
length_label = tk.Label(length_frame, text="Password Length:")
length_label.pack(side=tk.LEFT, padx=5)
length_entry = tk.Entry(length_frame, width=5)
length_entry.insert(0, "12")
length_entry.pack(side=tk.LEFT)

# Character type options
options_frame = tk.Frame(root)
options_frame.pack(pady=10)

include_uppercase = tk.BooleanVar(value=True)
uppercase_check = tk.Checkbutton(options_frame, text="Include Uppercase", variable=include_uppercase)
uppercase_check.pack(anchor="w")

include_lowercase = tk.BooleanVar(value=True)
lowercase_check = tk.Checkbutton(options_frame, text="Include Lowercase", variable=include_lowercase)
lowercase_check.pack(anchor="w")

include_digits = tk.BooleanVar(value=True)
digits_check = tk.Checkbutton(options_frame, text="Include Digits", variable=include_digits)
digits_check.pack(anchor="w")

include_special = tk.BooleanVar(value=True)
special_check = tk.Checkbutton(options_frame, text="Include Special Characters", variable=include_special)
special_check.pack(anchor="w")

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white", font=("Arial", 12))
generate_button.pack(pady=15)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), wraplength=350, justify="center")
result_label.pack(pady=10)

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="green", fg="white", font=("Arial", 10))
copy_button.pack(pady=5)

# Run the application
root.mainloop()
