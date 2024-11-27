import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.lower_bound = None
        self.upper_bound = None
        self.max_attempts = None
        self.secret_number = None
        self.attempts = 0

        self.setup_ui()

    def setup_ui(self):
        # Setting up the main frame
        main_frame = tk.Frame(self.root, bg="lightblue", padx=20, pady=20)
        main_frame.pack(padx=10, pady=10)

        title_label = tk.Label(main_frame, text="🎯 Number Guessing Game 🎯", font=("Helvetica", 18, "bold"), bg="lightblue")
        title_label.pack(pady=10)

        # User inputs for game settings
        self.create_input(main_frame, "Enter the lower bound:", "lower_bound")
        self.create_input(main_frame, "Enter the upper bound:", "upper_bound")
        self.create_input(main_frame, "Enter the maximum attempts:", "max_attempts")

        # Start button to initiate the game
        start_button = tk.Button(main_frame, text="Start Game", font=("Helvetica", 12), bg="darkblue", fg="white", command=self.start_game)
        start_button.pack(pady=10)

        # Entry for user guesses
        self.guess_entry = tk.Entry(main_frame, font=("Helvetica", 12), state='disabled')
        self.guess_entry.pack(pady=10)

        # Submit button for guesses
        self.submit_button = tk.Button(main_frame, text="Submit Guess", font=("Helvetica", 12), bg="darkblue", fg="white", state='disabled', command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(main_frame, text="", font=("Helvetica", 14), bg="lightblue")
        self.result_label.pack(pady=10)

    def create_input(self, frame, label_text, var_name):
        label = tk.Label(frame, text=label_text, font=("Helvetica", 12), bg="lightblue")
        label.pack(pady=5)
        entry = tk.Entry(frame, font=("Helvetica", 12))
        entry.pack()
        setattr(self, f"{var_name}_entry", entry)

    def start_game(self):
        try:
            self.lower_bound = int(self.lower_bound_entry.get())
            self.upper_bound = int(self.upper_bound_entry.get())
            self.max_attempts = int(self.max_attempts_entry.get())
            self.secret_number = random.randint(self.lower_bound, self.upper_bound)
            self.attempts = 0
            self.guess_entry.config(state='normal')
            self.submit_button.config(state='normal')
            self.result_label.config(text="Game started! Make your guess.")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for bounds and attempts.")

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1

            if guess < self.lower_bound or guess > self.upper_bound:
                self.result_label.config(text="Invalid input. Please enter a number within the specified range.")
            elif guess == self.secret_number:
                self.result_label.config(text=f"🎉 Congratulations! You guessed the secret number {self.secret_number} in {self.attempts} attempts.")
                self.guess_entry.config(state='disabled')
                self.submit_button.config(state='disabled')
            elif guess < self.secret_number:
                self.result_label.config(text="📉 Too low! Try again.")
            else:
                self.result_label.config(text="📈 Too high! Try again.")

            if self.attempts >= self.max_attempts and guess != self.secret_number:
                self.result_label.config(text=f"☹️ Sorry, you ran out of attempts! The secret number was {self.secret_number}.")
                self.guess_entry.config(state='disabled')
                self.submit_button.config(state='disabled')

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
