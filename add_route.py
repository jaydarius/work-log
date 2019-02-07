from get_inputs import (get_date, get_title,
                        get_time, get_notes,
                        get_keyword, get_regex)

from csv_access import insert_record

from display import clear_screen, pause

def add_route():
    date = get_date()
    title = get_title()
    time_spent = get_time()
    notes = get_notes() 
    
    add_entry(date, title, time_spent, notes)
    clear_screen()
    print("The entry has been added!\n")
    pause()
        

def add_entry(date, title, time_spent, notes):
    record = {}
    record.update([
        ('date', date), 
        ('title', title),
        ('time_spent', time_spent),
        ('notes', notes)])
    insert_record(record, 'a')
