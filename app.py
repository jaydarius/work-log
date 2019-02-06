import os
import csv
from datetime import datetime

from get_inputs import (get_date, get_title, get_regex, 
                        get_time, get_notes,
                        get_keyword)
from csv_access import (insert_record, open_csv, date_search,
                        keyword_search, regex_search,
                        time_search, del_record, edit_record)
from display import (print_record, main_menu, search_menu,
                     clear_screen, pause)


def add_entry(date, title, time_spent, notes):
    record = {}
    record.update([
        ('date', date), 
        ('title', title),
        ('time_spent', time_spent),
        ('notes', notes)])
    insert_record(record, 'a')

def search_meta(getf, searchf):
    user_input = getf()
    records = searchf(user_input)  

    if not records:
        print("Not found!\n")
        pause()
    else:
        show_each_record_one_at_a_time(records)

def show_each_record_one_at_a_time(records):
    # records = list returned from search criteria - NOT entire csv
    index = 0
    origin_csv = open_csv('work-log.csv')

    while True:
        record = records[index]

        clear_screen()
        print("Result {} out of {}".format(index+1, len(records)))
        print_record(record)

        print("Next, Back, Edit, Delete, Return to Search Menu")
        user_choice = input("> ")

        if user_choice == "n":
            index += 1
            continue

        if user_choice == "b":
            index -= 1
            continue
        
        # Edit Record
        if user_choice == "e":
            edit_record(record)

        # Delete Record
        if user_choice == "d":
            del_record()
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

        
