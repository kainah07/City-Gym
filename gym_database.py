""" City Gym Database """

from tkinter import messagebox
import sqlite3

# Connect to our database (or create a new one if none exists)
class GymDataBase():
    def __init__(self, master):
        """ Class for connecting the Membership form to the gym database """
        
        self.conn = sqlite3.connect("gym_database.db")
        self.cursor = self.conn.cursor()

        try:
            # Create the database
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS Memberships (
                                MemberID INTEGER PRIMARY KEY NOT NULL,
                                First_Name TEXT NOT NULL,
                                Last_Name TEXT NOT NULL,
                                Address TEXT NOT NULL,
                                Mobile TEXT NOT NULL,
                                Membership_Type TEXT NOT NULL,
                                Membership_Duration TEXT NOT NULL,
                                Direct_Debit BOOLEAN NOT NULL,
                                Extra_1 BOOLEAN NOT NULL,
                                Extra_2 BOOLEAN NOT NULL,
                                Extra_3 BOOLEAN NOT NULL,
                                Extra_4 BOOLEAN NOT NULL,
                                Payment_Frequency TEXT NOT NULL
                                )''')
            self.conn.commit()
            print("Database initialized successfully.")

        except sqlite3.Error as e:
            print("Error initializing database:", e)
            

    # Insert new member method
    def insert_new_member(self, first_name, last_name, address, mobile_number, membership_plan, membership_duration, payment_method, extra1, extra2, extra3, extra4, payment_frequency):
        """ Insert new member into the gym database """

        try: 
            self.cursor.execute('''INSERT INTO Memberships (First_Name, Last_Name, Address, Mobile, Membership_Type, Membership_Duration, Direct_Debit, Extra_1, Extra_2, Extra_3, Extra_4, Payment_Frequency)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (first_name, last_name, address, mobile_number, membership_plan, membership_duration, payment_method, extra1, extra2, extra3, extra4, payment_frequency))

            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Error inserting new member:", e)

        # Close the connection after all database operations are complete
        self.close_connection()

    def close_connection(self):
        self.conn.close()
      

    