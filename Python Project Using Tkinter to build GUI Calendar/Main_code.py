# Project - Using Tkinter to build GUI Calendar


# Importing required libraries
import tkinter as tk
from tkcalendar import Calendar

# Creating the Tkinter window and configure its properties
def get_date():
    # Defining a function to retrieve the selected date from the Calendar
    selected_date = cal.get_date()
    # Creating a label to display the selected date
    selected_date_label.config(text="Selected Date: " + selected_date)

# Creating the Tkinter window
root = tk.Tk()
root.title("Calendar Date Picker")

# Creating the Calendar widget
cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
cal.pack(pady=20)

# Creating a button to trigger date selection and link it to the get_date() function
select_date_button = tk.Button(root, text="Select Date", command=get_date)
select_date_button.pack(pady=10)

# Creating a label to display the selected date
selected_date_label = tk.Label(root, text="Selected Date: ")
selected_date_label.pack(pady=10)

# Running the Tkinter event loop
root.mainloop()
