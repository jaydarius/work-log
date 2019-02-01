import os

from datetime import datetime


def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def pause():
    # Wont work in Treehouse Workspaces :)
    cmd = "pause" if os.name == "nt" else "read -rsp $'Press any key to continue . . .\n' -n 1 key"
    os.system(cmd)
    return None

# Continuously ask the user to add date
def get_date_from_user():
    while True: 
        try:  
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

# Continuously ask the user to add title
def get_title_from_user():
    while True:
        try: 
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
         

# Continuously ask the user to add time
def get_time_from_user():
    while True:
        try:  # Give time spent on task
            print("Minutes spent on the task (rounded)\n")
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

# Continuously ask the user to add notes
def get_notes_from_user():
    while True:
        print("Notes (optional)\n")
        return input("> ")

# Continuously ask the user to enter a keyword
def get_keyword_from_user():
    while True:
        try: 
            print("Search by keyword\n")
            title = input("> ")
            if len(title) == 0:
                raise NameError("Please enter a valid keywprd.")
            clear_screen()
            return title
        except NameError as e:
            print(e)
            pause()
            clear_screen()
            continue