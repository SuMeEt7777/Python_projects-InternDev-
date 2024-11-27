import datetime
import time
import tkinter as tk
from tkinter import messagebox
import threading
import pygame
import os


def play_sound(sound_file):
    """
    Play the alarm sound using pygame asynchronously.
    """
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()  # Play the sound in the background
    except pygame.error as e:
        messagebox.showerror("Sound Error", f"Could not play sound: {e}")


def check_alarm(alarm_time, sound_file):
    """
    Continuously checks the current time against the alarm time.
    """
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            messagebox.showinfo("Alarm", "Wake up! It's time!")
            play_sound(sound_file)  # Play sound without blocking
            break
        time.sleep(1)


def set_alarm():
    """
    Sets the alarm based on user input from the GUI.
    """
    alarm_time = alarm_time_entry.get()
    sound_file = "alarm/alarm.mp3"  # Relative path to the sound file

    # Ensure the sound file exists
    if not os.path.exists(sound_file):
        messagebox.showerror("File Error", f"Sound file not found: {sound_file}")
        return

    if not alarm_time:
        messagebox.showerror("Input Error", "Please enter a valid alarm time.")
        return

    # Validate time format
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        messagebox.showerror("Format Error", "Time must be in HH:MM:SS format.")
        return

    # Inform user that the alarm is set
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}.")
    
    # Start a new thread to check the alarm
    alarm_thread = threading.Thread(target=check_alarm, args=(alarm_time, sound_file))
    alarm_thread.daemon = True  # Ensure thread exits when the main program exits
    alarm_thread.start()


# Create the main application window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x300")
root.configure(bg="#f0f8ff")

# UI Elements
title_label = tk.Label(root, text="Alarm Clock", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#000080")
title_label.pack(pady=10)

time_label = tk.Label(root, text="Enter Alarm Time (HH:MM:SS):", font=("Helvetica", 12), bg="#f0f8ff")
time_label.pack(pady=5)

alarm_time_entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
alarm_time_entry.pack(pady=5)

set_alarm_button = tk.Button(root, text="Set Alarm", font=("Helvetica", 12), bg="#000080", fg="#ffffff", command=set_alarm)
set_alarm_button.pack(pady=20)

credits_label = tk.Label(root, text="Created by You", font=("Helvetica", 10), bg="#f0f8ff", fg="#808080")
credits_label.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
