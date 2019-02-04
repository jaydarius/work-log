import os
import csv
from datetime import datetime

from get_inputs import (get_date, get_title, get_regex, 
                        get_time, get_notes,
                        pause, get_keyword)
from csv_access import (insert_record, date_search,
                        keyword_search, regex_search,
                        time_search)


def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    print( 
        "== WORK LOG==\n"
        "What would you like to do?\n"
        "a) Add new entry\n"
        "b) Search existing entries\n"
        "c) Quit program\n"
        )

def search_menu():
    print( 
        "Do you want to search by:\n"
        "a) Exact Date\n"
        "b) Range of Dates\n"  #extra credit
        "c) Exact Search\n"
        "d) Regex Pattern\n"
        "e) Time Spent\n"
        "f) Return to Main Menu\n"
)

def print_record(record):
    print(
        f"Date: {record['date']}\n"
        f"Title: {record['title']}\n"
        f"Time Spent: {record['time_spent']}\n"
        f"Notes: {record['notes']}\n")

def add_entry(date, title, time_spent, notes):
    record = {}
    record.update([
        ('date', date), 
        ('title', title),
        ('time_spent', time_spent),
        ('notes', notes)])
    insert_record(record)

def search_meta(getf, searchf):
    user_input = getf()
    records = searchf(user_input)  

    if not records:
        print("Not found!\n")
    else:
        for record in records:
                print_record(record)
    pause()

# create a function that will allow me to:  # extra credit
    # cycle through results
    # edit the currently viewed result
    # deleted the currently viewed result
    # return to the search menu form the currently viewed result

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
            
            date = get_date()
            title = get_title()
            time_spent = get_time()
            notes = get_notes() 
           
            add_entry(date, title, time_spent, notes)
            clear_screen()
            input("The entry has been added! Press enter to return to the menu.")

        # Follow the 'Search' route
        while choice == "b":
            search_menu()
            
            choice = input("> ")
            choice = choice.lower()
            
            clear_screen()

            if choice == 'a':
                search_meta(get_date, date_search)

            # if b  # extra credit

            if choice == 'c':
                search_meta(get_keyword, keyword_search)
            
            if choice == 'd':
                search_meta(get_regex, regex_search)

            if choice == 'e':
                search_meta(get_time, time_search)

            if choice == 'f':
                break
            
            choice = 'b' # stay in the Search Menu

            clear_screen()
            
        if choice == "c":
            print("Thanks for using the Work Log! See ya soon.")
            break

        
