from random import choice 

def get_guess_word():
    """
    Description: This is a function that grabs the word that will be used 
    as the word to guess for the wyrdle game.

    Returns: A string representing the word to guess.
    """
    word_list = ["SNAKE", "AORTA", "TIGER", "LEMON"]
    return choice(word_list)


def main():
    """
    This is a clone of the popular Wordle game. A player gets 6 guesses to guess
    a random 5 letter word. 
    """
    word_to_guess = get_guess_word()

    for guess_num in range(1,7):
        guess = input(f"\nGuess {guess_num}: ").upper()
        
        if guess == word_to_guess:
            print("RIGHT!")
            break
        
        correct_letters = {
            letter for letter, correct in zip(guess, word_to_guess) if letter == correct
        }
        misplaced_letters = set(guess) & set(word_to_guess) - correct_letters
        wrong_letters = set(guess) - set(word_to_guess)

        print("Correct letters:", ", ".join(sorted(correct_letters)))
        print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
        print("Wrong letters:", ", ".join(sorted(wrong_letters)))
    else:
        print(f"The word was {word_to_guess}")


if __name__ == "__main__":
    main()
