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

    # Find a card in the deck
    def find_card(self, phrase, lang):
        with open(self.file, 'r') as file:
            cards = json.load(file)
            for idx, card in enumerate(cards):
                if card.get(lang) == phrase:
                    return idx, card
            return -1, None

    # Delete the deck
    def delete_deck(self):
        os.remove(self.file)
        print(f"{self.name} deck deleted.")

    def practice_deck(self):
        pass
    
    # Print the card in a clear format
    def print_card(self, learner_phrase, target_phrase, sentences):
        print("-----------------")
        print(f"{self.learner}: {learner_phrase}")
        print(f"{self.target}: {target_phrase}")
        print("Example sentences:")
        for idx, sentence in enumerate(sentences):
            print(f"  ({idx + 1}) {sentence["learner"]} / {sentence["target"]}")
        print("-----------------")

    # Prompt the user to add a card to the deck
    def add_card(self):
        new_card = {
            "learner": "",
            "target": "",
            "sentences": [None] * 3
        }
        
        # Get a new word or phrase
        new_card["learner"] = input(f"Word or phrase in {self.learner}: ")
        card_idx, _ = self.find_card(new_card["learner"], "learner")
        if card_idx > -1:
            print("That card already exists. Try another phrase.")
            return
        
        # Get its translation in the target language
        new_card["target"] = input(f"Word or phrase in {self.target}: ")
        
        # Get 3 example sentences that use it
        print(f"Now use the word. Use the phrase first in {self.learner}, translate it to {self.target}.")
        for idx, sentence in enumerate(new_card["sentences"]):
            learner_sentence = input(f"  ({idx + 1}) {self.learner[:3]}: ")
            target_sentence = input(f"      {self.target[:3]}: ")
            sentence = {
                "learner": learner_sentence,
                "target": target_sentence
            }
            new_card["sentences"][idx] = sentence
                    
        # Print card 
        print("\nCard created:")
        self.print_card(new_card["learner"], new_card["target"], new_card["sentences"])
        
        # Check to confirm adding it to the deck
        confirmation = ""
        while confirmation != "y" and confirmation != "n":
            confirmation = input("Add to deck? (y/n) ")
        if confirmation == "y":
            # Get entire deck
            with open(self.file, 'r') as file:
                cards = json.load(file)
            # Append new card
            cards.append(new_card)
            # Update the json file
            with open(self.file, 'w') as file:
                json.dump(cards, file)
            # Update the user
            print(f"Success! Your card was added to your {self.name} deck.")
        else:
            print("No problem, it's discarded.")
        print("")

    def remove_card(self):
        pass
