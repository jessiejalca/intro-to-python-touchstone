# Language learning flashcard CLI

import os
import re
from src import manage_dictionary
from src import menus

DICT_DIR = "./data"
DICT_RE = r"[a-z]+_to_[a-z]+\.json"

main_menu_selection = 0
dictionary_files = []
dictionaries = []

while True:
    print("\n-------MAIN MENU-------")
    # Create main menu
    # start with basic menu
    main_menu = ["create new dictionary", "exit program"]
    if not os.path.exists(DICT_DIR):
        os.mkdir(DICT_DIR)
    # add any existing dictionaries
    else:
        files = [f for f in os.listdir(DICT_DIR) if os.path.isfile(os.path.join(DICT_DIR, f))]
        dictionary_files = [d for d in files if re.match(DICT_RE)]
        for dict_file in dictionary_files:
            dict_name = dict_file[:-5].replace("_", " ")
            main_menu.insert(1, dict_name)
            
    # Print full main menu and get user's selection
    main_menu_selection = menus.print_menu(main_menu)
    
    # Direct user to appropriate menu selection
    if main_menu_selection == 1:
        print("Ok, let's create a new dictionary")
        manage_dictionary.create_dictionary(DICT_RE)
    elif main_menu_selection == len(main_menu):
        print("Exiting flashcard program...")
        break
    else:
        dictionary_options = ["edit dictionary", "search dictionary", "practice vocabulary", "delete dictionary", "exit dictionary"]
        dict_menu_selection = menus.print_menu(dictionary_options)
    
    break
    