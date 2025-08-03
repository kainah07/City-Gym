"""Separete file for optioonal extras"""

# Import necessary modules
import tkinter as tk
from tkinter import ttk

class OptionalExtras:
  def __init__ (self, master):
    """A class managing Optional extras GUI"""
    
    self.master = master
    self.create_widgets_container()
    self.initialize_price_label()
    self.initialize_checkbutton_widgets()
  
  def create_widgets_container(self):
    """Create a container to display all optional extras check buttons"""

    # Optional extras container
    self.frame = ttk.Frame(self.master, style="Container.TFrame", width=40, height=25 )
    self.text_frame = ttk.Frame(self.frame, style="Label.TFrame", width=40, height=25)
    self.optional_extras = ttk.Label(self.text_frame, text="Optional extras", 
                                          background="#FFA842", foreground="white", 
                                          padding="1", style="Custom.TLabel")
    
     # Widgets positions 
    self.frame.grid(row= 1, column= 1, sticky="ne", padx=20, pady=20)
    self.text_frame.grid(row=1, column=0,columnspan=3, sticky="w", padx=5, pady=5)
    self.optional_extras.grid(row=0, columnspan=5, sticky="w", padx=118, pady=0)

  def initialize_price_label(self):

    self.prices = [ttk.Label(self.frame, text="----------------------  $1"),
                  ttk.Label(self.frame, text="----------------------  $20"),
                  ttk.Label(self.frame, text="----------------------  $20"),
                  ttk.Label(self.frame, text="----------------------  $2")
                  ]
    for i,price in enumerate(self.prices):
      price.grid(row=i +3, column=1, sticky="w", padx= 5, pady=5)

  def initialize_checkbutton_widgets(self):
    """Initialize optional extras check button selections"""

    # Define varible for optional extras
    self.twenty_four_access = tk.BooleanVar()
    self.personal_trainer = tk.BooleanVar()
    self.diet_consultation = tk.BooleanVar()
    self.access_online_video = tk.BooleanVar()
    
    # Optional extras checkbuttons
    self.extras = [ttk.Checkbutton(self.frame, text="24/7 access", variable=self.twenty_four_access),
                   ttk.Checkbutton(self.frame, text="Personal trainer", variable=self.personal_trainer),
                   ttk.Checkbutton(self.frame, text="Diet consultation", variable=self.diet_consultation),
                   ttk.Checkbutton(self.frame, text="Acces online fitness video", variable=self.access_online_video)]
    
    for i,checkbotton in enumerate(self.extras):
      checkbotton.grid(row=i +3, column=0, sticky="w", padx=5, pady=5)
   

  def get_twenty_four_access(self):
    """ Check if the '24/7 Access' option is selected by the user. """
    
    if self.twenty_four_access.get():
      extra = True
    else:
      extra = False

    return extra

  def get_personal_trainer(self):
    """ Check if the 'personal trainer' option is selected by the user. """
  
    if self.personal_trainer.get():
      extra = True
    else:
      extra = False

    return extra

  def get_diet_consultation(self):
    """ Check if the 'diet consultation' option is selected by the user. """

    if self.diet_consultation.get():
      extra = True
    else:
      extra = False

    return extra

  def get_access_online_video(self):
    """ Check if the 'access online video' option is selected by the user. """
    
    if self.access_online_video.get():
      extra = True
    else:
      extra = False

    return extra

  # Get total amount of selected extras
  def calculate_total_extra(self):
    """Calculate the total amount of etras selected by the user"""
    
    extras_total = 0 

    if self.twenty_four_access.get():
      extras_total += 1
    if self.personal_trainer.get():
      extras_total += 20
    if self.diet_consultation.get():
      extras_total += 20
    if self.access_online_video.get():
      extras_total += 2

    return extras_total
  
  def reset(self):
    """Reset all selected check buttons"""
      
    self.twenty_four_access.set(0)
    self.personal_trainer.set(0)
    self.diet_consultation.set(0)
    self.access_online_video.set(0)

  