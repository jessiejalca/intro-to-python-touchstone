import re
import os

def create_dictionary(regex):
    dict_file = ""
    while re.match(dict_file, regex):
        # Get the learner and target languages, and build the dictionary's file name with them
        learner_lang = input("Learner language (the one you're starting from): ")
        target_lang = input("Target language (the one you're learning): ")
        dict_file = f"{learner_lang.lower()}_to_{target_lang.lower()}.json"
        
        # Check if the dictionary already exists
        filepath = f"./data/{dict_file}"
        if os.path.exists(filepath):
            print("That dictionary already exists.\n")
        # If not, create an empty json array
        else:
            dictionary = open(filepath, "x")
            dictionary.write('[]')
            dictionary.close()
            print(f"{learner_lang.capitalize()} to {target_lang.capitalize()} dictionary created.\n")
            