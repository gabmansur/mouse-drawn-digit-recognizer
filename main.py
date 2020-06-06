# Gabriella Mansur
# 07-06-2020

import tkinter as tk
from tkinter import *
import PIL
from PIL import Image, ImageDraw, ImageGrab
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
import os

##### Functions 

def predict():
    
    # get the canvas bounding box on screen
    x, y = cv.winfo_rootx(), cv.winfo_rooty()
    w, h = cv.winfo_width(), cv.winfo_height()
    # take a snapshot on the canvas and save the image to file
    ImageGrab.grab((x, y, x+w, y+h)).save('img.png')
    
    # load pre-trained model
    model = load_model('cnn-keras-model.h5')
    
    # Load and process image
    image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (28, 28))
    image = image.reshape(1, 28, 28, 1)
    image = 255 - image
    image = image/255.0
    
    result = model.predict(image)
    
#    print(result)
#    print('The number is', np.argmax(result))
  
    tk.messagebox.showinfo("Prediction", "The number is " + str(np.argmax(result)))

        
#def save():
#    filename = f'img.png'
#    image1.save(filename)
    
    
def clear():
    cv.delete("all")

def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), width=15)
    #  --- PIL
    draw.line((lastx, lasty, x, y), fill='black', width=10)
    lastx, lasty = x, y
    
##### Main 

root = Tk()
root.title("Predicting your mouse-drawn digit")
lastx, lasty = None, None

cv = Canvas(root, width=500, height=500, bg='white')
# --- PIL
image1 = PIL.Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(image1)

cv.bind('<1>', activate_paint)
cv.pack(expand=YES, fill=BOTH)

#btn_save = Button(text="Save", command=save)
#btn_save.pack(side="top", fill="both", expand=True)

btn_clear = Button(text="Clear", command=clear)
btn_clear.pack(side="top", fill="both", expand=True)

btn_clear = Button(text="Predict", command=predict)
btn_clear.pack(side="top", fill="both", expand=True)
        
root.mainloop()