""" Main Menu file"""

# Import necessary modules for creating the application
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import os

from header import MainMenuHeader

class MainMenu(tk.Tk):
  def __init__(self):
    super().__init__()
    """ Main Menu for the City Gym Application """

    self.add_icon()
    self.title("City Gym Main Menu")
    self.header = MainMenuHeader(self)
    self.initialize_top_menu_buttons()
    self.initialize_navigation_buttons()

  def add_icon(self):
      """Add an icon to the application window"""

      try:
          # If the image fails to load, ensure that the entire directory containing the gymicon_KxF_icon.ico image is  provided
          icon = "images/gymicon_KxF_icon.ico" 

          self.iconbitmap(icon)

      except Exception as e:
          # Handle the error if loading the icon fails
          print("Error loading icon:", e) 

  def initialize_navigation_buttons(self):
      """ Buttons to navigate each forms of the Application """

      style = ttk.Style()
      style.configure('Button.TButton', foreground='black', width=30, font=('', 15))

      self.button_container = ttk.Frame(self.master, padding=20)
      self.button_container.grid(row= 4, column=0, sticky="n", columnspan=3, padx=9, pady=100)

      self.open_registration_form = ttk.Button(self.button_container, text= "Membership form", style="Button.TButton", padding=5, command=self.open_membership_form)
      self.search_form = ttk.Button(self.button_container, text= "Search form", style="Button.TButton", padding=5, command=self.open_search_form)
      self.statistics_form = ttk.Button(self.button_container, text= "Statistics form", style="Button.TButton", padding=5, command=self.open_statistics_form)

      self.open_registration_form.grid(row= 5, column= 0, columnspan=3, sticky="n", padx=20, pady=15)
      self.search_form.grid(row= 6, column= 0, columnspan=3, sticky="n", padx=20, pady=15)
      self.statistics_form.grid(row= 7, column= 0, columnspan=3, sticky="n", padx=20, pady=15)
    
  def initialize_top_menu_buttons(self):
      """ Buttons to open the Help screen and close the application """
     
      style = ttk.Style()
      style.configure('Menu.TButton', foreground='black',  background="#FFA500")
      style.configure("Frame.TFrame", background="#FFA842")

      self.button_frame = ttk.Frame(self.master, width=45, height=50, style="Frame.TFrame")
      self.button_frame.grid(row=0, column=0, columnspan=5, sticky="e", padx=20, pady=0)

      self.about = ttk.Button(self.button_frame, text= "Help", style= "Menu.TButton", command=self.open_help_screen)
      self.about.grid(row=0, column= 1, sticky="w", padx=10, pady=0)
      self.exit = ttk.Button(self.button_frame, text= "Exit", style= "Menu.TButton", command= self.close_application)

      self.exit.grid(row=0, column= 2, sticky="w", padx=10, pady=0)
     
  def open_membership_form(self):
      """ Navigate to the  Memnership Form"""

      self.destroy() # Close main menu window
    
      # Ensure the path to the membership form script ('membership_form.py') is correct.
      membership_form_path = "membership_form.py"

      # Check if the file exists
      if not os.path.exists(membership_form_path):
          messagebox.showerror("Error opening Membership Form", 
                               f"Error: The file at {membership_form_path} does not exist. \nEnsure the path to the membership form script ('membership_form.py') is correct ")
          return None
      
      # Execute the membership form script using subprocess
      subprocess.run(["python", membership_form_path])

  def open_search_form(self):
      """ Navigate to the  Search Form """
    
      self.destroy()

      # Ensure the path to the search form script ('search_form.py') is correct.
      search_form_path = "search_form.py"

      if not os.path.exists(search_form_path):
          messagebox.showerror("Error opening Search Form", 
                               f"Error: The file at {search_form_path} does not exist. \nEnsure the path to the search form script ('search_form.py') is correct ")
          return None

      subprocess.run(["python", search_form_path])

  def open_statistics_form(self):
      """ Navigate to the  Statistics Form """
     
      self.destroy()
    
      # Ensure the path to the statistics form script ('statistics_form.py') is correct.
      statistics_form_path =  "statistics_form.py" 

      if not os.path.exists(statistics_form_path):
          messagebox.showerror("Error opening Statistics Form", 
                               f"Error: The file at {statistics_form_path} does not exist. \nEnsure the path to the statistics form script ('statistics_form.py') is correct ")
          return None

      subprocess.run(["python", statistics_form_path])
     
  def close_application(self):
      """ Exits the application after the user confirmation """

      confirm_exit = messagebox.askyesno("Exit application", "Are you sure you want to exit Application?")
      if confirm_exit:
        exit()

  def initialize_help_screen(self, help_message):
      """ Initialize the help screen with porvided help message """
      
       # Create a Help screen
      self.help_screen = tk.Toplevel(self.button_frame)
      self.help_screen.title("Help")
      self.help_screen.resizable(False, False)

      # Display information about the application
      self.help_label = ttk.Label(self.help_screen, text=help_message)
      self.about_label = ttk.Label(self.help_screen, text= "About this program: City Gym Application")
      self.version_label = ttk.Label(self.help_screen, text="Version 1.0")
      self.app_developer_label = ttk.Label(self.help_screen, text= "Developer: Shekinah Joy Canosa")

      # Create ok button
      self.ok_button = ttk.Button(self.help_screen, text= "OK", command= self.help_screen.destroy)

      # Positions
      self.help_label.grid(row=0, column=0, sticky="n", padx=10, pady=10)
      self.about_label.grid(row=1, column=0, sticky="n", padx=10, pady=10)
      self.version_label.grid(row=3, column=0, sticky="n", padx= 10, pady=1)
      self.app_developer_label.grid(row=4, column=0, sticky="n", padx= 10, pady=1)
      self.ok_button.grid(row=5, column=0, sticky="n", padx= 10, pady=10)        
  
  def open_help_screen(self):
      """ Displays the help screen for the Main Menu """

      # Help screen content
      help_message = (
          "Help Information:\n\n"
          "Welcome to the application Main Menu. Here is how you can use this application:\n\n"
          "1. Membership Form:\n"
          "   - Click the 'Membership Form' button to open the membership registration form where you can enter details to sign up for a gym membership.\n\n"
          "2. Search Form:\n"
          "   - Click the 'Search Form' button to open the search form where you can search for existing members.\n\n"
          "3. Staristics Form:\n"
          "   - Click the 'Statistics Form' button to open the statistics form that displays various statistics about gym memberships.\n\n"
          "4. Help Screen:\n"
          "   - Click the 'Help' button to display a help screen with information on how to use the application.\n"
          "   - For additional support, contact our support team at customerservice@citygym.com.\n\n"
          "5. Exit:\n"
          "   - Click the 'Exit' button to close the application.\n\n"
          "If you encounter any issues or have any questions, please contact our support team at customerservice@citygym.com."
      )

      self.initialize_help_screen(help_message)
     
# Run application
if __name__ == "__main__":
    
    app = MainMenu()
    app.mainloop()