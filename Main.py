import PIL
import tkinter as tk
from PIL import Image, ImageTk
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
        # Now create the buttons
        male_button = tk.Button(frame, image=self.male_img)
        female_button = tk.Button(frame, image=self.female_img)
        # Create photoinstances of the images
        self.Male_photo = ImageTk.PhotoImage(male_img)
        self.Female_photo = ImageTk.PhotoImage(female_img)
        # Store frame to switch later
        self.frames["second"] = frame
      # frame 3
    def create_skcolor_page(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="Pick a Skin Color.")
        label.pack(pady=20)
        # Back to home page button
        reset_button = tk.Button(frame, text="Reset", command=lambda: self.show_frame("start"))
        reset_button.pack(pady=10)
        nxt_button = tk.Button(frame, text="Continue ->", command=lambda: self.show_frame("fourth"))
        nxt_button.pack(pady=10)
        # Store frame to switch later
        self.frames["third"] = frame
      # frame 4
    def create_eyecolor_page(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="Pick a Eye Color.")
        label.pack(pady=20)
        # Back to home page button
        reset_button = tk.Button(frame, text="Reset", command=lambda: self.show_frame("start"))
        reset_button.pack(pady=10)
        nxt_button = tk.Button(frame, text="Continue ->", command=lambda: self.show_frame("fifth"))
        nxt_button.pack(pady=10)
        # Store frame to switch later
        self.frames["fourth"] = frame
      # frame 5
    def create_outfits_page(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="The best part: Pick your favorite outfit")
        label.pack(pady=20)
        # Back to home page button
        reset_button = tk.Button(frame, text="Reset", command=lambda: self.show_frame("start"))
        reset_button.pack(pady=10)
        nxt_button = tk.Button(frame, text="Continue ->", command=lambda: self.show_frame("sixth"))
        nxt_button.pack(pady=10)
    
      # Store frame to switch later
        self.frames["fifth"] = frame
    # frame 6
    def create_final_page(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="How do you like it?")
        label.pack(pady=20)
        # Back to home page button
        reset_button = tk.Button(frame, text="Reset", command=lambda: self.show_frame("start"))
        reset_button.pack(pady=10)
        # Store frame to switch later
        self.frames["sixth"] = frame
    def show_frame(self, page_name):
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()
        # Show the selected frame
        self.frames[page_name].pack()
# Create the Tkinter root window
root = tk.Tk()
# Create the application object
app = App(root)
# Start the Tkinter main loop
root.mainloop()


