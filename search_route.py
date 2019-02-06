from csv_access import (insert_record, open_csv, date_search,
                        keyword_search, regex_search,
                        time_search, del_record)
from edit_route import edit_record
from display import pause, clear_screen, print_record

def display_search(records):
    # records = list returned from search criteria - NOT entire csv
    index = 0
    origin_csv = open_csv('work-log.csv')
    searching = True
    
    while searching:
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
            edit_record(record, origin_csv)

        # Delete Record
        if user_choice == "d":
            del_record()
            clear_screen()
            print(""""{}" log has been deleted!\n""".format(record['title']))       
            pause()
            break

        if user_choice == "r":
            break    

def search_records(getf, searchf):
    user_input = getf()
    records = searchf(user_input)  

    if not records:
        print("Not found!\n")
        pause()
    else:
        display_search(records)



