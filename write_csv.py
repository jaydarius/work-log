import os
import csv

def csv_insert(work_log):
    with open('work-log.csv', 'a') as f:
        fieldnames = ['date', 'title', 'time_spent', 'notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
    
        writer.writerow(work_log)

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
        'title': 'Boom Dyna',
        'time_spent': 20,
        'notes': ''
    }

    csv_insert(work_log2)