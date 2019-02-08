import os
from datetime import datetime, timedelta

from display import pause, clear_screen


# Continuously ask the user to add date
def get_date():
    while True: 
        try:  
            print( "Date of the task\nPlease use DD/MM/YYYY\n")
            date = input("> ")
           
            # Ensure that date format is valid
            parsed_date = datetime.strptime(date, '%d/%m/%Y')
            formatted_date = parsed_date.strftime('%d/%m/%Y')
            clear_screen()
            return formatted_date
        except ValueError:
            print("\n{} doesn't seem to be a valid date and time."
                  .format(date))
            pause()
            clear_screen()
            continue

def get_parsed_date():
    while True: 
        try:  
            print( "Please use DD/MM/YYYY\n")
            date = input("> ")
           
            # Ensure that date format is valid
            parsed_date = datetime.strptime(date, '%d/%m/%Y')

            clear_screen()
            return parsed_date
        except ValueError:
            print("\n{} doesn't seem to be a valid date and time."
                  .format(date))
            pause()
            clear_screen()
            continue

# Continuously ask the user to add title
def get_title():
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
def get_time():
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
def get_notes():
    while True:
        print("Notes (optional)\n")
        return input("> ")

# Continuously ask the user to enter a keyword
def get_keyword():
    while True:
        try: 
            print("Keyword\n")
            keyword = input("> ")
            if len(keyword) == 0:
                raise NameError("Please enter a valid keyword.")
            clear_screen()
            return keyword
        except NameError as e:
            print(e)
            pause()
            clear_screen()
            continue

def get_regex():
    while True:
        try: 
            print("RegEx\n")
            regex = input("> ")
            if len(regex) == 0:
                raise NameError("Please enter a valid RegEx.")
            clear_screen()
            return regex
        except NameError as e:
            print(e)
            pause()
            clear_screen()
            continue

def get_date_range():
    date_list = []
    start = get_parsed_date()
    end = get_parsed_date()
    # generator
    date_array = (start + timedelta(days=x) for x in range(0, (end-start).days))

    for date_object in date_array:
        date_list.append(date_object.strftime('%d/%m/%Y'))

    return date_list

# Testing!
if __name__ == "__main__":
    get_date_range()