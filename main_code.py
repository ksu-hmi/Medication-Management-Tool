# Medication Management Tool
# Base code from found repository to build upon 


# Prescription Reminder

#Importing all the necessary libraries:
from tkinter import *
import datetime
import time
import sys
import signal
import os
import webbrowser
import time
import re
import tkinter as tk
import sqlite3


# Log into the app
print ("Pocket Pill, your guide to better health")

print("Enter Email address(Username): ")
email_address = input()
while "@" not in email_address:
    email_address = input("Your email address must have '@' in it\nPlease write your email address again: ")
    if len(email_address) <= 6 :
        email_address = input("Your email address is too short\nPlease write your email address again: ")
    if "." not in email_address:
        email_address = input("Your email address must have '.' in it\nPlease write your email address again: ")
while "." not in email_address:
    email_address = input("Your email address must have '.' in it\nPlease write your email address again: ")
    if len(email_address) <= 6 :
        email_address = input("Your email address is too short\nPlease write your email address again: ")
    if "@" not in email_address:
        email_address = input("Your email address must have '@' in it\nPlease write your email address again: ")

# Create password
def checkPassword(password):
    """
    Validate the password
    """
    if len(password) < 8:
        # Password to short
        print("Your password must be 8 characters long.")
        return False
    elif not re.findall(r'\d+', password):
        # Missing a number
        print("You need a number in your password.")
        return False
    elif not re.findall(r'[A-Z]+', password):
        # Missing at least one capital letter
        print("You need a capital letter in your password.")
        return False
    else:
        # All good
        print("All good")
        return True

# Promt user to enter valid password
passwordValid = False
while not passwordValid:
    create_password = input( "Create your password:\n (Password must contain at least 8 characters, one number,\n one capital letter, and one lowercase letter)")
    passwordValid = checkPassword(create_password)

print("Enter your first name: ")
first_name=input()
print("Enter your last name: ")
last_name=input()

#Now log in with new password
print("Welcome", first_name + "!", "Your profile is set up")
print("Log in to access the application\n You have 3 attempts or application quits")

attempts = 0

username = email_address
password = create_password

while True:
    usern = input("Enter Username: ")
    print()
    userp = input("Enter Password: ")
    attempts += 1
    if attempts == 3:
        print("Too many incorrect attempts. Please try again in few minutes")
        exit()
    else:
        if usern == username and userp == password:
            print("\nAccess Granted. Welcome " + first_name)
            break
        else:
            print("\nIncorrect credentials. Try again")
            


def print_menu():
    print()
    print("Welcome to Pocket Pill! Press enter to select option")
    print()

    choice = input("""
            1. Add A Medication
            2. Delete A Medication
            3. Review Your Medication List
            4. Set an Alarm for Medication
            5. Create A Note
            6. View Saved Notes
            7. Exit
            """)

print_menu()


choice = input("Select the menu item that you want edit [1-5]: ")
choice = int(choice)
medication_name=[]

# Creating Notes Window
# Create the main window
window = tk.Tk()
window.title("Note Taking")
window.geometry("400x300")

# Create a text box
note_entry = tk.Text(window)
note_entry.pack()

# Create a save button and database integration
def save_note():
   note = note_entry.get("1.0", tk.END)
   conn = sqlite3.connect("notes.db")
   cursor = conn.cursor()
   cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
   cursor.execute("INSERT INTO notes (content) VALUES (?)", (note,))
   conn.commit()
   conn.close()

save_button = tk.Button(window, text="Save Note", command=save_note)
save_button.pack()

