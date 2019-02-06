import os

def main_menu():
    print("== WORK LOG==\n"
          "What would you like to do?\n"
          "a) Add new entry\n"
          "b) Search existing entries\n"
          "c) Quit program\n")

def search_menu():
    print("Do you want to search by:\n"
          "a) Exact Date\n"
          "b) Range of Dates\n"  #extra credit
          "c) Exact Search\n"
          "d) Regex Pattern\n"
          "e) Time Spent\n"
          "f) Return to Main Menu\n")

def edit_menu():
    print("What would you like to edit?\n"
          "[D]ate\n"
          "[T]itle\n"
          "Time [S]pent\n"
          "[N]otes\n"
          "[R]eturn to Search Menu\n")

def print_record(record):
    print(f"Date: {record['date']}\n"
          f"Title: {record['title']}\n"
          f"Time Spent: {record['time_spent']}\n"
          f"Notes: {record['notes']}\n")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def pause():
    # Wont work in Treehouse Workspaces :)
    cmd = "pause" if os.name == "nt" else "read -rsp $'Press any key to continue . . .\n' -n 1 key"
    os.system(cmd)
    return None
