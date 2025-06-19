import tkinter as tk
from tkinter import *
from model.predict import predict_digit
from PIL import Image, ImageDraw
import numpy as np

def on_button_click():
    digit, confidence = predict_digit(image1)

    result_label.config(text=f"Predicted: {digit} with {confidence:.2f}% confidence")

def clear_canvas():
    canvas.delete("all")
    draw.rectangle((0, 0, 280, 280), fill="white")

def savePosn(event):
       global lastx, lasty
       lastx, lasty = event.x, event.y
  
def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), width=8, fill='black', capstyle='round', smooth=True)
    draw.line((lastx, lasty, event.x, event.y), fill='black', width=8)
    savePosn(event)

# Set up the main window
root = tk.Tk()
root.title("Live Digit Classifier")
root.geometry("600x600")

# Title label
title_label = Label(root, text="Welcome to the Live Digit Classifier!", font=("Helvetica", 48))
title_label.pack()

# Subtitle label
subtitle_label = Label(root, text="Please draw a digit from 0–9 below", font=("Helvetica", 24))
subtitle_label.pack()

# Drawing canvas
canvas = Canvas(root, bg='white', width=280, height=280)
image1 = Image.new("L", (280, 280), 'white')  # L = grayscale
draw = ImageDraw.Draw(image1)
canvas.pack()
canvas.bind("<Button-1>", savePosn)
canvas.bind("<B1-Motion>", addLine)

# Result label
result_label = Label(root, text="", font=("Helvetica", 18))
result_label.pack()

# Buttons for predict and clear
predict_btn = Button(root, text="Predict", command=on_button_click)
predict_btn.pack()

clear_btn = Button(root, text="Clear", command=clear_canvas)
clear_btn.pack()

root.mainloop()
