import os
import csv
from datetime import datetime

from get_inputs import (get_date_from_user, get_title_from_user, 
                        get_time_from_user, get_notes_from_user,
                        pause, get_keyword_from_user)
from csv_access import csv_insert, csv_read


def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    print(  # Main Menu
            "== WORK LOG==\n"
            "What would you like to do?\n"
            "a) Add new entry\n"
            "b) Search existing entries\n"
            "c) Quit program\n"
        )

def search_menu():
    print(  # Search Menu
    "Do you want to search by:\n"
    "a) Exact Date\n"
    "b) Range of Dates\n"  #extra credit
    "c) Exact Search\n"
    "d) Regex Pattern\n"
    "e) Return to Main Menu\n"
)

def print_record(record):
    print(
        f"Date: {record['date']}\n"
        f"Title: {record['title']}\n"
        f"Time Spent: {record['time_spent']}\n"
        f"Notes: {record['notes']}\n")


work_log = {}


if __name__ == "__main__":
    clear_screen()
        
    logging = True

    while logging:
        clear_screen()
        main_menu()
        
        choice = input("> ")
        choice = choice.lower()

        clear_screen()

        # Follow the 'Add new entry' route
        if choice == "a":
            
            date = get_date_from_user()
            title = get_title_from_user()
            time_spent = get_time_from_user()
            notes = get_notes_from_user() 

            work_log.update([
                ('date', date), 
                ('title', title),
                ('time_spent', time_spent),
                ('notes', notes)
            ])
            csv_insert(work_log)
            clear_screen()

            input("The entry has been added! Press enter to return to the menu.")

        while choice == "b":
            search_menu()
            
            choice = input("> ")
            choice = choice.lower()
            
            clear_screen()

            # create a function that will allow me to:  # extra credit
                # cycle through results
                # edit the currently viewed result
                # deleted the currently viewed result
                # return to the search menu form the currently viewed result

            if choice == 'a':
                date = get_date_from_user()
                # pass the date into a function to read csv
                record = csv_read(date)  # record is an OrderedDict

                print_record(record)
                pause()

            # if b  # extra credit

            if choice == 'c':
                keyword = get_keyword_from_user()
                pause()
            
            # if d

            # if e
            
            choice = 'b' # stay in the Search Menu

            clear_screen()
            
        if choice == "c":
            print("Thanks for using the Work Log! See ya soon.")
            break

        
