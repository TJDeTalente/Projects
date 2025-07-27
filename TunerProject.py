import tkinter as tk
import sounddevice as sd
import numpy as np
from scipy.fft import rfft, rfftfreq
import math

# 🎸 Standard Guitar Frequencies
GUITAR_STRINGS = {
    "E2": 82.41,
    "A2": 110.00,
    "D3": 146.83,
    "G3": 196.00,
    "B3": 246.94,
    "E4": 329.63
}

SAMPLE_RATE = 44100
DURATION = 0.5


def detect_pitch(audio, sample_rate):
    N = len(audio)
    yf = np.abs(rfft(audio))
    xf = rfftfreq(N, 1 / sample_rate)
    peak_idx = np.argmax(yf)
    return xf[peak_idx]


def closest_string(freq):
    return min(GUITAR_STRINGS.items(), key=lambda x: abs(x[1] - freq))


class GuitarTunerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guitar Tuner")
        self.root.geometry("400x400")
        self.root.configure(bg="black")

        # LABELS
        self.note_label = tk.Label(root, text="--", font=("Arial", 32, "bold"), fg="lime", bg="black")
        self.note_label.pack(pady=10)

        self.freq_label = tk.Label(root, text="0 Hz", font=("Arial", 16), fg="white", bg="black")
        self.freq_label.pack()

        # CANVAS
        self.canvas = tk.Canvas(root, width=300, height=200, bg="black", highlightthickness=0)
        self.canvas.pack()

        self.center_x = 150
        self.center_y = 150
        self.needle = self.canvas.create_line(
            self.center_x, self.center_y, self.center_x, 50, width=4, fill="red"
        )

        self.update_tuner()

    def update_tuner(self):
        audio = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype='float64')
        sd.wait()
        audio = audio.flatten()

        freq = detect_pitch(audio, SAMPLE_RATE)
        note, target_freq = closest_string(freq)
        diff = freq - target_freq

        # --- Update Labels ---
        self.note_label.config(text=note)
        self.freq_label.config(text=f"{freq:.1f} Hz")

        # Move Needle
        # Map frequency difference (-10 to +10 Hz) to angle (-45 to +45 degrees)
        diff = max(min(diff, 10), -10)
        angle = (diff / 10) * 45  # degrees

        rad = math.radians(angle)
        needle_length = 80
        x_end = self.center_x + needle_length * math.sin(rad)
        y_end = self.center_y - needle_length * math.cos(rad)
        self.canvas.coords(self.needle, self.center_x, self.center_y, x_end, y_end)

        # Feedback Visual
        if abs(diff) < 1.0:
            self.note_label.config(fg="lime")
        elif diff > 0:
            self.note_label.config(fg="red")
        else:
            self.note_label.config(fg="yellow")

        # Refresh
        self.root.after(500, self.update_tuner)


if __name__ == "__main__":
    root = tk.Tk()
    app = GuitarTunerApp(root)
    root.mainloop()
