import os
import csv
import re
import copy

from display import (
    print_record,
    clear_screen,
    pause
)


def open_csv(csv_file):
    """Open work-log.csv and return a list of records.
    
    :param csv_file: string containing file in directory to open
    """
    try:
        records = []

        with open(csv_file, newline='') as f:
            fieldnames = ['date', 'title', 'time_spent', 'notes']
            reader = csv.DictReader(f, fieldnames=fieldnames)
            records = list(reader)
        
        return records
    except FileNotFoundError:
        return False
        pause()

def insert_record(record, permission):
    """Adds a record to the CSV file.

    :param record: dictionary containing the required fieldnames
        date, title, time_spent, notes
    :param permission: string containing file-mode to open the file with i.e 'a'
    :return: None
    """

    with open('work-log.csv', permission, newline='') as f:
        fieldnames = ['date', 'title', 'time_spent', 'notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
    
        writer.writerow(record)

def date_search(search):
    """Search the csv for all records that match a date.

    :param search: a string containing user's search criteria
    :return: a list of the found records
    """

    records = []
    recs = open_csv('work-log.csv')
        
    for rec in recs:
        if rec['date'] == search:
            records.append(rec)
    
    return records

def date_range_search(search):
    """Search the csv for all records inside a date range.

    :param search: a string containing user's search criteria
    :return: a list of the found records
    """

    records = []
    recs = open_csv('work-log.csv')
        
    for rec in recs:
        if rec['date'] in search:
            records.append(rec)
    
    return records


def keyword_search(search):
    """Search the csv for all records that match a keyword.

    :param search: a string containing user's search criteria
    :return: a list of the found records
    """

    records = []
    recs = open_csv('work-log.csv')
    
    for rec in recs:
        if search in rec['title']:
            records.append(rec)
        elif search in rec['notes']:
            records.append(rec)

    return records

def regex_search(search):
    """Search the csv for all records that match a RegEx.

    :param search: a string containing user's search criteria
    :return: a list of the found records
    """

    records = []
    search = str(search)
    recs = open_csv('work-log.csv')
    
    for rec in recs:
        if re.findall(r'{}'.format(search), rec['title']):
            records.append(rec)
        elif re.findall(r'{}'.format(search), rec['notes']):
            records.append(rec)
    
    return records

def time_search(search):
    """Search the csv for all records that match a unit of time.

    :param search: an integer containing user's search criteria
    :return: list of the found records
    """
    
    records = []
    search = str(search)
    recs = open_csv('work-log.csv')
        
    for rec in recs:
        if rec['time_spent'] == search:
            records.append(rec)
    
    return records    

def del_record(record, origin_csv):
    """
    Remove work-log.csv and copy its records to a new work-log.csv
    excluding the record marked for deletion.

    :param record: dictionary marked for delection
    :param origin_csv: list of records in work-log.csv 
    :return: None
    """

    os.remove("work-log.csv")

    for r in origin_csv:
        if r != record:
            insert_record(r, 'a')

def edit_item(key, value, record, origin_csv): 
    """
    Create a copy of origin record, edit it's key's value, 
    delete origin record, and insert the edited copy into work-log.csv

    :param key: string of record that will be selected 
    :param value: string of record that will be edited
    :param record: dictionary marked for editing
    :param origin_csv: list of records in work-log.csv  
    :return: dictionary of the edited record
    """

    e_record = copy.copy(record) 
    e_record[key] = value

    del_record(record, origin_csv)
    insert_record(e_record, 'a')

    return e_record


# TESTING!
if __name__ == "__main__":
   
    print(time_search(90))
    
    