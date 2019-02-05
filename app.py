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
        pause()
    else:
        show_each_record_one_at_a_time(records)

def show_each_record_one_at_a_time(records):
    # records = list returned from search
    index = 0

    while True:
        print(records)
        record = records[index]

        clear_screen()
        print(records)
        print("\nResult {} out of {}".format(index+1, len(records)))
        print_record(record)

        print("Next, Back, Edit, Delete, Return to Search Menu")
        user_choice = input("> ")

        if user_choice == "n":
            index += 1
            continue

        if user_choice == "b":
            index -= 1
            continue
        
        # Edit Row
        if user_choice == "e":
            # what do you want to edit?
            # display the 4 items
            # show the 1 item
            # get the user input for the 1 item
            
            pass

        # Delete Row
        if user_choice == "d":
            # read the origin csv and write all rows except deleted to edited csv
            with open('work-log.csv', 'r', newline='') as inp, open('work-log-edit.csv', 'w', newline='') as out:
                writer = csv.writer(out)
                for row in csv.reader(inp):
                    # This delete will delete multiple entries with the same title
                    print("{} and {} and {} and {}".format(record['title'], record['date'], row[1], row[0]))
                    pause()
                    if row[1] != record['title'] and row[0] != record['date']:
                        writer.writerow(row)
            
            # read the edited csv and overwrite the origin csv with all rows
            with open('work-log-edit.csv', 'r', newline='') as inp, open('work-log.csv', 'w', newline='') as out:
                writer = csv.writer(out)
                for row in csv.reader(inp):
                    writer.writerow(row)
            clear_screen()
            print("Entry has been deleted! Returning to search menu.\n")
            pause()
            user_choice = 'r'
            break
            

        if user_choice == "r":
            break    


if __name__ == "__main__":
    ### TESTING
    with open('test-data.csv', 'r', newline='') as inp, open('work-log.csv', 'w', newline='') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            writer.writerow(row)
    ###
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

        
