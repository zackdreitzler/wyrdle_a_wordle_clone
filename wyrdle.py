def get_guess_word():
    """
    Description: This is a function that grabs the word that will be used as the correct
    word for the wyrdle game.

    Returns: A string representing the word to guess.
    """
    return "SNAKE"

if __name__ == "__main__":
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
