import tkinter as tk
from tkinter import messagebox
import time
import random

class TypingTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("800x400")

        # Sample texts for testing
        self.sample_texts = [
            "The quick brown fox jumps over the lazy dog.",
            "Python is an amazing programming language for beginners and experts alike.",
            "Typing fast and accurately is an essential skill in today's digital world.",
            "Practice makes perfect when it comes to improving your typing speed.",
        ]

        # Variables
        self.selected_text = random.choice(self.sample_texts)
        self.start_time = None

        # Create UI
        self.create_widgets()

    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Typing Speed Tester", font=("Arial", 24))
        self.title_label.pack(pady=10)

        # Display sample text
        self.sample_label = tk.Label(
            self.root, text=self.selected_text, font=("Arial", 14), wraplength=750, justify="center"
        )
        self.sample_label.pack(pady=20)

        # Input text box
        self.text_entry = tk.Text(self.root, height=5, width=80, font=("Arial", 12))
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<KeyPress>", self.start_typing)

        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.calculate_results)
        self.submit_button.pack(pady=10)

        # Results display
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def start_typing(self, event):
        """Start the timer on the first key press."""
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_results(self):
        """Calculate and display typing speed and accuracy."""
        if self.start_time is None:
            messagebox.showerror("Error", "Please start typing to begin the test!")
            return

        end_time = time.time()
        total_time = end_time - self.start_time

        # Get the user's input text
        user_text = self.text_entry.get("1.0", tk.END).strip()

        # Calculate Words Per Minute (WPM)
        word_count = len(user_text.split())
        wpm = round((word_count / total_time) * 60, 2)

        # Calculate accuracy
        correct_chars = sum(1 for a, b in zip(user_text, self.selected_text) if a == b)
        accuracy = round((correct_chars / len(self.selected_text)) * 100, 2)

        # Display results
        self.result_label.config(
            text=f"Typing Speed: {wpm} WPM\nAccuracy: {accuracy}%"
        )

        # Disable further typing
        self.text_entry.config(state=tk.DISABLED)

    def reset_test(self):
        """Reset the test with a new random text."""
        self.selected_text = random.choice(self.sample_texts)
        self.sample_label.config(text=self.selected_text)
        self.text_entry.delete("1.0", tk.END)
        self.text_entry.config(state=tk.NORMAL)
        self.result_label.config(text="")
        self.start_time = None


if __name__ == "__main__":
    root = tk.Tk()
    typing_tester = TypingTester(root)

    # Add a reset button
    reset_button = tk.Button(root, text="Reset", command=typing_tester.reset_test)
    reset_button.pack(pady=10)

    root.mainloop()
