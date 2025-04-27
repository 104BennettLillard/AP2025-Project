import PIL
import tkinter as tk
from PIL import Image, ImageTk

# Initialize global variables with default values (Github Copilot)
final_skin_color = "none"
final_eye_color = "none"
final_hair_color = "none"
final_outfit = "none"
isMale = True  # Default gender (can be changed later)

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

def hair_picked(idx):
        global final_hair_color
        hair_path = "Hair/"
        hair = ["BrownShort.png", "BlondeShort.png", "BrownBun.png", "BlondeBun.png", "BrownLong.png", "BlondeLong.png"]
        final_hair_color = hair_path + hair[idx]
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
def finalize_character(self):
    global final_skin_color
    global final_eye_color
    global final_hair_color
    global final_outfit

     # Set defaults if any of the options are missing
    if final_skin_color == "none":
        final_skin_color = "Face Colors/Color1.png"
    if final_eye_color == "none":
        final_eye_color = "EyeColors/Amber.png"
    if final_hair_color == "none":
        final_hair_color = "Hair/BrownShort.png"
    if final_outfit == "none":
        if isMale:
            final_outfit = "MaleOutfits/MaRed.png"
        else:
            final_outfit = "FemaleOutfits/FeRed.png"  # example fallback for females
    # Load images
    skin_image = Image.open(final_skin_color)
    eye_image = Image.open(final_eye_color)
    hair_image = Image.open(final_hair_color)
    outfit_image = Image.open(final_outfit)

    # Convert for Tkinter
    self.skin_photo = ImageTk.PhotoImage(skin_image)
    self.eye_photo = ImageTk.PhotoImage(eye_image)
    self.hair_photo = ImageTk.PhotoImage(hair_image)
    self.outfit_photo = ImageTk.PhotoImage(outfit_image)

    # Clear the canvas first if needed
    self.final_canvas.delete("all")

    # Draw images centered at (200, 300)
    self.final_canvas.create_image(400, 490, image=self.outfit_photo)
    self.final_canvas.create_image(400, 325, image=self.skin_photo)
    self.final_canvas.create_image(400, 300, image=self.eye_photo)
    self.final_canvas.create_image(400, 290, image=self.hair_photo)
