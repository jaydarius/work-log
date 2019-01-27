import os

from datetime import datetime

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

while True:    
    try:
        # Give date of task
        
        print(
            "Date of the task\n"
            "Please use DD/MM/YYYY\n"
        )
        date_input = input("> ")
        # Ensure that date format is valid
        parsed_date = datetime.strptime(date_input, '%m/%d/%Y')
        
    except ValueError:
        print("\n{} doesn't seem to be a valid date and time.".format(date_input))
        os.system("pause")
        clear_screen()
    else:
        break
clear_screen()
print("move")
    

            