# Language learning flashcard CLI

import os
import re
from src import manage_dictionary
from src import menus

DICT_DIR = "./data"

main_menu_selection = 0
dictionary_regex = "[a-z]+_to_[a-z]+\.json"

while True:
    # Create main menu
    # start with basic menu
    main_menu = ["create new dictionary", "exit"]
    if not os.path.exists(DICT_DIR):
        os.mkdir(DICT_DIR)
    # add any existing dictionaries
    else:
        files = [f for f in os.listdir(DICT_DIR) if os.path.isfile(os.path.join(DICT_DIR, f))]
        dictionary_files = [d for d in files if re.match(dictionary_regex)]
        dictionaries = []
        for dict_file in dictionary_files:
            dict_name = dict_file[:-5].replace("_", " ")
            main_menu.insert(1, dict_name)
            
    # Print full main menu
    menus.print_menu(main_menu)
    
    
    
    
    break
    