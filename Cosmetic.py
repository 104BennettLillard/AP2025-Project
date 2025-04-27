import PIL
import tkinter as tk
from PIL import Image, ImageTk

#the isMale boolean will be decided depending on a 0 or 1. 0 is male, and 1 is female
def gender_picked(gender):
    global isMale
    if (gender == 0):
        isMale = True
        return
    else:
        isMale = False
        return
    
def skin_color_picked(idx):
        global final_skin_color
        skin_color_path = "Face Colors/"
        colors = ["Color1.png", "Color2.png", "Color3.png", "Color4.png", "Color5.png", "Color6.png", "Color7.png","Color8.png","Color9.png","Color10.png"]
        final_skin_color = skin_color_path + colors[idx]
        return

def eye_color_picked(idx):
        global final_eye_color
        eye_color_path = "EyeColors/"
        eye_colors = ["Amber.png", "Black.png", "Blue.png", "Brown.png", "Green.png", "Hazel.png"]
        final_eye_color = eye_color_path + eye_colors[idx]
        return

