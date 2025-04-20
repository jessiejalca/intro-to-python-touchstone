import re
import os
import json
import random

DECK_RE = r"[a-z]+_to_[a-z]+\.json"

def create_deck():
    deck_file = ""
    while not re.match(DECK_RE, deck_file):
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
        # Check if the file exists and is not empty
        if not os.path.exists(self.file) or os.path.getsize(self.file) == 0:
            return -1, None
        with open(self.file, 'r') as file:
            try:
                cards = json.load(file)
            except json.JSONDecodeError:
                print("Warning: Deck file is corrupted or empty.")
                return -1, None

            for idx, card in enumerate(cards):
                if card.get(lang) == phrase:
                    return idx, card
            return -1, None

    # Delete the deck
    def delete_deck(self):
        os.remove(self.file)
        print(f"{self.name} deck deleted.")

    # Practice the deck
    def practice_deck(self):
        correct = 0
        incorrect = 0
        stack = [None] * 20
        
        # Give the user instructions
        print(f"For each sentence in {self.learner}, translate it to {self.target}. Then hit 'enter' to flip the card and check your answer.")

        # Get the cards and the size of the deck to get a range
        with open(self.file, 'r') as file:
            cards = json.load(file)
            total = len(cards)
        # Randomly select cards within the range
        for i, _ in enumerate(stack):
            stack[i] = random.randint(0, total - 1)
        # Go through the stack
        for idx in stack:
            # Randomly choose a sentence from the card
            rand_sentence = random.randint(0, 2)
            card = cards[idx]
            # Print a sentence for the user to translate
            print("\n-----------------")
            print(f"({card["learner"]}) {card["sentences"][rand_sentence]["learner"]}")
            input("-----------------")
            # Print the other side
            print(f"({card["target"]}) {card["sentences"][rand_sentence]["target"]}")
            print("-----------------")
            # See if the user got it right
            confirmation = ""
            while confirmation != "y" and confirmation != "n":
                confirmation = input("Did you get it right? (y/n) ")
            if confirmation == "y":
                correct += 1
            else:
                incorrect += 1
        
        # Print the stats
        print("")
    
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

    # Remove a card from the deck given an index
    def remove_card(self, index):
        # Load the deck
        with open(self.file, 'r') as file:
            cards = json.load(file)
        # Print the card
        self.print_card(cards[index]["learner"], cards[index]["target"], cards[index]["sentences"])
        # Make sure the user wants to remove the card
        confirmation = input("Are you sure you want to remove this card? (y/n) ")
        if confirmation == "y":
            # Remove the card from the deck
            cards.pop(index)
            # Update the file
            with open(self.file, 'w') as file:
                json.dump(cards, file)
                print("Card removed.\n")
