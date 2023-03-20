from random import choice 

def get_guess_word() -> str:
    """
    Description: This is a function that grabs the word that will be used 
    as the word to guess for the wyrdle game.

    Returns: A string representing the word to guess.
    """
    word_list = ["SNAKE", "AORTA", "TIGER", "LEMON"]
    return choice(word_list)
