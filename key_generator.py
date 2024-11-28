import random
import time
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk
import pygame

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#запускайте музыку
pygame.mixer.init()
pygame.mixer.music.load("labo.mp3")  
pygame.mixer.music.play(-1) 

#генерирует ключ
def generator():
    try:
        key_top = random.choice(alphabet)
        key_bottom = random.choice(alphabet)
        
        # упорядочивание случайных вариантов таким образом, чтобы начало всегда было меньше конца
        if ord(key_top) > ord(key_bottom):
           key_top, key_bottom = key_bottom, key_top
        
        #Блоки 1 и 3 - это порядковые значения букв
        block1 = f"{ord(key_top) - 64:02d}"  
        block3 = f"{ord(key_bottom) - 64:02d}"
        
        interval = [chr(i) for i in range(ord(key_top), ord(key_bottom) + 1)]
        block2 = ''.join(random.choices(interval, k=7))
        
        # Формат ключа
        key = f"{block1}\n{block2}\n{block3}"
        
        # изменение отображения
        key_field.config(state="normal")
        key_field.delete(1.0, "end")
        key_field.insert("end", key)
        key_field.config(state="disabled")
        
        animate_key()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Функция анимации для генерации ключа
def animate_key():
    for _ in range(3):
        key_field.config(bg="yellow")
        window.update()
        time.sleep(0.1)
        key_field.config(bg="white")
        window.update()
        time.sleep(0.1)

# Главное окно
window = tk.Tk()
window.title("Генератор ключей")
window.geometry("800x450")

bg_img = Image.open("lab.jpg") 
bg_img = bg_img.resize((800, 450), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)

bg_lbl = tk.Label(window, image=bg_photo)
bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

# Этикетка
lbl = tk.Label(window, text="Генератор ключей", font=("Arial", 24, "bold"), bg="#000000", fg="white")
lbl.pack(pady=10)

# Ключевое поле отображения
key_frame = tk.Frame(window, bg="black", padx=10, pady=10)
key_frame.pack(pady=20)
key_field = tk.Text(key_frame, font=("Courier", 18), width=10, height=3, state="disabled", bg="white", fg="black")
key_field.pack()

# Ключевая кнопка
btn = tk.Button(window, text="Cгенерируйте ключ", font=("Arial", 16), command=generator, bg="#008CBA", fg="white")
btn.pack(pady=10)

window.mainloop()

pygame.mixer.music.stop()