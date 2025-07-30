import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os


# Functions
def record_and_translate():
    source_lang = source_lang_var.get()
    target_lang = target_lang_var.get()

    output_label.config(text="🎤 Listening...", fg="blue")
    root.update()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=source_lang)
        output_label.config(text=f"✅ You said: {text}", fg="green")
        root.update()

        # Translate
        translator = Translator()
        translated = translator.translate(text, dest=target_lang).text
        translated_label.config(text=f"🌍 Translation: {translated}", fg="purple")

        # Speak translation
        tts = gTTS(text=translated, lang=target_lang)
        filename = "temp_translation.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    except sr.UnknownValueError:
        output_label.config(text="❌ Could not understand audio.", fg="red")
    except sr.RequestError:
        output_label.config(text="❌ API unavailable.", fg="red")


# GUI
root = tk.Tk()
root.title("Multilingual Speech Translator")
root.geometry("400x300")

# Language selector
source_lang_var = tk.StringVar(value="en")
target_lang_var = tk.StringVar(value="es")

tk.Label(root, text="Source Language:").pack()
source_dropdown = ttk.Combobox(root, textvariable=source_lang_var, values=["en", "es", "fr", "de", "hi", "zh-cn", "ar"])
source_dropdown.pack()

tk.Label(root, text="Target Language:").pack()
target_dropdown = ttk.Combobox(root, textvariable=target_lang_var, values=["en", "es", "fr", "de", "hi", "zh-cn", "ar"])
target_dropdown.pack()

tk.Button(root, text="🎤 Speak & Translate", command=record_and_translate, bg="lightblue").pack(pady=10)

output_label = tk.Label(root, text="", wraplength=350)
output_label.pack()

translated_label = tk.Label(root, text="", wraplength=350)
translated_label.pack()

root.mainloop()
