import os
import csv

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
    record = {}

    recs = open_csv('work-log.csv')
        
    for rec in recs:
        # if a record contains the date
        if rec['date'] == search:
        # return the row
            record = rec
    
    return record

# string is a search
# must pull up all records matching the string
# loop through each row
    # inside each row look at title and notes to contain the string
def keyword_search(search):
    record_list = []

    recs = open_csv('work-log.csv')
    
    for rec in recs:
        # if a row contains the search
        if search in rec['title']:
            record_list.append(rec)
        elif search in rec['notes']:
            record_list.append(rec)

    return record_list 

# TESTING!
if __name__ == "__main__":

    print(keyword_search('20'))

    
    