while choice != 7:
    if choice == 1:
        med_add = input("Enter the medication Name to add to your list: ")
        medication_name.append(med_add)
        print("Updated Medication List: ", medication_name) 
        med_direction = input()
        break
    elif choice == 2:
        print ("Delete A Medication")
        med_remove = input("Enter the medication that you are removing from your list: ")   
        medication_name.remove(med_remove)
        print("Updated medication list: ", medication_name)
        continue
    elif choice == 3:
        print ("Review Your Medication List")
        print("Current medication list: ", "\n", medication_name)
        break
    elif choice == 4:
        print ("Set an Alarm for Medication")

        alarm_HH = input("Enter the hour you want to take the medication - in 24 hour format: ")
        alarm_MM = input("Enter the minute you want to take the medication: ")
    elif choice == 5:
        def notes_window():
            # Runs note-taking window application
            window.mainloop()
        notes_window()
    elif choice == 6:
        def view_notes():
            conn = sqlite3.connect("notes.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notes")
            notes = cursor.fetchall()
            conn.close()
   
            view_window = tk.Toplevel(window)
            view_window.title("View Notes")
            view_text = tk.Text(view_window)
            for note in notes:
                view_text.insert(tk.END, note[1] + "\n")
            view_text.pack()
        view_notes()

# Creating button for viewing notes
view_button = tk.Button(window, text="View Notes", command=view_notes)
view_button.pack()

print(medication_name)

print("Enter the directions for medication : ")
med_direction = input()

print(med_direction)
#need input format for the time so end user will know how to enter it!
print("Enter time of day medication is to be taken : ") 
time_take=input('Please input the time for the alarm in format HHMM: \n ')
print(time_take)
print("Hello", first_name,"!", "Remember to take", med_direction, "at", time_take)

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to take med")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
    
   
# Create GUI in tinker
clock = Tk()
clock.title("Pocket Pill")
clock.geometry("400x200")
# smcfar18-updated color scheme
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="white",bg="purple",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "Remember to take your med",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)
clock.mainloop()
#Execution of the window.



# Prescription Refill Reminder
import datetime
import decimal
InputDatePrescribed= input("When was prescription written? (year-month-day): ")
InputPillPatchRefillCount = input("How many pills/inhalers in this refill?: ")
InputPillsPerday = input("How many pills can be taken in a day?: ")
InputPatchDuration = input("How often is the inhaler used (hours)?: ")
# Written in standard Year, month,day 2008-8-2
YearMonthDayInput = InputDatePrescribed.split('-')#split this in arguments using"-", then input that
InputYear,InputMonth,InputDay = InputDatePrescribed.split('-')
DatePrescribed = datetime.date (int(InputYear), int(InputMonth),int(InputDay))


def PillRefillDuration (InputPillPatchRefillCount,InputPillsPerday): #STATES HOW MANY DAYS IT SHOULD LAST AS READABLE OUTPUT
    PillRefillDuration = decimal.Decimal(decimal.Decimal(InputPillPatchRefillCount)/decimal.Decimal(InputPillsPerday))
    return PillRefillDuration

def PillDeltaDueDate (InputPillPatchRefillCount, InputPillsPerday): #RETURNS A TIMEDELTA OBJECT IN DAYS WHICHS ALLOWS MANIPULATION
    return datetime.timedelta (float(PillRefillDuration(InputPillPatchRefillCount, InputPillsPerday)))#Need to do this since timedelta doesn't take Decimal type
    
def PatchRefillDuration (InputPillPatchRefillCount,InputPatchDuration):
    PatchRefillDuration = decimal.Decimal(decimal.Decimal(InputPatchDuration)/decimal.Decimal(24)) *decimal.Decimal(InputPillPatchRefillCount)
    return PatchRefillDuration

def PatchDeltaDueDue (InputPillPatchRefillCount, InputPatchDuration):
    return datetime.timedelta (float (PatchRefillDuration(InputPillPatchRefillCount, InputPatchDuration)))
    
if InputPatchDuration == "":
    a = PillRefillDuration (InputPillPatchRefillCount, InputPillsPerday)
    print ("It shoud last ", a, " days.")
    print ("It was prescrbied", DatePrescribed)
    DueDate = DatePrescribed + PillDeltaDueDate (InputPillPatchRefillCount, InputPillsPerday)
    print ("It is due on", DueDate)

if InputPillsPerday == "":
    a = PatchRefillDuration(InputPillPatchRefillCount, InputPatchDuration)
    print ("It shoud last ", a, " days.")
    print ("It was prescrbied", DatePrescribed)
    DueDate = DatePrescribed + PatchDeltaDueDue (InputPillPatchRefillCount, InputPatchDuration)
    print ("It is due on", DueDate)
