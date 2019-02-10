import os


def main_menu():
    print("== WORK LOG==\n"
          "What would you like to do?\n"
          "a) Add new entry\n"
          "b) Search existing entries\n"
          "c) Quit program\n")

def search_menu():
    print("== SEARCH MENU ==\n"
          "Do you want to search by:\n"
          "a) Exact Date\n"
          "b) Range of Dates\n"  
          "c) Exact Search\n"
          "d) Regex Pattern\n"
          "e) Time Spent\n"
          "f) Return to Main Menu\n")

def edit_menu():
    print("== EDIT MENU ==\n"
          "What would you like to edit?\n"
          "a) Date\n"
          "b) Title\n"
          "c) Time Spent\n"
          "d) Notes\n"
          "e) Return to Search Menu\n")

def page_menu(index, records):
    """Print page menu according to position on list of records
    
    :param index: integer of location on list
    :param records: list of records returned from search
    :return: None
    """
    
    if len(records) == 1:
        print("[E]dit, [D]elete, [R]eturn to Search Menu")
    elif index == (len(records)-1):
        print("[B]ack, [E]dit, [D]elete, [R]eturn to Search Menu")
    elif index == 0:
        print("[N]ext, [E]dit, [D]elete, [R]eturn to Search Menu")
    else:
        print("[N]ext, [B]ack, [E]dit, [D]elete, [R]eturn to Search Menu")


def print_record(record):
    print(f"Date: {record['date']}\n"
          f"Title: {record['title']}\n"
          f"Time Spent: {record['time_spent']}\n"
          f"Notes: {record['notes']}\n")

def invalid_input():
    print("\nNot a valid option!\n")
    pause()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def pause():
    """Pause the display until user enters a key and return None"""
    cmd = "pause" if os.name == "nt" else "read -rsp $'Press any key to continue . . .\n' -n 1 key"
    os.system(cmd)

