import tkinter as tk
import cv2
import threading
import pygame

# Initialize pygame mixer for audio
pygame.mixer.init()

# Function to play video using OpenCV and audio using pygame
def play_video(file_path, audio_path, wait_time):
    # Start audio playback
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    # OpenCV for video playback
    cap = cv2.VideoCapture(file_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Akala mo...", frame)
        if cv2.waitKey(wait_time) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    pygame.mixer.music.stop()  # Stop the audio when the video ends

# Functions triggered by button clicks
def tralalero():
    threading.Thread(target=play_video, args=("tralalero.mp4", "tralalero.mp3", 36), daemon=True).start()

def capuchino():
    threading.Thread(target=play_video, args=("capuchino.mp4", "capuchino.mp3", 12), daemon=True).start()

# GUI Window
root = tk.Tk()
root.title("Filipino Brainrot")
root.geometry("500x300")
root.configure(bg="black")

# Welcome Label
label = tk.Label(root, text="Welcome to Filipino Brainrot", font=("Arial", 20), fg="white", bg="black")
label.pack(pady=30)

# Author Label
author_label = tk.Label(root, text="by Matthewmatician", font=("Arial", 14), fg="white", bg="black")
author_label.pack(pady=(0, 20))

# Buttons
button1 = tk.Button(root, text="tralalero tralala", command=tralalero, width=25, height=2, bg="#ffcc00")
button1.pack(pady=10)

button2 = tk.Button(root, text="Capuchino Assassino", command=capuchino, width=25, height=2, bg="#00ccff")
button2.pack(pady=10)

# Start GUI loop
root.mainloop()
