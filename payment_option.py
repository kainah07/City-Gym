# BIT502, SHEKINAH JOY CANOSA, 5075645, ASSESSMENT 3
"""Separete file for payment option"""

# Import necessary modules
import tkinter as tk
from tkinter import ttk

class PaymentOption:
  def __init__(self, master):
    """A class for managing Payment option GUI"""

    self.master = master
    self.widgets_styles()
    self.create_widget_container()
    self.initialize_paymentt_method()
    self.initialize_payment_frequency()

  def widgets_styles(self):
    """ Change frame color, font, font sizes, and radio button backround color"""
    
    self.style = ttk.Style()
    self.style.configure("Container.TFrame", background="#EEEEEE")
    self.style.configure("Label.TFrame", background="#FFA842")
    self.style.configure("Custom.TLabel", font=('Microsoft Sans Serif', 10))
    self.style.configure("PaymentOption.TRadiobutton", background="#EEEEEE")

  def create_widget_container(self):
    """Create a container to display direct debit and payment frequency widgets"""

    self.frame = ttk.Frame(self.master, style="Container.TFrame", width=40, height=25 )
    self.text_frame = ttk.Frame(self.frame, style="Label.TFrame", width=40, height=25)

    self.payment_option = ttk.Label(self.text_frame, text="Payment option", 
                                          background="#FFA842", foreground="white", 
                                          padding="1", style="Custom.TLabel")
    
    # Widgets positions
    self.frame.grid(row=2, column=1, sticky="ne", padx=20, pady=5)
    self.text_frame.grid(row=1, column=0,columnspan=3, sticky="w", padx=5, pady=5)
    self.payment_option.grid(row=0, columnspan=5, sticky="w", padx=115, pady=0)

  #========================================== Direct debit =========================================  
  def initialize_paymentt_method(self):
    """Initialize payment method check button widget"""

    self.direct_debit_checked = tk.BooleanVar()
    self.direct_debit = ttk.Checkbutton(self.frame, text= "Direct debit", variable=self.direct_debit_checked)

    self.direct_debit.grid(row=2,column=0, sticky="w", padx=5,pady=10)

  #========================================== Payment frequency =========================================
  def initialize_payment_frequency(self):
    """Initialize widgets for payment frequency"""

    # Payment frequency
    self.payment_frequency_label = ttk.Label(self.frame, text="Payment frequency")

    # Define a value for payment frequency
    self.frequency = tk.StringVar() 

    # Frequency radiobuttons
    self.frequency_radiobottons = [
      ttk.Radiobutton(self.frame, text= "Weekly", variable= self.frequency, 
                      value="Weekly", style="PaymentOption.TRadiobutton"),
      ttk.Radiobutton(self.frame, text= "Monthly", variable= self.frequency, 
                      value="Monthly", style="PaymentOption.TRadiobutton")
      ]

    # Widgets positons
    self.payment_frequency_label.grid(row=3, column= 0, sticky= "w", padx=5, pady=10)
    for i, radiobutton in enumerate(self.frequency_radiobottons):
      radiobutton.grid(row=i +5,column=0, sticky="w", padx=5, pady=5)

  def payment_method(self):
    """Get the selected payment method selected by the use to save in the text file"""
      
    if self.direct_debit_checked.get():
          payment_method = True
    else:
          payment_method = False

    return payment_method
  
  def payment_frequency(self):
     
     payment_frequency = self.frequency.get()

     return payment_frequency
     
  def get_direct_debit(self):
     """Get the payment method selected by the user"""
     
     direct_debit = self.direct_debit_checked.get() 
     return direct_debit

  def get_payment_frequency(self, net_cost= None):
    """Get the selected payment frequency selected by the user"""

    frequency = self.frequency.get()
    regular_payment = 0

    if frequency == "":
      return None        # The funtion will return none to indicate a payment frequency is not yet chosen
    elif frequency == "Weekly":
        regular_payment = net_cost
    elif frequency == "Monthly":
        regular_payment = net_cost * 4  
    else:
        regular_payment = None  # Return None if the payment frequency is neither "Weekly" nor "Monthly"

    return regular_payment
        
  def reset(self):
        """Reset payment option check button and radio button"""
        self.direct_debit_checked.set(0)
        self.frequency.set(None)
       