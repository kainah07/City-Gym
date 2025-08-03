import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CalculateTotal():
    def __init__(self, master, membership_details= None, extras=None, payment_option= None) :
        """A class managing Calculated total GUI"""
        
        self.master = master
        self.calculated = False  # Initialize the calculated attribute to False
        self.membership_details = membership_details
        self.extras = extras
        self.payment_option = payment_option
        
        self.widgets_style()
        self.create_widgets_container()
        self.initialize_label_widget()
        self.initialize_entry_widgets()
        self.initialize_button_widget()

    def widgets_style(self):
        """ Change frame color, font, font sizes and background color"""

        self.style = ttk.Style()
        self.style.configure("Total.TFrame", background="#F6F6F6")

    def create_widgets_container(self):
        """Create a container to display total labels and entry to show calculated totals"""

        self.total_frame = ttk.Frame(self.master, style= "Total.TFrame", width= 40, height= 25)
        self.total_label = ttk.Label(self.total_frame, text="TOTAL", background="#F6F6F6")

        self.total_frame.grid(row=3, rowspan=2, column=1, sticky="ne", padx=20, pady=20)
        self.total_label.grid(row=1,column=0, sticky="w", padx=17, pady=10)

    def initialize_label_widget(self):
        """Initialize label for calculated total"""
        # Labels 
        self.total_payment_labels = [
        
            ttk.Label(self.total_frame, text= "Base membership cost:", background= "#F6F6F6"),
            ttk.Label(self.total_frame, text= "Extra charges:", background= "#F6F6F6"),
            ttk.Label(self.total_frame, text= "Total discount:", background= "#F6F6F6"),
            ttk.Label(self.total_frame, text= "Net membership cost:", background= "#F6F6F6"),
            ttk.Label(self.total_frame, text= "Regular payment amount:", background= "#F6F6F6")
            ]
        
        for i,label in enumerate(self.total_payment_labels):
            label.grid(row=i +3, column=0,  sticky="w",  padx=17, pady=3)

    def initialize_entry_widgets(self):
        """Initialize entry widget to show the calculated totals"""

        # Entry that shows the price of the calculated total
        self.base_membership_cost = ttk.Entry(self.total_frame, background= "#F6F6F6", justify= "center")
        self.extra_charges = ttk.Entry(self.total_frame,  background= "#F6F6F6", justify= "center")
        self.total_discount = ttk.Entry(self.total_frame,background= "#F6F6F6", justify= "center")
        self.net_cost = ttk.Entry(self.total_frame,  background= "#F6F6F6", justify= "center")
        self.regular_payment = ttk.Entry(self.total_frame, background= "#F6F6F6", justify= "center")
        
        # Insert a default value for the entry to show in the app
        self.base_membership_cost.insert(0, "$0" )
        self.extra_charges.insert(0, "$0" )
        self.total_discount.insert(0, "$0" )
        self.net_cost.insert(0, "$0" )
        self.regular_payment.insert(0, "$0" )

        self.base_membership_cost.grid(row=3,  column=1, sticky="w", padx=20, pady=3)
        self.extra_charges.grid(row=4, column=1, sticky="w", padx=20, pady=3)
        self.total_discount.grid(row=5, column=1, sticky="w", padx=20, pady=3)
        self.net_cost.grid(row=6, column=1, sticky="w", padx=20, pady=3)
        self.regular_payment.grid(row=7, column=1, sticky="w", padx=20, pady=3)

    def initialize_button_widget(self):
        """Initialize calculate button to calculate totals"""

        self.calculte_button = ttk.Button(self.total_frame, text="Calculate", command=self.calculate_totals)
        self.calculte_button.grid(row= 9, column=1, sticky="e", padx = 17, pady= 10)
        
    def calculate_totals(self, from_submit=False):
        """
        Calculate all the total amounts for membership cost total, 
        total extra, total discount, net mebership cost and regular payment
        """
        membership_cost = self.membership_details.get_membership_plan()
        membership_duration = self.membership_details.get_membership_duration()
        total_extra = self.extras.calculate_total_extra()
        direct_debit = self.payment_option.get_direct_debit()
        
         # Check if all required options have been selected
        if( membership_cost is None) or (membership_duration is None ):
            if not from_submit:
                messagebox.showwarning("Incomplete selection","Please select all required option")
                return None
            
        # Check if any required values are missing
        if any(value is None for value in [membership_cost, membership_duration, total_extra]):
            return None

        # If the user  chooses to pay direct debit a discount will be added 
        direct_debit_discount = 0
        if direct_debit:
            direct_debit_discount = membership_cost * 0.01

        # Calculate total amount
        net_cost = membership_cost + total_extra - membership_duration - direct_debit_discount

        total_discount = membership_duration + direct_debit_discount

        regular_payment = self.master.payment_option.get_payment_frequency(net_cost)

        # Check if all required options have been selected
        if (regular_payment is None):
            if not from_submit:
                messagebox.showwarning("Incomplete selection","Please select all required option")
                return None
            
        self.calculated = True  # Set calculated to True once the calculation is done
        
        # Delete the existing characters in the entry
        self.base_membership_cost.delete(0, tk.END)
        self.extra_charges.delete(0, tk.END)
        self.total_discount.delete(0, tk.END)
        self.net_cost.delete(0, tk.END)
        self.regular_payment.delete(0, tk.END)
        
        # Show the calculated result
        self.base_membership_cost.insert(0, f"${membership_cost}" )
        self.extra_charges.insert(0, f"${total_extra}" )
        self.total_discount.insert(0,f"${total_discount}")
        self.net_cost.insert(0, f"${net_cost}" )
        self.regular_payment.insert(0, f"${regular_payment}" )

        total_membership_cost = "\n".join([f"{totals}: {price}" for totals, price in {
            "Membership cost total": f"${net_cost}\n"}.items()])

        return total_membership_cost
    
    def calculated_totals(self):

        membership_details = self.membership_details.get_membership_details()
        membership_cost = self.membership_details.get_membership_plan()
        membership_duration = self.membership_details.get_membership_duration()
        total_extra = self.extras.calculate_total_extra()
        direct_debit = self.payment_option.get_direct_debit()

        # If the user  chooses to pay direct debit a discount will be added 
        direct_debit_discount = 0
        if direct_debit:
            direct_debit_discount = membership_cost * 0.01

        # Calculate total amount
        net_cost = membership_cost + total_extra - membership_duration - direct_debit_discount

        total_discount = membership_duration + direct_debit_discount

        regular_payment = self.master.payment_option.get_payment_frequency(net_cost)

        costs = "\n".join([f"{totals}: {price}" for totals, price in {
            "Base membership cost": f"${membership_cost}",
            "Extra charges": f"${total_extra}",
            "Total discount": f"${total_discount}",
            "Net membership cost": f"${net_cost}",
            "Regular payment": f"${regular_payment}\n"}.items()])

        return membership_details + "\n" + costs

    def reset(self):
        """Reset all entry fields displaying the totals"""

        self.base_membership_cost.delete(0, tk.END)
        self.extra_charges.delete(0, tk.END)
        self.total_discount.delete(0, tk.END)
        self.net_cost.delete(0, tk.END)
        self.regular_payment.delete(0, tk.END)

        self.base_membership_cost.insert(0, "$0" )
        self.extra_charges.insert(0, "$0" )
        self.total_discount.insert(0, "$0" )
        self.net_cost.insert(0, "$0" )
        self.regular_payment.insert(0, "$0" )

        self.calculated = False  # Initialize the calculated attribute to False 
            
