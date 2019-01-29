import os

from datetime import datetime

# Continuously ask the user to add date
def get_date_from_user():
    while True: 
        try:  # Give the date
            print( "Date of the task\nPlease use DD/MM/YYYY\n")
            date = input("> ")
            # Ensure that date format is valid
            parsed_date = datetime.strptime(date, '%m/%d/%Y')
            clear_screen()
            return date
        except ValueError:
            print("\n{} doesn't seem to be a valid date and time."
                  .format(date))
            pause()
            clear_screen()
            continue

# Contrinuously ask the user to add title
def get_title_from_user():
    while True:
        try:  # Give title of task
            print("Title of the task\n")
            title = input("> ")
            if len(title) == 0:
                raise NameError("Please enter a valid title.")
            clear_screen()
            return title
        except NameError as e:
            print(e)
            pause()
            clear_screen()
            continue
        clear_screen()     

def get_time_from_user():
    while True:
        try:  # Give time spent on task
            print("Time spent on the task (rounded)\n")
            time_spent = input("> ")
            time_spent = int(time_spent)  
            clear_screen()
            return time_spent
        except ValueError:
            print("\n{} doesn't seem to be a valid number."
                  .format(time_spent))
            pause()
            clear_screen()
            continue

def get_notes_from_user():
    while True:
        print("Notes (optional)\n")
        clear_screen()
        return input("> ")