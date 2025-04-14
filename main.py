# Language learning flashcard CLI

import os
import re
from src import manage_deck
from src import menus

DECK_DIR = "./data"

main_menu_selection = 0
decks = []

while True:
    print("\n-------MAIN MENU-------")
    # Create main menu
    # start with basic menu
    main_menu = ["create new deck", "exit program"]
    main_menu = [option.capitalize() for option in main_menu]
    if not os.path.exists(DECK_DIR):
        os.mkdir(DECK_DIR)
    # add any existing decks
    else:
        decks = [d for d in os.listdir(DECK_DIR) if os.path.isfile(os.path.join(DECK_DIR, d))]
        for deck in decks:
            deck_name = deck[:-5].replace("_", " ").title()
            main_menu.insert(1, deck_name)
            
    # Print full main menu and get user's selection
    main_menu_selection = menus.print_menu(main_menu)
    
    # Direct user to appropriate menu selection
    if main_menu_selection == 1:
    # create a deck
        print("Ok, let's create a new deck")
        manage_deck.create_deck()
    elif main_menu_selection == len(main_menu):
    # exit program
        print("Exiting flashcard program...\n")
        break
    else:
    # Open a deck
        # print chosen deck name
        print(f"Opening {main_menu[main_menu_selection - 1]} deck...")
        
        # print deck menu
        deck_options = ["edit deck", "search deck", "practice vocabulary", "delete deck", "exit deck"]
        deck_options = [option.capitalize() for option in deck_options]
        deck_menu_selection = menus.print_menu(deck_options)
    
    