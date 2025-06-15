from tkinter import messagebox, ttk
import tkinter as tk
import random
import time


root = tk.Tk()
root.title("Sorting Visualizer")

canvas = tk.Canvas(root, width=800, height=400, bg='white')
canvas.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

data = [random.randint(10, 300) for _ in range(100)]
# data = 

speed_scale = tk.Scale(frame, from_=0.01, to=0.5, length=200, digits=2, resolution=0.01, orient='horizontal', label="Speed")
speed_scale.set(0.25)
speed_scale.grid(row=0, column=3, padx=5)