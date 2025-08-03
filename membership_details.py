import tkinter as tk
from tkinter import ttk

class MembershipDetails:
  def __init__(self, master):

    """A class for managing Membership details GUI"""
    
    self.master = master

    self.widgets_styles()
    self.create_widget_container()
    self.initialize_membership_plan_price()
    self.initialize_membership_plan_widgets()
    self.initialize_membership_duration_widgets()

  def widgets_styles(self):
    """ Change frame color, font, and font sizes, and radio button backround color"""

    self.style = ttk.Style()
    self.style.configure("Container.TFrame", background="#EEEEEE")
    self.style.configure("Label.TFrame", background="#FFA842")
    self.style.configure("Custom.TLabel", font=('Microsoft Sans Serif', 10))
    self.style.configure("Membership.TRadiobutton", background="#EEEEEE")

  def create_widget_container(self):
    """Create a container to display membership plan and membership duration widgets"""
   
    #Frames
    self.frame = ttk.Frame(self.master, style="Container.TFrame", width=40, height=25 )
    self.text_frame = ttk.Frame(self.frame, style="Label.TFrame", width=40, height=25)
    
    # Label
    self.membership_details = ttk.Label(self.text_frame, text="Membership Details", 
                                          background="#FFA842", foreground="white", 
                                          padding="1", style="Custom.TLabel")
    
     # Widgets Positions
    self.frame.grid(row=2, rowspan=2, column=0, sticky="nw", padx=20, pady=5)
    self.text_frame.grid(row=1, column=0,columnspan=3, sticky="w", padx=5, pady=5)
    self.membership_details.grid(row=0, columnspan=5, sticky="w", padx=100, pady=0)
    
  #========================================== Membership paln =========================================
  def initialize_membership_plan_widgets(self):
    """Initialize membership plan widgets for selecting an option"""

    self.membership_plan = ttk.Label(self.frame, text="Membership Plan")

    # Define a variable for membership plan
    self.membership_plans = tk.StringVar()

    # Radiobutton list for membership plan (Basic, Regular, Premium)
    self.membership_plan_radiobuttons = [ 
        ttk.Radiobutton(self.frame, text="Basic", variable=self.membership_plans, 
                        value="Basic", style="Membership.TRadiobutton"),
        ttk.Radiobutton(self.frame, text="Regular", variable=self.membership_plans, 
                        value="Regular", style="Membership.TRadiobutton"),
        ttk.Radiobutton(self.frame, text="Premium", variable=self.membership_plans, 
                        value="Premium", style="Membership.TRadiobutton")]
   
   # Positions
    self.membership_plan.grid(row=2, column=0, sticky="w", padx=10, pady=10)
    for i,radiobutton in enumerate(self.membership_plan_radiobuttons):
      radiobutton.grid(row=i +3,column=0, sticky="w", padx=5, pady=7  )

  def initialize_membership_plan_price(self):

      self.membership_plan_prices = [ttk.Label(self.frame, text= "$10"),
                                     ttk.Label(self.frame, text= "$15"),
                                     ttk.Label(self.frame, text= "$20")
                                     ]

      for i, label in enumerate(self.membership_plan_prices):
        label.grid(row= i +3, column=0, sticky="w", padx=85,pady=10)

  #========================================== Membership duration =========================================
  def initialize_membership_duration_widgets(self):
    """Initialize membership duration widgets for selecting an option"""
  
    self.membership_duration = ttk.Label(self.frame, text="Membership Duration")

    # Define varible for membership duration
    self.membership_durations = tk.StringVar()
    
    self.membership_duration_radiobuttons = [

      ttk.Radiobutton(self.frame, text="3 Months",
                      variable=self.membership_durations,
                      value= "3 Months", style="Membership.TRadiobutton"),

      ttk.Radiobutton(self.frame, text="6 Months",
                      variable=self.membership_durations, 
                      value= "6 Months",  style="Membership.TRadiobutton"),

      ttk.Radiobutton(self.frame, text="12 Months",
                      variable=self.membership_durations, 
                      value= "12 Months",  style="Membership.TRadiobutton")
      ]
   
   # Positions
    self.membership_duration.grid(row=6, column=0, sticky="w", padx=10, pady=10)
    for i,radiobutton in enumerate(self.membership_duration_radiobuttons):
      radiobutton.grid(row=i +7,column=0, sticky="w", padx=5, pady=7  )

  def get_membership_details(self):
      """Get the membership details selected by the user"""
      
      membership_details = ""

      membership_plan = self.membership_plans.get()
      membership_duration = self.membership_durations.get()


      membership_details = f"{membership_plan}\n"
      membership_details += f"{membership_duration}\n"

      return( membership_details)
  
  def get_plan(self):

    membership_plan = ""

    plan = self.membership_plans.get()

    membership_plan = plan

    return membership_plan

  def get_duration(self):

      membership_duration = ""

      duration = self.membership_durations.get()

      membership_duration = duration

      return membership_duration

  def get_membership_plan(self):
    """Get the price of the selected membership plan"""

    membership_plan = self.membership_plans.get()
    
    if membership_plan == "":
      base_membership_cost = None
    elif membership_plan == "Basic":
      base_membership_cost = 10
    elif membership_plan == "Regular":
      base_membership_cost = 15
    elif membership_plan == "Premium":
      base_membership_cost = 20
    else:
      base_membership_cost = None

    return base_membership_cost
  
  # Get the discount of selected membership duration
  def get_membership_duration(self):   
    """Get the discount of the  selected membership duration selected by the user"""

    membership_duration = self.membership_durations.get()

    if  membership_duration == "":
      discount = None
    elif membership_duration == "3 Months":
      discount = 0
    elif membership_duration == "6 Months":
      discount = 2
    elif membership_duration == "12 Months":
      discount = 5
    else:
      discount = None

    return discount
  
  def reset(self):
      """Reset membership details"""
      self.membership_plans.set(None)
      self.membership_durations.set(None)
      
      
    