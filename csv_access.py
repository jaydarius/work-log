import os
import csv
import re


def open_csv(csv_file):
    records = []

    with open(csv_file, newline='') as f:
        fieldnames = ['date', 'title', 'time_spent', 'notes']
        reader = csv.DictReader(f, fieldnames=fieldnames)
        records = list(reader)
    
    return records

def insert_record(work_log):
    with open('work-log.csv', 'a', newline='') as f:
        fieldnames = ['date', 'title', 'time_spent', 'notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
    
        writer.writerow(work_log)

def date_search(search):
    records = []

    recs = open_csv('work-log.csv')
        
    for rec in recs:
        # if a record contains the date
        if rec['date'] == search:
        # return the row
            records.append(rec)
    
    return records

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

# TESTING!
if __name__ == "__main__":

    print(time_search(90))
    
    