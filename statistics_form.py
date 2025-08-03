# BIT502, SHEKINAH JOY CANOSA, 5075645, ASSESSMENT 3
""" Statistics Form file"""

# Import necessary modules for creating the application
import tkinter as tk
from tkinter import ttk
import sqlite3

from header import ApplicationHeader
from menu import Menu

class StatisticsForm(tk.Tk):
  def __init__(self, master=None):
    super().__init__(master)
    '''This class represents the main window of statistics form application'''

    self.title("City Gym Statistics Form")
    self.add_icon() 
    self.initialize_classes()
    self.initialize_member_treeview()
    self.initialize_totals_treeview()
    self.show_data()
    self.show_totals_data()

  def add_icon(self):   
      """Add an icon to the application window"""

      try:
          # If the image fails to load, ensure that the entire directory containing the gymicon_KxF_icon.ico image is  provided
          icon = "images/gymicon_KxF_icon.ico" 
          self.iconbitmap(icon)

      except Exception as e: 
          # Handle the error if loading the icon fails
          print("Error loading icon:", e) 

  def initialize_classes(self):
      """This method initializes instances of the application header and menu"""

      self.header = ApplicationHeader(self)
      self.menu = Menu(self)

      self.menu.statistics_form_help_button()

  def connect_database(self):
      """This method connects the application to the database"""

      # Connect to database
      self.conn = sqlite3.connect('gym_database.db')
      # Create a database cursor
      self.cursor = self.conn.cursor()

  def initialize_member_treeview(self):
      """This method is responsible for setting up the Treeview widget that will be used to display member records"""
     
      # Create frame to store Treeview widget widget and scrollbar
      self.frame = ttk.Frame(self, padding=10)

      # Defiene column names
      self.columns = ("First Name", "Last Name", "Membership Type",  "Extra 1", "Extra 2", "Extra 3", "Extra 4", "Direct Debit",)

      # Treeview widget
      self.tree = ttk.Treeview(self.frame, columns= self.columns, show="headings")

      # Configure column headings
      self.tree.heading("First Name", text="First Name")
      self.tree.heading("Last Name", text="Last Name")
      self.tree.heading('Membership Type', text='Membership Type')
      self.tree.heading('Extra 1', text='24/7 Access')
      self.tree.heading('Extra 2', text='Personal Trainer')
      self.tree.heading('Extra 3', text='Diet Consultation')
      self.tree.heading('Extra 4', text='Access Online Fitness Video')
      self.tree.heading('Direct Debit', text='Direct Debit')

      # Set column widths
      self.tree.column("First Name", width=100)
      self.tree.column("Last Name", width=100)
      self.tree.column("Membership Type", width=261, anchor=tk.CENTER)   
      self.tree.column("Extra 1", width=120, anchor=tk.CENTER)
      self.tree.column("Extra 2", width=130, anchor=tk.CENTER)
      self.tree.column("Extra 3", width=135, anchor=tk.CENTER)
      self.tree.column("Extra 4", width=190, anchor=tk.CENTER)
      self.tree.column("Direct Debit", width=100, anchor=tk.CENTER)

      # Cofigure row tag for alternating colors
      self.tree.tag_configure("evenrow", background="#FFA842")
      self.tree.tag_configure("oddrow", background="#FCD299")
      
      # Scrollbar
      self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
      self.tree.configure(yscroll= self.scrollbar.set)

      # Widgets positions
      self.frame.grid(row=3, column=0, columnspan=2, sticky= "wn")
      self.tree.grid(row=1,column=0,  columnspan=2, sticky="nsew", padx=2, pady=0)
      self.scrollbar.grid(row=1, column=2, sticky="ns")

  def initialize_totals_treeview(self):
      """This method is responsible for setting up the total Treeview widget that will be used to display total statistics"""
      
      self.totals_frame = ttk.Frame(self, padding=10)

      self.style = ttk.Style()
      self.style.configure("Custom.Treeview", background="white", foreground="black", font=("", 9))

      # Defiene column names
      self.columns = ("Total Members", "Basic Total", 
                      "Regular Total", "Premium Total", 
                      "24/7 Access Total", 
                      "Personal Trainer Total", 
                      "Diet Consultation Total", 
                      "Access Online Fitness Video Total", 
                      "Direct Debit Total",)

      self.totals_tree = ttk.Treeview(self.totals_frame, columns=self.columns, show="headings", style="Custom.Treeview")
      self.totals_tree.configure(height=1)

      # Configure column headings
      self.totals_tree.heading("Total Members", text="Total Members")
      self.totals_tree.heading("Basic Total", text="Basic Total")
      self.totals_tree.heading("Regular Total", text="Regular Total")
      self.totals_tree.heading("Premium Total", text="Premium Total")
      self.totals_tree.heading("24/7 Access Total", text="24/7 Access Total")
      self.totals_tree.heading("Personal Trainer Total", text="Personal Trainer Total")
      self.totals_tree.heading( "Diet Consultation Total", text= "Diet Consultation Total")
      self.totals_tree.heading("Access Online Fitness Video Total", text="Access Online Fitness Video Total")
      self.totals_tree.heading("Direct Debit Total", text= "Direct Debit Total")

      # Set column widths
      self.totals_tree.column("Total Members", width=200, anchor=tk.CENTER)
      self.totals_tree.column("Basic Total", width=87, anchor=tk.CENTER)
      self.totals_tree.column("Regular Total", width=87, anchor=tk.CENTER)
      self.totals_tree.column("Premium Total", width=87, anchor=tk.CENTER)   
      self.totals_tree.column("24/7 Access Total", width=120, anchor=tk.CENTER)
      self.totals_tree.column("Personal Trainer Total", width=130, anchor=tk.CENTER)
      self.totals_tree.column("Diet Consultation Total", width=135, anchor=tk.CENTER)
      self.totals_tree.column("Access Online Fitness Video Total", width=190, anchor=tk.CENTER)
      self.totals_tree.column("Direct Debit Total", width=100, anchor=tk.CENTER)

      # Configure row tag 
      self.totals_tree.tag_configure("evenrow", background="#FDB44E")

      # Widgets positions
      self.totals_frame.grid(row=4, column=0, columnspan=2, sticky= "wn")
      self.totals_tree.grid(row=1,column=0,  columnspan=2, sticky="nsew", padx=2, pady=0)

  def show_data(self):
      """This method displays all member in the Treeview"""

      # Connect to the database
      self.connect_database()

      self.query = "SELECT First_Name, Last_Name, Membership_Type, Extra_1,  Extra_2, Extra_3, Extra_4, Direct_Debit FROM Memberships"
      self.cursor.execute(self.query)
      self.records = self.cursor.fetchall()

      # Insert data to the Treeview 
      for i, row in enumerate(self.records):
          tag = 'evenrow' if i % 2 == 0 else 'oddrow'
          self.tree.insert("", "end", values=row, tags=(tag,))

      self.conn.close() # Close database connection

  def show_totals_data(self):
     """This method displays the calculated totals in the totals Treeview"""
     
     # Connect to the dataabase
     self.connect_database()

     total_members = self.count_total_members()
     basic_members = self.count_records_by_membership_type("Basic")
     regular_members = self.count_records_by_membership_type("Regular")
     premium_members = self.count_records_by_membership_type("Premium")
     extra1_members = self.count_records_by_debit_and_extras("Extra_1")
     extra2_members = self.count_records_by_debit_and_extras("Extra_2")
     extra3_members = self.count_records_by_debit_and_extras("Extra_3")
     extra4_members = self.count_records_by_debit_and_extras("Extra_4")
     debit_members = self.count_records_by_debit_and_extras("Direct_Debit")

    # Insert data into Treeview
     self.totals_tree.insert("", "end", values=(
        total_members, basic_members, regular_members, premium_members, 
        extra1_members, extra2_members, extra3_members, extra4_members, 
        debit_members), tags=("evenrow",))
     
     self.conn.close() # Close database connection
     
   #========================================== Helper methods =========================================
  """ These methods execute specific database queries to 
      retrieve various counts needed for the totals Treeview. """
  
  def count_total_members(self):
     
      query = "SELECT COUNT(*) FROM Memberships"
      self.cursor.execute(query)
      return self.cursor.fetchone()[0]
  
  def count_records_by_membership_type(self, membership_type):
     
      query = "SELECT COUNT(*) FROM Memberships WHERE Membership_Type = ?"
      self.cursor.execute(query,(membership_type,))
      return self.cursor.fetchone()[0]
 
  def count_records_by_debit_and_extras(self, debit_extras):
     
      query = f"SELECT COUNT(*) FROM Memberships WHERE {debit_extras} = 1"
      self.cursor.execute(query)
      return self.cursor.fetchone()[0]
  
# Run application
if __name__ == "__main__":
    
    app = StatisticsForm()
    app.mainloop()