import os
import csv

def csv_insert(work_log):
    with open('work-log.csv', 'a', newline='') as f:
        fieldnames = ['date', 'title', 'time_spent', 'notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
    
        writer.writerow(work_log)

def csv_read():
    with open('work-log.csv', newline='') as f:
        fieldnames = ['date', 'title', 'time_spent', 'notes']
        reader = csv.DictReader(f, fieldnames=fieldnames)
        rows = list(reader)
        
        for row in rows:
            # if a row contains the search
            # if row[0] == '7/20/2033':
            # print the row
            print(row['date'])
             

# TESTING!
if __name__ == "__main__":
    work_log = {}

    work_log.update([
        ('date', '1/30/2020'), 
        ('title', 'Test Title'),
        ('time_spent', '45'),
        ('notes', 'Testing is fun, pal')
    ])

    work_log2 = {
        'date': '7/20/2033', 
        'title': 'Record',
        'time_spent': 20,
        'notes': ''
    }

    csv_insert(work_log2)

    csv_read()