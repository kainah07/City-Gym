# BIT502, SHEKINAH JOY CANOSA, 5075645, ASSESSMENT 3
"""Menu file for all Application Forms"""

# Import necessary modules for creating the application
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox 
import subprocess
import os

class Menu(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    """  Class for managing the top navigation for City Gym application forms, providing options for Main Menu, Help, and Exit. """

    self.master = master
    self.initialize_menu()

  def initialize_menu(self):
      """ Exit and Main Menu navigation option """

      style = ttk.Style()
      style.configure('Menu.TButton', foreground='black',  background="#FFA500")
      style.configure("Frame.TFrame", background="#FFA842")

      self.button_frame = ttk.Frame(self.master, width=45, height=50, style="Frame.TFrame")
      self.button_frame.grid(row=0, column=0, columnspan=2, sticky="e", padx=20, pady=0)

      self.main_menu = ttk.Button(self.button_frame, text= "Main Menu", style= "Menu.TButton", command= self.open_main_menu)
      self.exit = ttk.Button(self.button_frame, text= "Exit", style= "Menu.TButton", command= self.close_application)

      self.main_menu.grid(row=0, column= 0, sticky="w", padx=10, pady=0)
      self.exit.grid(row=0, column= 2, sticky="w", padx=10, pady=0)

  def open_main_menu(self):
      """ Navigate to the main menu """
      
      self.master.destroy()

      # Ensure the path to the main menu script ('main_menu.py') is correct.
      file_path = "main_menu.py"
      
      # Check if the file exists
      if not os.path.exists(file_path):
          messagebox.showerror("Error opening Main Menu", 
                               f"Error: The file at {file_path} does not exist. \nEnsure the path to the main menu script ('main_menu.py') is correct ")
          return None
 
      # Execute the main menu script using subprocess
      subprocess.run(["python", file_path])

  # Exit app
  def close_application(self):
      """ Exits the application after the user confirmation """

      confirm_exit = messagebox.askyesno("Exit application", "Are you sure you want to exit membership form?")
      if confirm_exit:
          exit()

  #========================================== Help buttons =========================================
  """ These methods creates Help buttons ffor the application. Each buttons has different instructions, which is why they are created seperately """

  def membership_from_help_button(self):
      """ Help button for Membership Form """

      self.about = ttk.Button(self.button_frame, text= "Help", style= "Menu.TButton", command=self.open_help_screen_membership_form)
      self.about.grid(row=0, column= 1, sticky="w", padx=10, pady=0)

  def search_form_help_button(self):
      """ Help button for Search Form """

      self.about = ttk.Button(self.button_frame, text= "Help", style= "Menu.TButton", command=self.open_help_screen_search_form)
      self.about.grid(row=0, column= 1, sticky="w", padx=10, pady=0)
      
  def statistics_form_help_button(self):
      """ Help button for Statistics Form """

      self.about = ttk.Button(self.button_frame, text= "Help", style= "Menu.TButton", command=self.open_help_screen_statistics_form)
      self.about.grid(row=0, column= 1, sticky="w", padx=10, pady=0)

  def initialize_help_screen(self, help_message):
      """ Initialize the help screen with provided help message """
      
      
      self.help_screen = tk.Toplevel(self.button_frame)
      self.help_screen.title("Help")
      self.help_screen.resizable(False, False)

      # Display information about the application
      self.help_label = ttk.Label(self.help_screen, text=help_message)
      self.about_label = ttk.Label(self.help_screen, text= "About this program: City Gym Application")
      self.version_label = ttk.Label(self.help_screen, text="Version 1.0")
      self.app_developer_label = ttk.Label(self.help_screen, text= "Developer: Shekinah Joy Canosa")

      # Ok button
      self.ok_button = ttk.Button(self.help_screen, text= "OK", command= self.help_screen.destroy)

      # Positions
      self.help_label.grid(row=0, column=0, sticky="n", padx=10, pady=10)
      self.about_label.grid(row=1, column=0, sticky="n", padx=10, pady=10)
      self.version_label.grid(row=3, column=0, sticky="n", padx= 10, pady=1)
      self.app_developer_label.grid(row=4, column=0, sticky="n", padx= 10, pady=1)
      self.ok_button.grid(row=5, column=0, sticky="n", padx= 10, pady=10)

  """ Methods providing informtion on how to use the application """

  def open_help_screen_membership_form(self):     
      """ Displays the help screen for the Membership Form """

      membership_form_instruction = (
            "Help Information:\n\n"
            "Welcome to the Membership Registration application. Here is how you can use this application:\n\n"
            "1. Main Menu:\n"
            "   - Navigate through the different sections of the application using the main menu.\n\n"
            "2. Registration:\n"
            "   - Fill in your personal details including name, contact information, and membership preferences.\n"
            "   - Ensure all mandatory fields are completed before submitting the form.\n\n"
            "3. Sign up discounts:\n"
            "   - Sign up for a 6 months contract to recieve a $2 per week discount on any membership type.\n"
            "   - Sign up for 12 months to recieve a $5 per week discount on any membership type.\n"
            "   - For direct debit, there is a 1% discount on the base membership cost\n\n"
            "4. Submission:\n"
            "   - After filling in the details, click the 'Submit' button to complete your registration.\n"
            "   - You will receive a confirmation message once the registration is successful.\n\n"
            "5. Help:\n"
            "   - Click the 'Help' button in the menu to view this help screen.\n"
            "   - For additional support, contact our support team at customerservice@citygym.com.\n\n"
            "6. Exit:\n"
            "   - Click the 'Exit' button to close the application.\n\n"
            "If you encounter any issues or have any questions, please contact our support team at customerservice@citygym.com."
        )

      self.initialize_help_screen(membership_form_instruction)
      
  def open_help_screen_search_form(self): 
      """ Displays the help screen for the Search Form """

      search_form_instruction = (
            "Help Information:\n\n"
            "Welcome to the Statistics Form application. Here is how you can use this application:\n\n"
            "1. Main Menu:\n"
            "   - Navigate through the different sections of the application using the main menu.\n\n"
            "2. Search Form:\n"
            "   - Enter the Member ID, Last Name, or Membership Type in the corresponding fields.\n"
            "   - Click on the 'Search' button to find matching members.\n"
            "   - Results will be displayed in the table.\n\n"
            "3. Select a Member:\n"
            "   - To edit a member's details, click on the member's row in the table.\n"
            "   - Click the 'Select' button when a member is selected.\n"
            "   - The member's details will be displayed in the edit section.\n\n"
            "4. Edit Member Details:\n"
            "   - Modify the member's details in the edit section as needed.\n"
            "   - Click on the 'Save' button to update the changes.\n"
            "   - Click on the 'Cancel' button to cancel editing details.\n\n"
            "5. Help:\n"
            "   - Click the 'Help' button in the menu to view this help screen.\n"
            "   - For additional support, contact our support team at customerservice@citygym.com.\n\n"
            "6. Exit:\n"
            "   - Click the 'Exit' button to close the application.\n\n"
            "If you encounter any issues or have any questions, please contact our support team at customerservice@citygym.com."
        )

      self.initialize_help_screen(search_form_instruction)

  def open_help_screen_statistics_form(self):
      """ Displays the help screen for the Statistics Form """

      statistics_form_instruction = (
            "Help Information:\n\n"
            "Welcome to the Statistics Form application. Here is how you can use this application:\n\n"
            "1. Main Menu:\n"
            "   - Navigate through the different sections of the application using the main menu.\n\n"
            "2. Statistics Form:\n"
            "   - View members record.\n"
            "   - View overall statistics record.\n\n"
            "3. Help:\n"
            "   - Click the 'Help' button in the menu to view this help screen.\n"
            "   - For additional support, contact our support team at customerservice@citygym.com.\n\n"
            "4. Exit:\n"
            "   - Click the 'Exit' button to close the application.\n\n"
            "If you encounter any issues or have any questions, please contact our support team at customerservice@citygym.com."
        )

      self.initialize_help_screen(statistics_form_instruction)

