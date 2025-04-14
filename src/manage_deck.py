import re
import os
import json

DECK_RE = r"[a-z]+_to_[a-z]+\.json"

def create_deck():
    deck_file = ""
    while re.match(deck_file, DECK_RE):
        # Get the learner and target languages, and build the deck's file name with them
        learner_lang = input("Learner language (the one you're starting from): ").capitalize()
        target_lang = input("Target language (the one you're learning): ").capitalize()
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
            deck_name = f"{learner_lang} to {target_lang}".title()
            print(f"{deck_name} deck created.\n")
            

class Deck:
    def __init__(self, learner, target, name, file):
        self.learner = learner
        self.target = target
        self.name = name
        self.file = file

    def search_deck(self, phrase, lang):
        pass

    def delete_deck(self):
        os.remove(self.file)
        print(f"{self.name} deck deleted.")

    def practice_deck(self):
        pass

    def add_cards(self):
        pass

    def delete_cards(self):
        pass
