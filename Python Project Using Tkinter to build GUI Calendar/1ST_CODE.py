from tkinter import *
import calendar

def month_calendar():
    # Retrieving the selected month and year from the Spinbox widgets
    month = int(monthspinBox.get())
    year = int(yearspinBox.get())
    
    # Getting the calendar data for the specified month and year
    data = calendar.month(year, month)
    
    # Clearing the textfield and insert the calendar data
    textfield.delete(0.0, END)
    textfield.insert(INSERT, data)

# Creating the main Tkinter window
root = Tk()
root.resizable(0, 0)  # Disable window resizing
root.config(bg='green')  # Setting the background color of the window to green
root.title("Calendar Date Picker")  # Adding a window title

# Creating labels for the month and year fields
monthLabel = Label(root, text='Month', font=('arial', 12, 'bold'), bg='green')
monthLabel.grid()

yearLabel = Label(root, text='Year', font=('arial', 12, 'bold'), bg='green')
yearLabel.grid(row=0, column=1)

# Creating Spinbox widgets for selecting the month and year
monthspinBox = Spinbox(root, from_=1, to=12, width=8, font=('arial', 10, 'bold'))
monthspinBox.grid(row=1, column=0, padx=10)

yearspinBox = Spinbox(root, from_=1900, to=3000, width=8, font=('arial', 10, 'bold'))
yearspinBox.grid(row=1, column=1, padx=10)

# Creating a button to trigger the calendar display
goButton = Button(root, text='Go', font=('arial', 12, 'bold'), command=month_calendar)
goButton.grid(row=1, column=2, padx=10)

# Creating a text area to display the calendar
textfield = Text(root, width=24, height=8, fg='black')
textfield.grid(row=2, column=0, columnspan=3)

# Starting the main event loop of the Tkinter application
root.mainloop()


