# BIT502, SHEKINAH JOY CANOSA, 5075645, ASSESSMENT 3
""" Search Form file"""

# Import necessary modules for creating the application
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import time

from header import ApplicationHeader
from menu import Menu

class SearchForm(tk.Tk):
  def __init__(self, master=None):
    super().__init__(master)
    '''This class represents the main window of search form application'''
    
    self.title("City Gym Search Form")
    self.add_icon()
    self.initialize_classes()
    self.widgets_styles()
    self.initialize_search_form_widgets()
    self.initialize_edit_form_widgets()
    self.initialize_treeview()
    self.show_data()
    
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

      self.menu.search_form_help_button()

  def connect_database(self):
      """This method connects the application to the database"""

      # Connect to database
      self.conn = sqlite3.connect('gym_database.db')
      # Create a database cursor
      self.cursor = self.conn.cursor()
      
  def search_members(self):
      """This method handles search functionality when the search button is clicked"""

      # Retrieve values entered in search form fields   
      self.member_id = self.member_id_var.get()
      self.last_name = self.last_name_var.get().lower()
      self.membership_type = self.membership_type_var.get()

      # Connect to database
      self.connect_database()

      # Construct a search queary that selects all members from the 'Memberships' table
      self.query = "SELECT * FROM Memberships WHERE 1=1" 

      # Add filter to the queary based on the provided search criteria
      self.params = []

      if self.member_id:
         self.query += " AND MemberID = ? "
         self.params.append(self.member_id)

      if self.last_name:
         self.query += " AND lower(Last_Name) LIKE ? "
         self.params.append(f'%{self.last_name}%')

      if self.membership_type:
         self.query += " AND  Membership_Type = ? "
         self.params.append(self.membership_type)

      # Execute the query
      self.cursor.execute(self.query, self.params)
      self.results = self.cursor.fetchall()

      # Close the database connection
      self.conn.close()

      # Clear the Treeview of any existing data
      for item in self.tree.get_children():
         self.tree.delete(item)

      # Insert results into treeview
      if self.results:
         # Insert results into Treeview with striped row colors for better readability
         for i, row in enumerate(self.results):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=row, tags=(tag,))

      else:
         messagebox.showerror("No Result", "No results found") #  Display a message if no results found 
         self.show_data()

  def widgets_styles(self):
      """ Change frame color, font, and font sizes, and radio button backround color"""

      self.style = ttk.Style()
      self.style.configure("Container.TFrame", background="#F5F5F5")
      self.style.configure("Label.TFrame", background="#D9D9D9")
      self.style.configure("Custom.TLabel", font=('Microsoft Sans Serif', 9))
      self.style.configure("Button.TButton", foreground='black',  background="#F5F5F5")
      self.style.configure("Membership.TRadiobutton", background="#F5F5F5")

  def initialize_search_form_widgets(self):
      """This method creates the visual components of the search form"""

      # Define variables 
      self.member_id_var = tk.StringVar()
      self.last_name_var = tk.StringVar()
      self.membership_type_var = tk.StringVar()

      # Create frame to store search fields and buttons
      self.form_frame = ttk.Frame(self, padding=10, style="Container.TFrame", relief="sunken")
      self.button_frame = ttk.Frame(self.form_frame, style="Container.TFrame")
      self.text_frame = ttk.Frame(self.form_frame, style="Label.TFrame")
      self.search = ttk.Label(self.text_frame, text="Search", 
                                          background="#D9D9D9", foreground="black", 
                                          style="Custom.TLabel")

      # Labels
      ttk.Label(self.form_frame, text= "Member ID:", background="#F5F5F5").grid(row=1,column=0, columnspan=2, sticky="w", padx=20, pady=10)
      ttk.Label(self.form_frame, text= "Last Name:", background="#F5F5F5").grid(row=2,column=0, columnspan=2, sticky="w", padx=20, pady=10)
      ttk.Label(self.form_frame, text= "Membership Type:", background="#F5F5F5").grid(row=3,column=0, columnspan=2, sticky="w", padx=20, pady=10)

      # Entry search fields
      self.member_id_entry = ttk.Entry(self.form_frame, textvariable= self.member_id_var, width=30)
      self.last_name_entry = ttk.Entry(self.form_frame, textvariable= self.last_name_var, width=30)


      # Combobox
      self.membership_type_box = ttk.Combobox(self.form_frame, textvariable=self.membership_type_var, width=27)
      self.membership_type_box["values"] = ("", "Basic", "Regular", "Premium")

      # Search button
      self.search_button = ttk.Button(self.button_frame, text= "Search", command=self.search_members, style="Button.TButton")
      self.clear_button = ttk.Button(self.button_frame, text= "Clear Search", command=self.clear_search_form, style="Button.TButton")
      self.select_button = ttk.Button(self.button_frame, text= "Select Member", command=self.select_record, style="Button.TButton")

      # Widgets positions
      self.form_frame.grid(row=3, column=0,  sticky= "w", padx= 50, pady=20) 
      self.button_frame.grid(row=4, column=0,  columnspan=3,  sticky= "w", padx=20, pady=10)
      self.text_frame.grid(row=0, column=0, columnspan=3, sticky="w", padx=5, pady=5)  
      self.search.grid(row=0, column=0,columnspan=3, sticky="w", padx=30, pady=5) 
      self.member_id_entry.grid(row=1, column=2, columnspan=2,  sticky="w", padx=20, pady=10)
      self.last_name_entry.grid(row=2, column=2, columnspan=2, sticky="w", padx=20, pady=10)
      self.membership_type_box.grid(row=3, column=2,  columnspan=2, sticky="w", padx=20, pady=10)
      self.search_button.grid(row=4,column=0, sticky="w", padx=2, pady=10)
      self.clear_button.grid(row=4,column=1, sticky="wn", padx=2, pady=10)
      self.select_button.grid(row=4,column=2, sticky="wn", padx=2, pady=10)

  def initialize_edit_form_widgets(self):
      
      # Label frame to store edit form elements
      self.edit_frame = ttk.Frame(self, style="Container.TFrame", padding=10, width=40, height=25, relief="sunken" )      
      self.text_frame = ttk.Frame(self.edit_frame, style="Label.TFrame")
      self.edit = ttk.Label(self.text_frame, text="Edit member record", 
                                          background="#D9D9D9", foreground="black", 
                                          style="Custom.TLabel")
      
      self.edit_frame.grid(row=3, column=1, sticky= "w", padx=20, pady=20)
      self.text_frame.grid(row=0, column=0, columnspan=3, sticky="w", padx=5, pady=5)
      self.edit.grid(row=0, column=0,columnspan=3, sticky="w", padx=30, pady=5)

      # Define variables
      self.edit_first_name_var = tk.StringVar()
      self.edit_last_name_var = tk.StringVar()
      self.edit_address_var = tk.StringVar()
      self.edit_mobile_var = tk.StringVar()
      self.edit_membership_type_var = tk.StringVar()
      self.edit_membership_duration_var = tk.StringVar()

      # Labels
      ttk.Label(self.edit_frame, text= "First Name:", background="#F5F5F5").grid(row=1,column=0, sticky="w", padx=20, pady=10)
      ttk.Label(self.edit_frame, text= "Last Name:", background="#F5F5F5").grid(row=2,column=0, sticky="w", padx=20, pady=10)
      ttk.Label(self.edit_frame, text= "Address:", background="#F5F5F5").grid(row=3,column=0, sticky="w", padx=20, pady=10)
      ttk.Label(self.edit_frame, text= "Mobile Number:", background="#F5F5F5").grid(row=4,column=0, sticky="w", padx=20, pady=10)
      ttk.Label(self.edit_frame, text= "Membership Type:", background="#F5F5F5").grid(row=1,column=2, columnspan=2, sticky="w", padx=20, pady=10)
      ttk.Label(self.edit_frame, text= "Membership Duaration:", background="#F5F5F5").grid(row=3,column=2, columnspan=2, sticky="w", padx=20, pady=10)

      # Edit entry's
      self.edit_first_name_entry = ttk.Entry(self.edit_frame, textvariable= self.edit_first_name_var, width=30, background="#F5F5F5")
      self.edit_last_name_entry = ttk.Entry(self.edit_frame, textvariable= self.edit_last_name_var, width=30, background="#F5F5F5")
      self.edit_address_entry = ttk.Entry(self.edit_frame, textvariable= self.edit_address_var, width=30, background="#F5F5F5")
      self.edit_mobile_number_entry = ttk.Entry(self.edit_frame, textvariable= self.edit_mobile_var, width=30, background="#F5F5F5")

      # Buttons
      self.save_button = ttk.Button(self.edit_frame, text= "Save", command=self.update_record, style="Button.TButton")
      self.cancel_button = ttk.Button(self.edit_frame, text= "Cancel", command=self.clear_edit_form, style="Button.TButton")
      
      # Radiobuttons for membership type
      self.membership_plan_radiobuttons = [ 
         ttk.Radiobutton(self.edit_frame, text="Basic", variable=self.edit_membership_type_var, 
                           value="Basic", style="Membership.TRadiobutton"),
         ttk.Radiobutton(self.edit_frame, text="Regular", variable=self.edit_membership_type_var, 
                           value="Regular", style="Membership.TRadiobutton"),
         ttk.Radiobutton(self.edit_frame, text="Premium", variable=self.edit_membership_type_var, 
                           value="Premium", style="Membership.TRadiobutton")]
      
      # Radiobuttons for membership duration
      self.membership_duration_radiobuttons = [
         ttk.Radiobutton(self.edit_frame, text="3 Months",
                        variable= self.edit_membership_duration_var,
                        value= "3 Months", style="Membership.TRadiobutton"),
         ttk.Radiobutton(self.edit_frame, text="6 Months",
                        variable= self.edit_membership_duration_var, 
                        value= "6 Months",  style="Membership.TRadiobutton"),
         ttk.Radiobutton(self.edit_frame, text="12 Months",
                        variable= self.edit_membership_duration_var, 
                        value= "12 Months",  style="Membership.TRadiobutton")]

      # Widgets positions
      self.edit_first_name_entry.grid(row=1,column=1, sticky="w", padx=20, pady=10)
      self.edit_last_name_entry.grid(row=2,column=1, sticky="w", padx=20, pady=10)
      self.edit_address_entry.grid(row=3,column=1, sticky="w", padx=20, pady=10)
      self.edit_mobile_number_entry.grid(row=4,column=1, sticky="w", padx=20, pady=10)
      self.save_button.grid(row=4,column=5, sticky="w", padx=10, pady=10)
      self.cancel_button.grid(row=4,column=6, sticky="w", padx=10, pady=10)

      for i,radiobutton in enumerate(self.membership_plan_radiobuttons):
         radiobutton.grid(row=2,column=i +2, sticky="w", padx=20, pady=10)

      for i,radiobutton in enumerate(self.membership_duration_radiobuttons):
               radiobutton.grid(row=4,column=i +2, sticky="w", padx=20, pady=10)   

  def initialize_treeview(self):
      """This method is responsible for setting up the Treeview widget that will be used to display member records"""

      self.tree_contaniner = ttk.Frame(self, padding=10)

      self.style = ttk.Style()
      self.style.configure("Custom.Treeview", background="white", foreground="black", font=("", 10))

      # Defiene column names
      self.columns = ("ID", "First Name", "Last Name", "Address", "Mobile Number", "Membership Type", "Membership Duration", "Direct Debit", "Extra 1", "Extra 2", "Extra 3", "Extra 4",
                        "Payment Frequency")

      # Create the Treeview widget
      self.tree = ttk.Treeview(self.tree_contaniner, columns= self.columns, show="headings", style="Custom.Treeview")

      # Configure column headings
      self.tree.heading('ID', text='ID')
      self.tree.heading('First Name', text='First Name')
      self.tree.heading('Last Name', text='Last Name')
      self.tree.heading('Address', text='Address')
      self.tree.heading('Mobile Number', text='Mobile Number')
      self.tree.heading('Membership Type', text='Membership Type')
      self.tree.heading('Membership Duration', text='Membership Duration')
      self.tree.heading('Direct Debit', text='Direct Debit')
      self.tree.heading('Extra 1', text='24/7 Access')
      self.tree.heading('Extra 2', text='Personal Trainer')
      self.tree.heading('Extra 3', text='Diet Consultation')
      self.tree.heading('Extra 4', text='Access Online Fitness Video')
      self.tree.heading('Payment Frequency', text='Payment Frequency')

      # Set column widths
      self.tree.column("ID", width=40, anchor=tk.CENTER)
      self.tree.column("First Name", width=100)
      self.tree.column("Last Name", width=100)
      self.tree.column("Address", width=200)
      self.tree.column("Mobile Number", width=100)
      self.tree.column("Membership Type", width=130)
      self.tree.column("Membership Duration", width=130)
      self.tree.column("Direct Debit", width=100, anchor=tk.CENTER)
      self.tree.column("Extra 1", width=100, anchor=tk.CENTER)
      self.tree.column("Extra 2", width=100, anchor=tk.CENTER)
      self.tree.column("Extra 3", width=100, anchor=tk.CENTER)
      self.tree.column("Extra 4", width=155, anchor=tk.CENTER)
      self.tree.column("Payment Frequency", width=125)

      # Configure row tag for alternating colors
      self.tree.tag_configure("evenrow", background="#FFA842")
      self.tree.tag_configure("oddrow", background="#FCD299")

      # Scrollbar
      self.scrollbar = ttk.Scrollbar(self.tree_contaniner, orient=tk.VERTICAL, command=self.tree.yview)
      self.tree.configure(yscroll= self.scrollbar.set)

      # Widgets positions
      self.tree_contaniner.grid(row=2, column=0, columnspan=2, sticky= "wn", padx=0, pady=20)
      self.tree.grid(row=1,column=0,  columnspan=2, sticky="nsew", padx=2, pady=0)
      self.scrollbar.grid(row=1, column=2, sticky="ns")

  def select_record(self):
      """This method is intended for selecting a member record from the Treeview"""
      
      # Clear edit form
      self.clear_edit_form()

      # Get the selected member from the Treeview
      self.selected = self.tree.focus()

      # Display an error message when no item member is selected
      if not self.selected:
          messagebox.showerror("Error", "Please select a member first")
          return None

      # Retrieve all values
      self.values = self.tree.item(self.selected, "values")

      self.selected_member_id = self.values[0]
      self.direct_debit = self.values[7]
      self.extra_1 = self.values[8]
      self.extra_2 = self.values[9]
      self.extra_3 = self.values[10]
      self.extra_4 = self.values[11]
      self.frequency = self.values[12]

      # Insert values to edit form
      self.edit_first_name_entry.insert(0, self.values[1])
      self.edit_last_name_entry.insert(0, self.values[2])
      self.edit_address_entry.insert(0, self.values[3])
      self.edit_mobile_number_entry.insert(0, self.values[4])
      self.edit_membership_type_var.set(self.values[5])
      self.edit_membership_duration_var.set(self.values[6])
   
  def update_record(self):
      """This method is responsible for upadating the selected member record in the database"""
      
      self.selected = self.tree.focus()

      # Display an error message when no item is selected
      if not self.selected:
          messagebox.showerror("Error", "Please select a member first")
          return None
      
      # Ask the user to confirm changes in members record
      confirm = messagebox.askokcancel("Update Record", "Are you sure you want to save changes to the member record?")

      if confirm:
      
         # Connect to database
         self.connect_database()

         # Create an update query
         update_query = '''
                  UPDATE Memberships 
                  SET First_Name=?, Last_Name=?, Address=?, Mobile=?, 
                     Membership_Type=?, Membership_Duration=?, 
                     Direct_Debit=?, Extra_1=?, Extra_2=?, Extra_3=?, 
                     Extra_4=?, Payment_Frequency=?
                  WHERE MemberID=?
            '''
         # Create a tuple containng the new values for each field in the database record
         values =(
                  self.edit_first_name_entry.get(), 
                  self.edit_last_name_entry.get(), 
                  self.edit_address_entry.get(), 
                  self.edit_mobile_number_entry.get(),
                  self.edit_membership_type_var.get(),
                  self.edit_membership_duration_var.get(),
                  self.direct_debit,
                  self.extra_1,
                  self.extra_2,
                  self.extra_3,
                  self.extra_4,
                  self.frequency,
                  self.selected_member_id,)
         
         try:
               # Execute the update query
               self.cursor.execute(update_query, values)

               # Commit the changes
               self.conn.commit()

               # Inform the user that the record was updated
               time.sleep(1.1)
               messagebox.showinfo("Success", "Record updated successfully")

               # Clear edit form
               self.clear_edit_form()

               # Refresh the treeview
               self.clear_treeview()
               self.show_data()

         except Exception as e:
               # Handle any errors
               messagebox.showerror("Error", f"An error occurred: {e}")
      
      else:
          # Cancel updating record
          messagebox.showerror("Update failed", "Failed to save the changes. No updates were made.")

  def clear_treeview(self):
      """Ths method removes all items from the Treeview"""

      # Delete all items from the Treeview
      self.tree.delete(*self.tree.get_children())

  # Clear search form
  def clear_search_form(self):
      
      self.member_id_entry.delete(0, tk.END)
      self.last_name_entry.delete(0, tk.END)
      self.membership_type_box.set("")
   
  # Clear edit form
  def clear_edit_form(self):
      
      self.edit_first_name_entry.delete(0, tk.END)
      self.edit_last_name_entry.delete(0,tk.END)
      self.edit_address_entry.delete(0, tk.END)
      self.edit_mobile_number_entry.delete(0, tk.END)
      self.edit_membership_type_var.set(None)
      self.edit_membership_duration_var.set(None)

  def show_data(self):
      """This method display members record in the Treeview"""
      
      # Connect to the database
      self.connect_database()
      
      self.query = "SELECT * FROM Memberships"
      self.cursor.execute(self.query)               
      self.records = self.cursor.fetchall()
      
      # Insert data to the Treeview
      for i, row in enumerate(self.records):
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tree.insert("", "end", values=row, tags=(tag,))

# Run application
if __name__ == "__main__":
    
    app = SearchForm()
    app.mainloop()