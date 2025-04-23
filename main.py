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

# --- GUI Setup ---
root = tk.Tk()
root.title("Brainlapse")
root.geometry("700x450")
root.resizable(False, False)

# Gradient Background
canvas = Canvas(root, width=700, height=450)
canvas.pack(fill="both", expand=True)

for i in range(700):
    red = int(255 - (i / 700) * 155)
    blue = int(100 + (i / 700) * 155)
    color = f'#{red:02x}30{blue:02x}'
    canvas.create_line(i, 0, i, 450, fill=color)

# Rounded black box (center container)
rounded_box = tk.Frame(root, bg="#1a1a1a")
rounded_box.place(relx=0.5, rely=0.5, anchor="center")

main_frame = tk.Frame(rounded_box, bg="#1a1a1a", padx=40, pady=30)
main_frame.pack()

# Title
title = tk.Label(main_frame, text="🎬 Brainlapse", font=("Segoe UI", 24, "bold"), fg="white", bg="#1a1a1a")
title.pack(pady=(0, 5))

author = tk.Label(main_frame, text="Python Tkinter Practice by Matthewmatician", font=("Segoe UI", 12), fg="#cccccc", bg="#1a1a1a")
author.pack(pady=(0, 20))

# --- Gradient Button Function ---
def create_gradient_button(parent, text, command, width=250, height=50, start_color="#ff9f30", end_color="#641aff"):
    btn_canvas = Canvas(parent, width=width, height=height, bd=0, highlightthickness=0, relief="ridge", cursor="hand2")

    def lighten(hex_color, factor=0.15):
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        r = min(int(r + (255 - r) * factor), 255)
        g = min(int(g + (255 - g) * factor), 255)
        b = min(int(b + (255 - b) * factor), 255)
        return f'#{r:02x}{g:02x}{b:02x}'

    normal_colors = (start_color, end_color)
    hover_colors = (lighten(start_color), lighten(end_color))

    def draw_gradient(start, end):
        btn_canvas.delete("all")
        r1, g1, b1 = int(start[1:3], 16), int(start[3:5], 16), int(start[5:7], 16)
        r2, g2, b2 = int(end[1:3], 16), int(end[3:5], 16), int(end[5:7], 16)
        for i in range(width):
            r = int(r1 + (r2 - r1) * (i / width))
            g = int(g1 + (g2 - g1) * (i / width))
            b = int(b1 + (b2 - b1) * (i / width))
            hex_color = f'#{r:02x}{g:02x}{b:02x}'
            btn_canvas.create_line(i, 0, i, height, fill=hex_color)
        btn_canvas.create_text(width // 2, height // 2, text=text, fill="white", font=("Segoe UI", 12, "bold"), tags="button_text")

    draw_gradient(*normal_colors)

    btn_canvas.bind("<Button-1>", lambda event: command())
    btn_canvas.bind("<Enter>", lambda e: draw_gradient(*hover_colors))
    btn_canvas.bind("<Leave>", lambda e: draw_gradient(*normal_colors))

    btn_canvas.pack(pady=10)


# Buttons
create_gradient_button(main_frame, "🦈 Tralalero Tralala", tralalero)
create_gradient_button(main_frame, "☕ Capuchino Assassino", capuchino, start_color="#641aff", end_color="#ff9f30")

root.mainloop()
