

if __name__ == "__main__":
    word_to_guess = get_guess_word()

    for guess_num in range(1,7):
        guess = input("Guess a five letter word: ").upper()
        
        if guess.upper() == "SNAKE":
            print("RIGHT!")
            break
        else:
            print("WRONG!")


def get_guess_word():
    """
    Description: This is a function that grabs the word that will be used as the correct
    word for the wyrdle game.

    Returns: A string representing the word to guess.
    """
    return "SNAKE"
