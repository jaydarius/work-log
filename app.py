import os
import csv
from datetime import datetime

from get_inputs import (get_date, get_title,
                        get_time, get_notes,
                        get_keyword, get_regex)

from csv_access import (insert_record, open_csv, date_search,
                        keyword_search, regex_search,
                        time_search, del_record)
from display import (print_record, main_menu, search_menu,
                     clear_screen, pause, invalid_input)

from search_route import search_records, page_records, search_route

from add_route import add_route




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
            add_route()

        elif choice == "b":
            search_route()

        elif choice == "c":
            print("Thanks for using the Work Log! See ya soon.")
            break

        else:
            invalid_input()
        
