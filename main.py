# Language learning flashcard CLI

import os
import re
from src import manage_deck

DECK_DIR = "./data"
SEARCH_RE = r'^(t|l):\s*(.+)'

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

# Accepts a list of strings to return capitalized
def capitalize_list(list):
    return [item.capitalize() for item in list]

# Stay or exit check
def stay_check(yn_question):
    stay = ""
    while stay != "y" and stay != "n":
        stay = input(f"{yn_question} (y/n) ")
    if stay == "n":
        print("Returning to deck menu...\n")
        return False
    return True

# Loops until user exits
while True:
    print("\n-------MAIN MENU-------")
    # Create main menu
    # start with basic menu
    main_menu = capitalize_list(["create new deck", "exit program"])
    if not os.path.exists(DECK_DIR):
        os.mkdir(DECK_DIR)
    else: # add any existing decks
        files = [d for d in os.listdir(DECK_DIR) if os.path.isfile(os.path.join(DECK_DIR, d))]
        for file in files:
            # parse info
            deck_name = file[:-5].replace("_", " ").title()
            langs = deck_name.split(" To ")
            # add existing decks
            decks.insert(0, manage_deck.Deck(langs[0], langs[1], deck_name, DECK_DIR + "/" + file))
            # insert into menu
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
        deck_options = capitalize_list(["add cards", "remove cards", "search deck", "practice session", "delete deck", "exit deck"])
    
        while True:
            # Print deck name & options
            print(f"{main_menu[main_menu_selection - 1]} deck")
            
            # Get user selection & save deck
            open_deck = decks[main_menu_selection - 2]
            deck_menu_selection = print_menu(deck_options)
            
            # Direct user to appropriate deck menu selection
            match deck_menu_selection:
                case 1: # add cards
                    print(f"Add to {open_deck.name} deck:")
                    while True:
                        open_deck.add_card()
                        # Check if the user wants to continue or not
                        if not stay_check("Add another card?"):
                            break

                case 2: # remove cards
                    print(f"Remove cards from {open_deck.name} deck:")
                    print(f"To search by your learner language ({open_deck.learner}), prefix with \"l:\"")
                    print(f"To search by your target language ({open_deck.target}), prefix with \"t:\"")
                    while True:
                        # Get the card to remove
                        remove_input = input("\nWord or phrase to remove: ").strip()
                        match = re.match(SEARCH_RE, remove_input)
                        # Parse the input
                        if match:
                            prefix = match.group(1)
                            phrase = match.group(2)
                            lang = "learner" if prefix == "l" else "target"
                            # Find the card
                            idx, _ = open_deck.find_card(phrase, lang)
                            if idx > -1:
                                # Remove the card if found
                                open_deck.remove_card(idx)
                            else:
                                # Tell the user if it wasn't found
                                print("Card not found.\n")
                        else:
                            # Remind the user of correct usage
                            print("Can't parse phrase or language. Remember to use syntax like this: \"l:to eat\" or \"t:manger\"")
                        # Check if the user wants to continue or not
                        if not stay_check("Remove another card?"):
                            break
                        
                case 3: # search deck
                    print(f"Find cards in {open_deck.name} deck:")
                    print("Input the word or phrase you want to remove from the deck.")
                    print(f"To search by your learner language ({open_deck.learner}), prefix with \"l:\"")
                    print(f"To search by your target language ({open_deck.target}), prefix with \"t:\"")
                    while True:
                        # Get the card to search
                        search_input = input("\nWord or phrase to find: ").strip()
                        match = re.match(SEARCH_RE, search_input)
                        # Parse the input
                        if match:
                            prefix = match.group(1)
                            phrase = match.group(2)
                            lang = "learner" if prefix == "l" else "target"
                            # Find the card in the deck
                            _, card = open_deck.find_card(phrase, lang)
                            if card == None:
                                print("Card not found.\n")
                            else:
                                # Print the card
                                open_deck.print_card(card["learner"], card["target"], card["sentences"])
                        else:
                            # Remind the user of correct usage
                            print("Can't parse phrase or language. Remember to use syntax like this: \"l:to eat\" or \"t:manger\"")
                        # Check if the user wants to continue or not
                        if not stay_check("Search again?"):
                            break
                        
                case 4: # practice session
                    print("practice session")
                    
                case 5: # delete deck
                    open_deck.delete_deck()
                    break
                
                case _:
                    print("Closing deck...\n")
                    break