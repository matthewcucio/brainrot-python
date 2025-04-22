import tkinter as tk
from tkinter import messagebox
import cv2
import threading

# Function to play video using OpenCV
def play_video(file_path):
    cap = cv2.VideoCapture(file_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Functions triggered by button clicks
def tralalero():
    threading.Thread(target=play_video, args=("tralalero.mp4",), daemon=True).start()

def capuchino():
    threading.Thread(target=play_video, args=("capuchino.mp4",), daemon=True).start()

# GUI Window
root = tk.Tk()
root.title("Filipino Brainrot")
root.geometry("500x300")
root.configure(bg="black")

# Welcome Label
label = tk.Label(root, text="Welcome to Filipino brainrot", font=("Arial", 20), fg="white", bg="black")
label.pack(pady=30)

# Buttons
button1 = tk.Button(root, text="tralalero tralala (left)", command=tralalero, width=25, height=2, bg="#ffcc00")
button1.pack(pady=10)

button2 = tk.Button(root, text="Capuchino Assassino (right)", command=capuchino, width=25, height=2, bg="#00ccff")
button2.pack(pady=10)

# Start GUI loop
root.mainloop()
