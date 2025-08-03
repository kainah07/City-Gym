# BIT502, SHEKINAH JOY CANOSA, 5075645, ASSESSMENT 3
"""Separete file for customers details """

# Import necessary modules
import tkinter as tk     
from tkinter import ttk

class CustomersDetails:
  def __init__(self, master):

    """A class for managing Customers details GUI"""
    
    self.master = master
    self.widgets_styles()
    self.create_widget_container()
    self.initialize_label_widgets()
    self.initialize_entry_widgets()

  def widgets_styles(self):
    """ Change frame color, font, and font sizes"""

    self.style = ttk.Style()
    self.style.configure("Container.TFrame", background="#EEEEEE")
    self.style.configure("Label.TFrame", background="#FFA842")
    self.style.configure("Custom.TLabel", font=('Microsoft Sans Serif', 10))

  def create_widget_container(self):
    
    """Create a container to display label and entry widgets"""
    
    # Frames
    self.frame = ttk.Frame(self.master, style="Container.TFrame", width=40, height=25 )
    self.text_frame = ttk.Frame(self.frame, style="Label.TFrame", width=40, height=25)
    
    # Labels 
    self.personal_information = ttk.Label(self.text_frame, text="Personal Inforamtion", 
                                          background="#FFA842", foreground="white", 
                                          padding="1", style="Custom.TLabel")
    
    # Container position
    self.frame.grid(row=1, column=0, sticky="nw", padx=20, pady=20)
    self.text_frame.grid(row=1, column=0,columnspan=3, sticky="w", padx=5, pady=5)
    self.personal_information.grid(row=0, columnspan=2, sticky="w", padx=100, pady=0)
    
  def initialize_label_widgets(self):
    """Initialize label widgets"""
  
    # First name
    self.first_name_label = ttk.Label(self.frame, text= "First name:", 
                                      style="Custom.TLabel", background="#EEEEEE")
    
    # last name
    self.last_name_label = ttk.Label(self.frame, text= "Last name:", 
                                     style="Custom.TLabel", background="#EEEEEE")
    
    # Address
    self.address_label = ttk.Label(self.frame, text="Address:", 
                                   style="Custom.TLabel", background="#EEEEEE")
    
    # Mobile number
    self.mobile_number_label = ttk.Label(self.frame, text="Mobile number", 
                                         style="Custom.TLabel", background="#EEEEEE")
  

    # Label positions
    self.first_name_label.grid(row=3, column=0, sticky="w", padx=10, pady=6 )
    self.last_name_label.grid(row=4, column=0, sticky="w", padx=10, pady=6 )
    self.address_label.grid(row=5, column=0, sticky="w", padx=10, pady=6 )
    self.mobile_number_label.grid(row=6, column=0, sticky="w", padx=10, pady=6 )
    
  def initialize_entry_widgets(self):
    """Initialize entry widgets"""

    # Define variables for each entry
    self.first_name = tk.StringVar()
    self.last_name = tk.StringVar()
    self.address = tk.StringVar()
    self.mobile_number = tk.StringVar()
    
    # First name
    self.first_name_entry = ttk.Entry(self.frame, width=30, 
                                      textvariable=self.first_name)

    # Last name
    self.last_name_entry = ttk.Entry(self.frame, width=30, 
                                     textvariable=self.last_name)
    
    # Address
    self.address_entry = ttk.Entry(self.frame, width=30, 
                                   textvariable=self.address)

    # # Mobile number
    self.mobile_number_entry = ttk.Entry(self.frame, width=30, 
                                         textvariable=self.mobile_number)

    # Entry positions
    self.first_name_entry.grid(row=3, column=1, sticky="e", padx=0, pady=5 )
    self.last_name_entry.grid(row=4, column=1, sticky="e", padx=0, pady=5 )
    self.address_entry.grid(row=5, column=1, sticky="e", padx=0, pady=5 )
    self.mobile_number_entry.grid(row=6, column=1, sticky="e", padx=0, pady=5 )

  # Get customers first name
  def get_first_name(self):
    """ Get the first name entered by the user """

    first_name = self.first_name_entry.get().title().rstrip().lstrip()

    if not first_name: 
      return None
    
    return first_name
  
  # Get customers last name
  def get_last_name(self):
    """ Get the last name entered by the user """
    
    last_name = self.last_name_entry.get().title().rstrip().lstrip()

    if not last_name:
      return None

    return last_name
  
  # Get customers address
  def get_address(self):
    """ Get the address entered by the user """

    address = self.address_entry.get().title().rstrip().lstrip()

    if not address:
      return None
   
    return address
  
  # Get customers mobile number
  def get_mobile_number(self):
    """ Get the mobile number entered by  the user """

    mobile_number = self.mobile_number_entry.get().rstrip().lstrip().strip("+")

    if not mobile_number:
      return None
    
    return mobile_number
   
   # Clear entry
  def reset(self):
      """Reset all entry fields"""

      self.first_name_entry.delete(0, tk.END)
      self.last_name_entry.delete(0, tk.END)
      self.address_entry.delete(0, tk.END)
      self.mobile_number_entry.delete(0, tk.END)
