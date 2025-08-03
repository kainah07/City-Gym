""" Main file for City Gym Membership Application Form"""

import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Import custom modules for the application
from header import ApplicationHeader
from customers_details import  CustomersDetails
from membership_details import MembershipDetails
from optional_extras import OptionalExtras
from payment_option import PaymentOption
from calculate_total import CalculateTotal 
from gym_database import GymDataBase
from menu import Menu

class MembershipForm(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        """ Main class for managing the City Gym Membership Application Form GUI  """

        self.title("City Gym Membership Form")
        self.add_icon()
        self.initialize_classes()
        self.initialize_buttons()
        
    def add_icon(self):

        try:
            # If the image fails to load, ensure that the entire directory containing the gymicon_KxF_icon.ico image is  provided
            icon = "images/gymicon_KxF_icon.ico" 

            self.iconbitmap(icon)

        except Exception as e:
            # Handle the error if loading the icon fails
            print("Error loading icon:", e) 

    def initialize_classes(self):
        """Initialize instances for managing different sections of the appliations."""

        self.header = ApplicationHeader(self)
        self.customer_details = CustomersDetails(self)
        self.membership_details = MembershipDetails(self)
        self.extras = OptionalExtras(self)
        self.payment_option = PaymentOption(self) 
        self.calculate_widgets = CalculateTotal(self, self.membership_details, self.extras, self.payment_option)
        self.gym_data = GymDataBase(self)
        self.menu = Menu(self)
                      
    def initialize_buttons(self):
        """Initialzed buttons for submitting and resetting the form"""

        style = ttk.Style()
        # Define the style for the view discount button
        style.configure('Button.TButton', foreground='black', width=15, font=('', 8))

        # Initialize help button from Menu
        self.menu.membership_from_help_button()

        self.button_container = ttk.Frame(self.master)

        # Submit membership
        self.submit_button = ttk.Button(self.button_container, text="Submit", 
                                        command=self.submit)

        # Clear form
        self.reset_button = ttk.Button(self.button_container, text="Reset Buttons", 
                                        command=self.confirm_reset)

        # Button positions
        self.button_container.grid(row= 4, column=0, sticky="w", padx=9, pady=10)
        self.submit_button.grid(row= 1, column=0, sticky="w", padx=20, pady=5)
        self.reset_button.grid(row= 1, column=1, sticky="w", padx=10, pady=5)

    def reset_form(self):
        """Reset all form fields"""

        self.customer_details.reset()
        self.membership_details.reset()
        self.extras.reset()
        self.payment_option.reset()
        self.calculate_widgets.reset()
    
    def confirm_reset(self):
         """Prompt the user to confirm clearing the all fields"""

         confirm_reset = messagebox.askyesno("Confirm clearing all fields", "Are you sure you want to clear all fields?")

         if confirm_reset:      # Clears all fields
              self.reset_form()

    # Submit application
    def submit(self):
        """
        Validate form data and save to a tect file
        """

        first_name = self.customer_details.get_first_name()
        last_name = self.customer_details.get_last_name()
        address = self.customer_details.get_address()
        mobile_number  = self.customer_details.get_mobile_number()

        membership_plan = self.membership_details.get_plan()
        membership_duration = self.membership_details.get_duration()

        payment_method = self.payment_option.payment_method()
        payment_frequency = self.payment_option.payment_frequency()

        extra1 = self.extras.get_twenty_four_access()
        extra2 = self.extras.get_personal_trainer()
        extra3 = self.extras.get_diet_consultation()
        extra4 = self.extras.get_access_online_video()
        
         # Check for  empty fields
        if (not first_name) or (not last_name) or (not address) or (not mobile_number) :
            messagebox.showerror("Error", "Please fill all fields")
            return False
        
        # Validate first name 
        if any(name.isdigit() for name in first_name):
            messagebox.showerror("Invalid name input", "Please enter alphabetic characters only.")
            return False
        
        elif not all(name.isalpha() or (name.isspace()) for name in first_name):
             messagebox.showerror("Invalid name input", "Please enter alphabetic characters only.")
             return False

        # Validate last name 
        if  any(name.isdigit() for name in last_name) :
            messagebox.showerror("Invalid name input", "Please enter alphabetic characters only.")
            return False
        
        elif not all(name.isalpha() or (name.isspace()) for name in last_name):
             messagebox.showerror("Invalid name input", "Please enter alphabetic characters only.")
             return False
        
         # Validate mobile number
        if not mobile_number.isdigit():
            messagebox.showerror("Error", "Invalid mobile number")
            return False
        
        elif len(mobile_number ) != 10:
             messagebox.showerror("Error", "Invalid mobile number: must 10 digits long")
             return False
                   
        # Format customers details 
        customers_details = f"First name: {first_name }\nLast name: {last_name}\nAddress: {address}\nMobile number: {mobile_number}\n"
        
        # Check if totals calculated
        if not self.calculate_widgets.calculated:
            messagebox.showerror("Error", "Please calculate the program before submitting.")
            return None

        calculated_totals = self.calculate_widgets.calculate_totals(from_submit= True)
        
        # Check if all required option is selected
        if not calculated_totals:
            messagebox.showerror("Error", "Some required values are missing.")
            return

        # Show confirmation message with customers details and calculated total membership cost
        confirm = messagebox.askyesno("Confirm details",f"Please confirm membership details: \n\n{customers_details}\n{calculated_totals}\n")
 
        # Save members data to gym database
        if confirm:
                self.gym_data.insert_new_member(first_name, 
                                                last_name, address, 
                                                mobile_number, 
                                                membership_plan, 
                                                membership_duration, 
                                                payment_method, 
                                                extra1, 
                                                extra2, 
                                                extra3, 
                                                extra4, 
                                                payment_frequency)
                
                time.sleep(1.1)  # Delay succes mesaage notification
                messagebox.showinfo("Success", "Membership saved succesfully!") # Message indicating members data is saved successfuly
                self.reset_form()

# Run application
if __name__ == "__main__":
    
    app = MembershipForm()
    app.mainloop()
