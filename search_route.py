from csv_access import (insert_record, open_csv, date_search,
                        keyword_search, regex_search,
                        time_search, del_record)
from edit_route import edit_record
from display import pause, clear_screen, print_record, invalid_input, page_menu

def page_records(records):
    # records = list returned from search criteria - NOT entire csv
    index = 0
    origin_csv = open_csv('work-log.csv')
    searching = True
    edited_record = None
    
    while searching:
        record = records[index]

        clear_screen()
        print("Result {} out of {}".format(index+1, len(records)))
        print_record(record)
        page_menu(index)
        user_choice = input("> ")

        if user_choice == "n":
            index += 1
            continue
        elif user_choice == "b":
            if index < 1:
                print("\nCan't go back!\n")
                pause()
            else:
                index -= 1
            continue
        elif user_choice == "e":
            edit_record(record, origin_csv)
            break
        elif user_choice == "d":
            del_record()
            clear_screen()
            print(""""{}" log has been deleted!\n""".format(record['title']))       
            pause()
            break
        elif user_choice == "r":
            break    
        else:
            invalid_input()


def search_records(getf, searchf):
    user_input = getf()
    records = searchf(user_input)  

    if not records:
        print("Not found!\n")
        pause()
    else:
        page_records(records)



