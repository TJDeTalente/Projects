import tkinter as tk
import sounddevice as sd
import numpy as np
import threading

 # Standard Tuning Frequencies

NOTES = {
    "E2": 82.41,
    "A2": 110.00,
    "D3": 146.83,
    "G3": 196.00,
    "B3": 246.94,
    "E4": 329.63
}

sample_rate = 44100
duration = 0.5

# Pitch Detection

def detect_frequency(audio_data):
    fft_result = np.fft.fft(audio_data)
    freqs = np.fft.fftfreq(len(fft_result), 1 / sample_rate)
    positive_freqs = freqs[:len(freqs)//2]
    magnitudes = np.abs(fft_result[:len(freqs)//2])
    return positive_freqs[np.argmax(magnitudes)]

def find_closest_note(freq):
    closest = min(NOTES, key=lambda n: abs(NOTES[n] - freq))
    return closest, freq - NOTES[closest]

def update_tuner():
    while running:
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="float64")
        sd.wait()
        audio = audio.flatten()

        freq = detect_frequency(audio)
        note, diff = find_closest_note(freq)

    # Update GUI
        note_label.config(text=f"{note} ({freq: .1f} Hz)")
        if abs(diff) < 1.0:
            status_label.config(text="In Tune!", fg="green")
        elif diff > 0:
            status_label.config(text="Sharp", fg="red")
        else:
            status_label.config(text="Flat", fg="red")

        # Move needle
        shift = max(min(diff * 5, 50), -50)
        canvas.coords(needle, 100, 150, 100 + shift, 80)

# GUI
def start_tuner():
    global running
    running = True
    threading.Thread(target=update_tuner, daemon=True).start()

def stop_tuner():
    global running
    running = False

root = tk.Tk()
root.title("Guitar Tuner Project")
root.geometry("250x300")

note_label = tk.Label(root, text="Play a note...", font=("Arial, 10"))
note_label.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial, 14"))
status_label.pack()

canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack()

# Draw meter

canvas.create_line(100, 150, 100, 50, width=4)
needle = canvas.create_line(100, 150, 100, 80, width=3, fill="red")

tk.Button(root, text="Start", command=start_tuner, bg="lightgreen").pack(side=tk.LEFT, padx=20, pady=10)
tk.Button(root, text="Stop", command=stop_tuner, bg="lightcoral").pack(side=tk.RIGHT, padx=20, pady=10)

running = False
root.mainloop