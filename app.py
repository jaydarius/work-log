import os
from get_inputs import (get_date_from_user, get_title_from_user, 
                        get_time_from_user, get_notes_from_user,
                        clear_screen)
from datetime import datetime


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


worklog = {}


clear_screen()
if __name__ == "__main__":
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
        
        date = get_date_from_user()

        title = get_title_from_user()

        time_spent = get_time_from_user()
        
        notes = get_notes_from_user()  

        break  # the "Add new Entry route"
            
    clear_screen()

    # add all inputs to the dict

    worklog.update([
        ('Date', date), 
        ('Title', title),
        ('Time Spent', time_spent),
        ('Notes', notes)
    ])

    print(worklog)
