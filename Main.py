import tkinter as tk
from PIL import Image, ImageTk

from Cosmetic import gender_picked, skin_color_picked, eye_color_picked, outfit_picked, hair_picked, finalize_character

isMale = True
final_skin_color = "none"
final_eye_color = "none"
final_hair_color = "none"
final_outfit = "none"
class App:
  # The intial framework for the start and gender pages, as well as the show_frame procedures take credit from Chatgpt
    def __init__(self, root):
        self.root = root
        self.root.title("Multipage Tkinter Application")
        # Create a container for all frames
        self.frames = {}
        # Initialize frames
        self.create_start_page()
        self.create_gender_page()
        self.create_skcolor_page()
        self.create_eyecolor_page()
        self.create_hair_page()
        self.create_outfits_page()
        self.create_final_page()
  # frame 1
    def create_start_page(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="Are you ready to make your character?")
        label.grid(column=0,row=0)
        # Switch to second page button
        nxt_button = tk.Button(frame, text="Get Started", command=lambda: self.show_frame("second"))
        nxt_button.grid(column=0,row=6)
        # Store frame to switch later
        self.frames["start"] = frame
        # Pack the frame
        frame.pack()
  # frame 2
    def create_gender_page(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="Pick a Gender.")
        label.grid(column=0,row=0)
        # Back to home page button
        reset_button = tk.Button(frame, text="Reset", command=lambda: self.show_frame("start"))
        reset_button.grid(column=1,row=1)
        nxt_button = tk.Button(frame, text="Continue ->", command=lambda: self.show_frame("third"))
        nxt_button.grid(column=0,row=1)
        # load images for both male and female
        male_img = Image.open("MaleOutfits/Male.png")
        female_img = Image.open("FemaleOutfits/Female.png")
        # Create photoinstances of the images
        self.male_photo = ImageTk.PhotoImage(male_img)
        self.female_photo = ImageTk.PhotoImage(female_img)
        # Now create the buttons
        male_button = tk.Button(frame, image=self.male_photo, command=gender_picked(0))
        male_button.grid(column=0,row=2)
        female_button = tk.Button(frame, image=self.female_photo, command=gender_picked(1),)
        female_button.grid(column=1,row=2)
        # Store frame to switch later
        self.frames["second"] = frame
  # frame 3
    def create_skcolor_page(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="Pick a Skin Color.")
        label.grid(column=0,row=0)
        # Back to home page button
        reset_button = tk.Button(frame, text="Reset", command=lambda: self.show_frame("start"))
        reset_button.grid(column=1,row=1)
        nxt_button = tk.Button(frame, text="Continue ->", command=lambda: self.show_frame("fourth"))
        nxt_button.grid(column=0,row=1)
        # iteration time. This will create a grid of buttons with all skin tones
        skin_color_path = "Face Colors/"
        colors = ["Color1.png", "Color2.png", "Color3.png", "Color4.png", "Color5.png", "Color6.png", "Color7.png","Color8.png","Color9.png","Color10.png"]
        i = 1
        for idx, color in enumerate(colors):
          color_img = Image.open(skin_color_path + color)
          self.color_photo = ImageTk.PhotoImage(color_img)
          color_btn = tk.Button(frame, image=self.color_photo, command=lambda idx=idx:skin_color_picked(idx))
          color_btn.image = self.color_photo  # Keep a reference to avoid garbage collection (Github copilot)
          if idx % 2 == 0:
              color_btn.grid(row=2, column=(idx // 2))
          else:
              color_btn.grid(row=3, column=(idx - i))
              i += 1

        # Store frame to switch later
        self.frames["third"] = frame
  # frame 4
    def create_eyecolor_page(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="Pick a Eye Color.")
        label.grid(column=0,row=0)
        # Back to home page button
        reset_button = tk.Button(frame, text="Reset", command=lambda: self.show_frame("start"))
        reset_button.grid(column=1,row=1)
        nxt_button = tk.Button(frame, text="Continue ->", command=lambda: self.show_frame("fifth"))
        nxt_button.grid(column=0,row=1)
        # Iterate through all the eyes and make a grid of buttons
        eye_color_path = "EyeColors/"
        eye_colors = ["Amber.png", "Black.png", "Blue.png", "Brown.png", "Green.png", "Hazel.png"]
        i = 1
        for idx, color in enumerate(eye_colors):
          color_img = Image.open(eye_color_path + color)
          self.color_photo = ImageTk.PhotoImage(color_img)
          color_btn = tk.Button(frame, image=self.color_photo, command=lambda idx=idx: eye_color_picked(idx))
          color_btn.image = self.color_photo #to avoid garbage collection
          if idx % 2 == 0:
              color_btn.grid(row=2, column=(idx // 2))
          else:
              color_btn.grid(row=3, column=(idx - i))
              i += 1

        # Store frame to switch later
        self.frames["fourth"] = frame
  # frame 5
    def create_hair_page(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="Pick a Hair Color.")
        label.grid(column=0,row=0)
        # Back to home page button
        reset_button = tk.Button(frame, text="Reset", command=lambda: self.show_frame("start"))
        reset_button.grid(column=1,row=1)
        nxt_button = tk.Button(frame, text="Continue ->", command=lambda: self.show_frame("sixth"))
        nxt_button.grid(column=0,row=1)
        # Iterate through all the hair colors and make a grid of buttons
        hair_color_path = "Hair/"
        hair = ["BrownShort.png", "BlondeShort.png", "BrownBun.png", "BlondeBun.png", "BrownLong.png", "BlondeLong.png"]
        i = 1
        for idx, color in enumerate(hair):
          hair_img = Image.open(hair_color_path + color)
          self.color_photo = ImageTk.PhotoImage(hair_img)
          color_btn = tk.Button(frame, image=self.color_photo, command=lambda idx=idx: hair_picked(idx))
          color_btn.image = self.color_photo #to avoid garbage collection
          if idx % 2 == 0:
              color_btn.grid(row=2, column=(idx // 2))
          else:
              color_btn.grid(row=3, column=(idx - i))
              i += 1
        
        # Store frame to switch later
        self.frames["fifth"] = frame
  # frame 6
    def create_outfits_page(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="The best part: Pick your favorite outfit")
        label.grid(column=0,row=0)
        # Back to home page button
        reset_button = tk.Button(frame, text="Reset", command=lambda: self.show_frame("start"))
        reset_button.grid(column=1,row=1)
        nxt_button = tk.Button(frame, text="Continue ->", command=self.finalize_and_show)
        nxt_button.grid(column=0,row=1)
        # iterate through all the outfits and make a grid of buttons
        outfit_path = "MaleOutfits/"
        outfits = ["MaRed.png", "MaOrange.png", "MaYellow.png", "MaGreen.png", "MaBlue.png", "MaPurple.png", "MaPink.png", "MaBlack.png"]
        for idx, outfit in enumerate(outfits):
          outfit_img = Image.open(outfit_path + outfit)
          self.outfit_photo = ImageTk.PhotoImage(outfit_img)
          outfit_btn = tk.Button(frame, image=self.outfit_photo, command=lambda idx=idx: outfit_picked(idx))
          outfit_btn.image = self.outfit_photo #to avoid garbage collection
          if idx > 3:
              outfit_btn.grid(row=3, column=(idx - 4))
          else:
              outfit_btn.grid(row=2, column=(idx))
             
      # Store frame to switch later
        self.frames["sixth"] = frame
  # final frame
    def create_final_page(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="How do you like it?")
        label.grid(column=0, row=0)
        # Back to home page button
        reset_button = tk.Button(frame, text="Reset", command=self.reset_game)
        reset_button.grid(column=0, row=1)
        # The canvas will be used to display the final character
        self.final_canvas = tk.Canvas(frame, width=750, height=750)
        self.final_canvas.grid(row=1, column=2, columnspan=2)
        # Store frame to switch later
        self.frames["final"] = frame
    def show_frame(self, page_name):
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()
        # Show the selected frame
        self.frames[page_name].pack()
#once the user has selected all the options, the final page will show up with the character they made
    def finalize_and_show(self):
      self.show_frame("final")
      finalize_character(self)

    def reset_game(self):
      self.show_frame("start")
      final_skin_color = "none"
      final_eye_color = "none"
      final_hair_color = "none"
      final_outfit = "none"
      isMale = True 

# Create the Tkinter root window
root = tk.Tk()
# Create the application object
app = App(root)
# Start the Tkinter main loop
root.mainloop()


