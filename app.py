import os
import csv
from datetime import datetime

from get_inputs import (get_date, get_title, get_regex, 
                        get_time, get_notes,
                        get_keyword)
from csv_access import (insert_record, open_csv, date_search,
                        keyword_search, regex_search,
                        time_search, del_record)
from display import (print_record, main_menu, search_menu,
                     clear_screen, pause, invalid_input)
from search_route import search_records, page_records


def add_entry(date, title, time_spent, notes):
    record = {}
    record.update([
        ('date', date), 
        ('title', title),
        ('time_spent', time_spent),
        ('notes', notes)])
    insert_record(record, 'a')


if __name__ == "__main__":
    ### Initialize Test Data
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
        elif choice == "b":
            searching = True
            
            while searching:
                search_menu()
                
                choice = input("> ")
                choice = choice.lower()
                
                clear_screen()

                if choice == 'a':
                    search_records(get_date, date_search)
                # if b  # extra credit
                elif choice == 'c':
                    search_records(get_keyword, keyword_search)
                elif choice == 'd':
                    search_records(get_regex, regex_search)
                elif choice == 'e':
                    search_records(get_time, time_search)
                elif choice == 'f':
                    main_menu()
                else:
                    invalid_input()

                clear_screen()
        elif choice == "c":
            print("Thanks for using the Work Log! See ya soon.")
            break
        else:
            invalid_input()
        
