import re
import os

DECK_RE = r"[a-z]+_to_[a-z]+\.json"

def create_deck():
    deck_file = ""
    while re.match(deck_file, DECK_RE):
        # Get the learner and target languages, and build the deck's file name with them
        learner_lang = input("Learner language (the one you're starting from): ")
        target_lang = input("Target language (the one you're learning): ")
        deck_file = f"{learner_lang.lower()}_to_{target_lang.lower()}.json"
        
        # Check if the deck already exists
        filepath = f"./data/{deck_file}"
        if os.path.exists(filepath):
            print("That deck already exists.\n")
        # If not, create an empty json array
        else:
            deck = open(filepath, "x")
            deck.write('[]')
            deck.close()
            print(f"{learner_lang.capitalize()} to {target_lang.capitalize()} deck created.\n")
            