from display import (pause, clear_screen, print_record,
                    edit_menu)
from csv_access import edit_item


def edit_date(record, origin_csv):
    clear_screen()
    print("Edit Date")
    # must validate date
    new_item = input("> ")

    e_record = edit_item('date', new_item, record, origin_csv)
    record = e_record
    clear_screen()
    print("Date successfully updated!\n")
    pause()

def edit_title(record, origin_csv):
    clear_screen()
    print("Edit Title")
    # must validate date
    new_item = input("> ")

    e_record = edit_item('title', new_item, record, origin_csv)
    record = e_record
    clear_screen()
    print("Title successfully updated!\n")
    pause()

def edit_time(record, origin_csv):
    clear_screen()
    print("Edit Time Spent")
    # must validate
    new_item = input("> ")

    e_record = edit_item('time_spent', new_item, record, origin_csv)
    record = e_record
    clear_screen()
    print("Time spent successfully updated!\n")
    pause()

def edit_notes(record, origin_csv):
    clear_screen()
    print("Edit Notes")
    # must validate date
    new_item = input("> ")

    e_record = edit_item('notes', new_item, record, origin_csv)
    record = e_record
    clear_screen()
    print("Notes successfully updated!\n")
    pause()

def edit_record(record, origin_csv):
    editing = True
    origin_csv = origin_csv
    record = record

    while editing:
        clear_screen()
        print_record(record)
        edit_menu()

        edit_choice = input("> ")

        if edit_choice.lower() == "d":
            edit_date(record, origin_csv)

        if edit_choice.lower() == "t":
            edit_title(record, origin_csv)

        if edit_choice.lower() == "s":
            edit_time(record, origin_csv)     

        if edit_choice.lower() == "n":
            edit_notes(record, origin_csv)

        if edit_choice.lower() == "r
            break