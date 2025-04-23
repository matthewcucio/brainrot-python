import tkinter as tk
from tkinter import Canvas
import cv2
import threading
import pygame

# Initialize pygame mixer for audio
pygame.mixer.init()

def play_video(file_path, audio_path, wait_time):
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

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
    pygame.mixer.music.stop()

def tralalero():
    threading.Thread(target=play_video, args=("tralalero.mp4", "tralalero.mp3", 36), daemon=True).start()

def capuchino():
    threading.Thread(target=play_video, args=("capuchino.mp4", "capuchino.mp3", 12), daemon=True).start()

# Main App
root = tk.Tk()
root.title("Brainlapse")
root.geometry("700x450")
root.resizable(False, False)

# Gradient Background (horizontal)
canvas = Canvas(root, width=700, height=450)
canvas.pack(fill="both", expand=True)

for i in range(700):
    red = int(255 - (i / 700) * 155)
    blue = int(100 + (i / 700) * 155)
    color = f'#{red:02x}30{blue:02x}'
    canvas.create_line(i, 0, i, 450, fill=color)

# Simulate Rounded Black Box
rounded_box = tk.Frame(root, bg="#1a1a1a", bd=0)
rounded_box.place(relx=0.5, rely=0.5, anchor="center")

# Add padding inside the box
main_frame = tk.Frame(rounded_box, bg="#1a1a1a", padx=40, pady=30)
main_frame.pack()

# Title
title = tk.Label(main_frame, text="🎬 Brainlapse", font=("Segoe UI", 24, "bold"), fg="white", bg="#1a1a1a")
title.pack(pady=(0, 5))

author = tk.Label(main_frame, text="by Matthewmatician", font=("Segoe UI", 12), fg="#cccccc", bg="#1a1a1a")
author.pack(pady=(0, 20))

# Modern Button Function
def create_modern_button(text, command, bg_color, hover_color):
    btn = tk.Label(main_frame, text=text, font=("Segoe UI", 12, "bold"), bg=bg_color, fg="black",
                   width=25, height=2, bd=0, relief="flat", cursor="hand2")
    btn.pack(pady=10)

    def on_enter(e):
        btn.config(bg=hover_color)

    def on_leave(e):
        btn.config(bg=bg_color)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.bind("<Button-1>", lambda e: command())
    return btn

# Buttons
create_modern_button("🦈 tralalero tralala", tralalero, "#ffd700", "#ffee88")
create_modern_button("☕ Capuchino Assassino", capuchino, "#00ccff", "#66e0ff")

root.mainloop()
