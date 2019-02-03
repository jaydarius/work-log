import os

from datetime import datetime


def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def pause():
    # Wont work in Treehouse Workspaces :)
    cmd = "pause" if os.name == "nt" else "read -rsp $'Press any key to continue . . .\n' -n 1 key"
    os.system(cmd)
    return None


def get_date_from_user():
    while True: 
        try:  
            print( "Date of the task\nPlease use DD/MM/YYYY\n")
            date = input("> ")
            
            # Ensure that date format is valid
            parsed_date = datetime.strptime(date, '%d/%m/%Y')
            formatted_date = parsed_date.strftime('%d/%m/%Y')
            clear_screen()
            return formatted_date
        except ValueError:
            print("\n{} doesn't seem to be a valid date and time."
                  .format(date))
            pause()
            clear_screen()
            continue


if __name__ == "__main__":
    
    # testing returning parsed date instead of date
    doink = get_date_from_user()
    print(doink)