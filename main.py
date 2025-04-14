# Language learning flashcard CLI

import os
from src import manage_deck

DECK_DIR = "./data"

main_menu_selection = 0
decks = []

# Prints a menu list of options and returns the user's selection
def print_menu(options):
    # Print menu
    for idx, option in enumerate(options):
        print(f"({idx + 1}) {option}")

    # Prompt for user's selection until given a valid response
    menu_selection = 0
    while menu_selection <= 0 or menu_selection > len(options):
        menu_selection = int(input(f"Select a menu option (1-{len(options)}): "))

    # Return valid selection
    print("")
    return menu_selection

def capitalize_list(list):
    return [item.capitalize() for item in list]

# Loops until user exits
while True:
    print("\n-------MAIN MENU-------")
    # Create main menu
    # start with basic menu
    main_menu = capitalize_list(["create new deck", "exit program"])
    if not os.path.exists(DECK_DIR):
        os.mkdir(DECK_DIR)
    else: # add any existing decks
        decks = [d for d in os.listdir(DECK_DIR) if os.path.isfile(os.path.join(DECK_DIR, d))]
        for deck in decks:
            deck_name = deck[:-5].replace("_", " ").title()
            main_menu.insert(1, deck_name)
            
    # Print full main menu and get user's selection
    main_menu_selection = print_menu(main_menu)
    
    # Direct user to appropriate main menu selection
    if main_menu_selection == 1: # Create a deck
        print("Ok, let's create a new deck.")
        manage_deck.create_deck()
    elif main_menu_selection == len(main_menu): # Exit program
        print("Exiting flashcard program...\n")
        break
    else: # Open a deck
        # Set deck menu
        deck_options = capitalize_list(["edit deck", "search deck", "practice session", "delete deck", "exit deck"])
    
        while True:
            # Print deck name & options
            print(f"{main_menu[main_menu_selection - 1]} deck")
            deck_menu_selection = print_menu(deck_options)
            open_deck = decks[main_menu_selection - 2]
            
            # Direct user to appropriate deck menu selection
            match deck_menu_selection:
                case 1: # edit deck
                    print("Ok, which action would you like to take?")
                    edit_options = capitalize_list(["add cards", "delete cards", "return to deck menu"])
                    edit_selection = print_menu(edit_options)
                case 2: # search deck
                    print("search deck")
                case 3: # practice session
                    print("practice session")
                case 4: # delete deck
                    print("delete deck")
                case _:
                    print("Closing deck...")
                    break