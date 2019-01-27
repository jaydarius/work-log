import os

from datetime import datetime

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def new_page(letter_choice):
    clear_screen()
    if letter_choice.lower() == "a":
        print("Date of the task\n")
        date_value = input("Please use DD/MM/YYYY: 01/05/2017 ")
    if letter_choice == "b":
        pass
    if letter_choice == "c":
        pass


worklog = {}
clear_screen()
print(
    "== WORK LOG==\n"
    "What would you like to do?\n"
    "a) Add new entry\n"
    "b) Search existing entries\n"
    "c) Quit program\n"
)

choice = input("> ")

clear_screen()

# Follow the 'Add new entry' route
while choice.lower() == "a":
    
    try:  # Give the date
        print( "Date of the task\nPlease use DD/MM/YYYY\n")
        date_input = input("> ")
        # Ensure that date format is valid
        parsed_date = datetime.strptime(date_input, '%m/%d/%Y')
        
    except ValueError:
        print("\n{} doesn't seem to be a valid date and time."
              .format(date_input))
        os.system("pause")
        clear_screen()
    else:
        break
    
            
    
clear_screen()

# Give title of task
print("Title of the task\n")
title_input = input("> ")
clear_screen()

# Give time spent on task
print("Time spent on the task (rounded)\n")
time_spent_value = input("> ")
clear_screen()

# Give optional notes of task
print("Notes (optional)\n")
notes_value = input("> ")
clear_screen()

# add all inputs to the dict
worklog.update([
    ('Date', date_input), 
    ('Title', title_input),
    ('Time Spent', time_spent_value),
    ('Notes', notes_value)
    ])
print(worklog)