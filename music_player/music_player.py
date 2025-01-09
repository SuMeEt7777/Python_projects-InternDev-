import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pygame import mixer


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("500x400")

        # Initialize the mixer
        mixer.init()

        # Current track
        self.current_track = None

        # Playlist
        self.playlist = []

        # UI components
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Music Player", font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Playlist Listbox
        self.playlist_listbox = tk.Listbox(self.root, width=50, height=12)
        self.playlist_listbox.pack(pady=10)

        # Add song button
        self.add_button = tk.Button(self.root, text="Add Song", width=20, command=self.add_song)
        self.add_button.pack(pady=5)

        # Control buttons
        self.play_button = tk.Button(self.root, text="Play", width=10, command=self.play_song)
        self.play_button.pack(side=tk.LEFT, padx=20)

        self.pause_button = tk.Button(self.root, text="Pause", width=10, command=self.pause_song)
        self.pause_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(self.root, text="Stop", width=10, command=self.stop_song)
        self.stop_button.pack(side=tk.LEFT, padx=20)

        self.resume_button = tk.Button(self.root, text="Resume", width=10, command=self.resume_song)
        self.resume_button.pack(side=tk.LEFT, padx=20)

        # Exit button
        self.exit_button = tk.Button(self.root, text="Exit", width=20, command=self.exit_player)
        self.exit_button.pack(pady=10)

    def add_song(self):
        file_path = filedialog.askopenfilename(
            title="Select a Song",
            filetypes=(("MP3 Files", "*.mp3"), ("All Files", "*.*"))
        )
        if file_path:
            self.playlist.append(file_path)
            self.playlist_listbox.insert(tk.END, os.path.basename(file_path))

    def play_song(self):
        selected_index = self.playlist_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a song to play.")
            return

        self.current_track = self.playlist[selected_index[0]]
        mixer.music.load(self.current_track)
        mixer.music.play()
        self.root.title(f"Now Playing: {os.path.basename(self.current_track)}")

    def pause_song(self):
        if mixer.music.get_busy():
            mixer.music.pause()

    def stop_song(self):
        mixer.music.stop()

    def resume_song(self):
        if not mixer.music.get_busy():
            mixer.music.unpause()

    def exit_player(self):
        mixer.music.stop()
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
