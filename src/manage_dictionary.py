import re
import os

def create_dictionary(valid_file):
    dict_file = ""
    while not re.match(dict_file, valid_file):
        learner_lang = input("Learner language (the one you're starting from): ")
        target_lang = input("Target language (the one you're learning): ")

        