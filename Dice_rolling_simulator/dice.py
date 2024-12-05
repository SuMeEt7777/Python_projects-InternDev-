import tkinter as tk
from tkinter import font
import random
import time

# Dice faces as Unicode characters
DICE_FACES = {
    1: "\u2680",  # ⚀
    2: "\u2681",  # ⚁
    3: "\u2682",  # ⚂
    4: "\u2683",  # ⚃
    5: "\u2684",  # ⚄
    6: "\u2685",  # ⚅
}

def roll_dice():
    """Simulate rolling the dice with an animation."""
    result_label.config(text="Rolling...", font=("Helvetica", 20, "italic"), fg="gray")
    number_label.config(text="")
    window.update()

    # Simulate a rolling effect
    for _ in range(10):
        face = random.choice(list(DICE_FACES.values()))
        result_label.config(text=face)
        window.update()
        time.sleep(0.1)

    # Get the final result
    dice_number = random.randint(1, 6)
    result_label.config(text=DICE_FACES[dice_number], font=("Helvetica", 100), fg="black")
    number_label.config(text=f"You rolled a {dice_number}!", fg="green")

def on_hover(button, color):
    """Change button color on hover."""
    button["bg"] = color

def on_leave(button, color):
    """Restore button color when mouse leaves."""
    button["bg"] = color

# Create the main window
window = tk.Tk()
window.title("Dice Rolling Simulator")
window.geometry("500x500")
window.configure(bg="lightblue")

# Custom fonts
title_font = font.Font(family="Helvetica", size=20, weight="bold")
button_font = font.Font(family="Helvetica", size=14)

# Add a title label
title_label = tk.Label(
    window, 
    text="🎲 Dice Rolling Simulator 🎲", 
    font=title_font, 
    bg="lightblue", 
    fg="darkblue"
)
title_label.pack(pady=20)

# Display the dice face
result_label = tk.Label(
    window, 
    text=DICE_FACES[1], 
    font=("Helvetica", 100), 
    bg="lightblue"
)
result_label.pack(pady=20)

# Display the rolled number
number_label = tk.Label(
    window, 
    text="You rolled a 1!", 
    font=("Helvetica", 16), 
    bg="lightblue", 
    fg="green"
)
number_label.pack(pady=10)

# Add a Roll Dice button with hover effects
roll_button = tk.Button(
    window, 
    text="Roll the Dice", 
    font=button_font, 
    bg="white", 
    fg="black", 
    activebackground="lightgreen", 
    command=roll_dice
)
roll_button.pack(pady=20)
roll_button.bind("<Enter>", lambda e: on_hover(roll_button, "lightgreen"))
roll_button.bind("<Leave>", lambda e: on_leave(roll_button, "white"))

# Add a Quit button with hover effects
quit_button = tk.Button(
    window, 
    text="Quit", 
    font=button_font, 
    bg="red", 
    fg="white", 
    activebackground="darkred", 
    command=window.quit
)
quit_button.pack(pady=10)
quit_button.bind("<Enter>", lambda e: on_hover(quit_button, "darkred"))
quit_button.bind("<Leave>", lambda e: on_leave(quit_button, "red"))

# Responsive layout adjustments
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# Start the tkinter event loop
window.mainloop()
