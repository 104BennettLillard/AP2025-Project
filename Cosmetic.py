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

def outfit_picked(idx):
        global final_outfit
        global isMale
        outfit_path = " "
        if isMale:
            outfit_path = "MaleOutfits/"
            outfits = ["MaRed.png", "MaOrange.png", "MaYellow.png", "MaGreen.png", "MaBlue.png", "MaPurple.png", "MaPink.png", "MaBlack.png"]
        else:
             outfit_path = "FemaleOutfits/"
             outfits = ["FeRed.png", "FeOrange.png", "FeYellow.png", "FeGreen.png", "FeBlue.png", "FePurple.png", "FePink.png", "FeBlack.png"]  

        final_outfit = outfit_path + outfits[idx]
        return

