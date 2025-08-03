"""Separete file for application header"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from menu import Menu

class ApplicationHeader():
  def __init__(self,master):

    self.master = master
    self.create_header(master)
    self.initialize_application_name()
   

  def initialize_menu(self):

    self.menu = Menu(self.button_frame)

  def create_header(self, master):
    """Create a header to display application name and logo"""

    # Change the color of frames
    self.header_color= ttk.Style()
    self.header_color.configure("Header.TFrame", background="#FFA842")
    self.header_color.configure("Frame.TFrame", background="#FFA842")

    # Frames 
    self.header = ttk.Frame(master, width=760, height=30, padding="5", style="Header.TFrame")
   

    # This is a frame between the to images to place the logo on the right side of the header 
    self.frame_inside_header = ttk.Frame(self.header, width=300, height=50, style="Frame.TFrame")
    self.button_frame = ttk.Frame(self.header, width=100, height=50, style="Frame.TFrame")

    # Frame positions
    self.header.grid(row=0, column=0, columnspan=3, sticky="new", padx=0, pady=5)
    self.frame_inside_header.grid(row=0, column=2, columnspan=3, sticky="e")
    self.button_frame.grid(row=0, column=5, columnspan=3, sticky="e", padx=20, pady=0)

    
  def initialize_application_name(self):
    """Initialize Application name"""

    try:
      # If the image fails to load, ensure that the entire directory containing the city_gym_text.png image is copied or provided
      application_name = "images/Logo.png" 
      
      text_image = Image.open(application_name).convert("RGBA")
      resize_text_image = text_image.resize((100,60), Image.LANCZOS)
      self.city_gym = ImageTk.PhotoImage(resize_text_image)
      self.city_gym_label = ttk.Label(self.header, image=self.city_gym, background="#FFA842")
      self.city_gym_label.grid(row=0, column=0, sticky="w",  padx=20, pady=0)
      
    except Exception as e:
        # Handle the error if loading the image fails
        print("Error loading icon:", e)

class MainMenuHeader():
  def __init__(self,master):

    self.master = master
    self.create_header(master)
    self.initialize_application_name()
    

  def create_header(self, master):
    """Create a header to display application name and logo"""

    # Change the color of frames
    self.header_color= ttk.Style()
    self.header_color.configure("Header.TFrame", background="#FFA842")
    self.header_color.configure("Frame.TFrame", background="#FFA842")

    # Frames 
    self.header = ttk.Frame(master, width=260, height=30, padding="5", style="Header.TFrame")
    self.bottom_frame = ttk.Frame(master, width=700, height=20, padding="5", style="Header.TFrame")

    # This is a frame between the to images to place the logo on the right side of the header 
    self.frame_inside_header = ttk.Frame(self.header, width=500, height=50, style="Frame.TFrame")

    # Frame positions
    self.header.grid(row=0, column=0, columnspan=3, sticky="new", padx=0, pady=5)
    self.frame_inside_header.grid(row=0, column=1, columnspan=5, sticky="ew")
    self.bottom_frame.grid(row=9, column=0, columnspan=3, sticky="s", padx=0, pady=0)

  def initialize_application_name(self):
    """Initialize Application name"""

    try:
      # If the image fails to load, ensure that the entire directory containing the city_gym_text.png image is copied or provided
      application_name = "images/Logo.png" 
      
      text_image = Image.open(application_name).convert("RGBA")
      resize_text_image = text_image.resize((95,60), Image.LANCZOS)
      self.city_gym = ImageTk.PhotoImage(resize_text_image)
      self.city_gym_label = ttk.Label(self.header, image=self.city_gym, background="#FFA842")
      self.city_gym_label.grid(row=0, column=0, sticky="w",  padx=20, pady=0)
      
    except Exception as e:
        # Handle the error if loading the image fails
        print("Error loading icon:", e)

  