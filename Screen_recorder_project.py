import tkinter as tk
from tkinter import messagebox
import threading
import cv2
import numpy as np
import pyautogui
import time


class ScreenRecorder:
    def __init__(self):
        self.recording = False
        self.out = None
        self.fps = 20.0
        self.screen_size = pyautogui.size()
        self.filename = "recording.mp4"

    def start_recording(self):
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        self.out = cv2.VideoWriter(self.filename, fourcc, self.fps, (self.screen_size[0], self.screen_size[1]))
        self.recording = True

    def record(self):
        while self.recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)
            time.sleep(1/self.fps)

        self.thread = threading.Thread(target=self.record)
        self.thread.start()

    def stop_recording(self):
        self.recording = False
        if self.out:
            self.out.release()

class RecorderApp:
    def __init__(self, root):
        self.recorder = ScreenRecorder()

        root.title("Screen Recoder Application")
        root.geometry("300x150")
        root.resizable(False, False)

        self.start_button = tk.Button(root, text="Start Recording", comman=self.start_recording, bg="green" , fg="white", font = ("Times New Roman", 20))
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(root, text="Stop Recording", command=self.stop_recording, bg="red", fg="white", font = ("Times New Roman", 20))
        self.stop_button.pack(pady=20)

    def start_recording(self):
        if not self.recorder.recording:
            self.recorder.start_recording()
            messagebox.showinfo("Record Started", "Recording started")
        else:
            messagebox.showwarning("ALready recording", "ALready recording")

    def stop_recording(self):
        if self.recorder.recording:
            self.recorder.stop_recording()
            messagebox.showinfo("Recording Stopped", "Recording stopped")
        else:
            messagebox.showwarning("Not Recording", "Not Recording")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecorderApp(root)
    root.mainloop()