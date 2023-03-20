from get_word import get_guess_word

def check_guess(guess: str, word_to_guess: str) -> bool | list[int]:
    """
    Description: 
        This function checks to see if the user's guess matches the
        word to guess.
    Arguments:
        guess: string, the word the user has guessed.
        word_to_guess: string, the word the user needs to guess.
    Returns: 
        winner: bool, true if word_to_guess and guess match.
        positions: list[int], list containing the state of each character in guess 
            versus the word to guess. 
            
            0 means its not in the word to guess.
            1 means the characters match.
            2 means the character is in the word to guess but in a different position.

            Example: 
                guess           = "Sneak" 
                word_to_guess   = "Shack"

                winner = 0
                positions = [1, 0, 2, 0, 1]

    """
    if guess == word_to_guess: 
        return 1, [1]*5
    
    positions = []
    for index in range(len(word_to_guess)):
        if guess[index] == word_to_guess[index]:
            positions.append(1)
        elif guess[index] in word_to_guess:
            positions.append(2)
        else:
            positions.append(0)

    return 0, positions


def main():
    """
    Description:
        This is a clone of the popular Wordle game. A player gets 6 guesses to guess
        a random 5 letter word. 
    """
    word_to_guess = get_guess_word()

    for guess_num in range(1,7):
        guess = input(f"\nGuess {guess_num}: ").upper()
        
        winner, positions = check_guess(guess, word_to_guess)

        if winner:
            print(f"Congrats! You Won!")
            break

        print(positions)
            
    else:
        print(f"The word was {word_to_guess}")


if __name__ == "__main__":
    main()
