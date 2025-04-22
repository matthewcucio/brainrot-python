# 🧠 Filipino Brainrot-Python

A chaotic little video-and-audio player powered by Python, OpenCV, Tkinter, and Pygame. Click a button and let the brainrot begin. 🎬🎧

> **Note:** This project serves as a personal **practice exercise for learning Tkinter and Python**. Built with love, bugs, and a healthy dose of experimentation.

## 🚀 Features

- Two iconic buttons:  
  - 🟡 **Tralalero Tralala** — plays `tralalero.mp4` with `tralalero.mp3` (uses `cv2.waitKey(36)`)
  - 🔵 **Capuchino Assassino** — plays `capuchino.mp4` with `capuchino.mp3` (uses `cv2.waitKey(16)`)
- Audio and video synced for maximum chaos
- Simple dark-themed GUI
- Made for laughs. Runs in a window, not in your heart (yet).

## 🛠️ Requirements

- Python 3.13.3
- `opencv-python`
- `pygame`

💡 Notes

- Press Q to stop playback.

- All video playback runs on a separate thread to keep the GUI responsive.
    

Install the required packages:

```bash
pip install opencv-python pygame


