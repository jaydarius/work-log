import os
import csv
from datetime import datetime


from display import (
    main_menu,
    clear_screen, 
    invalid_input
)
from search_route import (
    search_records,
    page_records,
    search_route
)
from add_route import add_route


if __name__ == "__main__":
    clear_screen()
        
    logging = True
    
    while logging:
        clear_screen()
        main_menu()
        
        choice = input("> ")
        choice = choice.lower()

        clear_screen()

        # Follow the 'Add new entry' route
        if choice == "a":
            add_route()

        elif choice == "b":
            search_route()

        elif choice == "c":
            print("Thanks for using the Work Log! See ya soon.")
            break

        else:
            invalid_input()
        
