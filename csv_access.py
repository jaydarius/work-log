import os
import csv
import re
import copy

from display import print_record, clear_screen, pause

def open_csv(csv_file):
    records = []

    with open(csv_file, newline='') as f:
        fieldnames = ['date', 'title', 'time_spent', 'notes']
        reader = csv.DictReader(f, fieldnames=fieldnames)
        records = list(reader)
    
    return records

def insert_record(record, permission):
    with open('work-log.csv', permission, newline='') as f:
        fieldnames = ['date', 'title', 'time_spent', 'notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
    
        writer.writerow(record)

# open work-log.csv and use date criteria to return records 
def date_search(search):
    records = []

    recs = open_csv('work-log.csv')
        
    for rec in recs:
        # if a record contains the date
        if rec['date'] == search:
        # return the row
            records.append(rec)
    
    return records

# open work-log.csv and use keyword criteria to return records 
def keyword_search(search):
    records = []

    recs = open_csv('work-log.csv')
    
    for rec in recs:
        # if a row contains the search
        if search in rec['title']:
            records.append(rec)
        elif search in rec['notes']:
            records.append(rec)

    return records

# open work-log.csv and use regex criteria to return records 
def regex_search(search):
    data = ""
    records = []
    search = str(search)
    
    recs = open_csv('work-log.csv')
    
    # for each record apply a regex search.
    for rec in recs:
        if re.findall(r'{}'.format(search), rec['title']):
            records.append(rec)
        elif re.findall(r'{}'.format(search), rec['notes']):
            records.append(rec)
    
    return records

# open work-log.csv and use time criteria to return records 
def time_search(search):
    records = []
    search = str(search)

    recs = open_csv('work-log.csv')
        
    for rec in recs:
        # if a record contains the date
        if rec['time_spent'] == search:
        # return the row
            records.append(rec)
    
    return records    


def del_record(record, origin_csv):
    # origin csv is inside show_each_record_one_at_a_time
    os.remove("work-log.csv")

    for r in origin_csv:
        if r != record:
            insert_record(r, 'a')

def edit_item(key, value, record, origin_csv):  # item is 1 of 4 record values
    e_record = copy.copy(record)  # copy the origin record

    e_record[key] = value

    del_record(record, origin_csv)
    insert_record(e_record, 'a')
    return e_record

def edit_menu(record, origin_csv):
    editing = True

    while editing:
        clear_screen()
        print_record(record)
        print("What would you like to edit?\n"
              "[D]ate\n"
              "[T]itle\n"
              "Time [S]pent\n"
              "[N]otes\n"
              "[R]eturn to Search Menu\n")

        edit_choice = input("> ")

        if edit_choice.lower() == "d":
            clear_screen()
            print("Edit Date")
            # must validate date
            new_item = input("> ")

            e_record = edit_item('date', new_item, record, origin_csv)
            record = e_record
            clear_screen()
            print("Date successfully updated!\n")
            pause()

        if edit_choice.lower() == "t":
            clear_screen()
            print("Edit Title")
            # must validate date
            new_item = input("> ")

            e_record = edit_item('title', new_item, record, origin_csv)
            record = e_record
            clear_screen()
            print("Title successfully updated!\n")
            pause()


        if edit_choice.lower() == "s":
            clear_screen()
            print("Edit Time Spent")
            # must validate
            new_item = input("> ")

            e_record = edit_item('time_spent', new_item, record, origin_csv)
            record = e_record
            clear_screen()
            print("Time spent successfully updated!\n")
            pause()

        if edit_choice.lower() == "n":
            clear_screen()
            print("Edit Notes")
            # must validate date
            new_item = input("> ")

            e_record = edit_item('notes', new_item, record, origin_csv)
            record = e_record
            clear_screen()
            print("Notes successfully updated!\n")
            pause()

        if edit_choice.lower() == "r":
            break

# TESTING!
if __name__ == "__main__":
   
    print(time_search(90))
    
    