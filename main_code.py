import datetime
import time

def get_user_input():
    name = input("Enter your name: ")
    medication = input("Enter the name of your medication: ")
    dosage = input("Enter the dosage of your medication: ")
    return name, medication, dosage
    
def set_reminder(name, medication, dosage, reminder_time):
    print(f"\nReminder set for {reminder_time.strftime('%H:%M')}:")
    print(f"Hello, {name}! Don't forget to take your {medication} ({dosage}).")
