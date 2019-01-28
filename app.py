import os

from datetime import datetime


def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

# Optimize following the route to add a journal
def new_page(letter_choice):
    clear_screen()
    if letter_choice.lower() == "a":
        print("Date of the task\n")
        date_value = input("Please use DD/MM/YYYY: 01/05/2017 ")
    if letter_choice == "b":
        pass
    if letter_choice == "c":
        pass

# Continuously ask the user to add date
def get_date_from_user():
    while True: 
        try:  # Give the date
            print( "Date of the task\nPlease use DD/MM/YYYY\n")
            date_input = input("> ")
            # Ensure that date format is valid
            parsed_date = datetime.strptime(date_input, '%m/%d/%Y')
            clear_screen()
            return date_input
            break
        except ValueError:
            print("\n{} doesn't seem to be a valid date and time."
                  .format(date_input))
            os.system("pause")
            clear_screen()
            continue
    return date_input

# Contrinuously ask the user to add title
def get_title_from_user():
    while True:
        try:  # Give title of task
            print("Title of the task\n")
            title_input = input("> ")
            if len(title_input) == 0:
                raise NameError("Please enter a valid title.")
        except NameError as e:
            print(e)
            os.system("pause")
            clear_screen()
            continue
        clear_screen()
        break

def get_time_from_user():
    while True:
        #try:  # Give time spent on task
        print("Time spent on the task (rounded)\n")
        time_spent_value = input("> ")
        time_spent_value = int(time_spent_value)
    

        break

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
    
    get_date_from_user()

    get_title_from_user()
    
    worklog.update([
    ('Date', date_input), 
    ('Title', title_input),
    ('Time Spent', time_spent_value),
    ('Notes', notes_value)
    ])

    print(worklog)
    


    break  # the "Add new Entry route"
        
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