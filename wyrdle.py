import logging
from random import choice 

from rich.console import Console
from rich.console import Theme

console = Console(width=100, theme=Theme({"warning": "red on yellow"}))


def main() -> None:
    """
    Description:
        This is a clone of the popular Wordle game. A player gets 6 guesses to guess
        a random 5 letter word. 
    """
    word_to_guess: str = get_guess_word()
    guesses_to_print: list[str] = []
    final_message: str = ""
    
    for guess_num in range(1,7):
        
        refresh_console(f"[bold blue]:computer: Guess: {guess_num} :computer:[/]\n")
        print_guesses(guesses_to_print)

        guess: str = get_guess()

        if not guess:
            final_message = f"[bold red]:skull: Failed to get a valid guess. Exiting game. :skull:[/]"
            break

        winner: int
        positions: list(int)
        winner, positions = check_guess(guess, word_to_guess)

        guesses_to_print.append(get_rich_formatted_str(positions, guess))

        if winner:
            final_message = f"[bold green]:exclamation: Congratulations! You have won! :exclamation:[/]"
            break            
    else:
        final_message = f"[bold red]:skull: Sorry you have lost! The word was {word_to_guess}. :skull:[/]"
    
    refresh_console(final_message)
    print_guesses(guesses_to_print)



def refresh_console(headline: str) -> None:
    """
    Description: 
        This refreshes the console and displays game information for the user.
    Arguments:
        headline: string, the headline to print at the top of the console.
    """
    console.clear()
    console.rule(headline)


def print_guesses(guesses_to_print: str) -> None:
    """
    Description:
        This prints the guesses to the display based on the following style.
    Arguments:
        guesses_to_print: str, a rich formatted string for printing each guess to the console.
    """
    for guess in guesses_to_print:
        console.print(guess, justify="center")


def get_rich_formatted_str(positions: list[int], guess: str) -> str:
    """
    Description:
        This function takes the last guess and creates a rich styled string. This will be
        used to print to the console.
    Arguments:
        postitions: list(int), a list of integers representing if the character is correct or not.
        guess: str, the guess made by the user.
    Returns:
        result: str, a string formatted for printing to the console using rich.
    """
    result: str = ""
    for position, guess_char in zip(positions, guess):
        if position == 0:
            result += (f"[white on #666666]{guess_char}[/]")
        elif position == 1:
            result += (f"[bold white on green]{guess_char}[/]")
        else:
            result += (f"[bold white on yellow]{guess_char}[/]")
    return result


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
    
    positions: list[int] = []
    for guess_char, word_to_guess_char in zip(guess,word_to_guess):
        if guess_char == word_to_guess_char:
            positions.append(1)
        elif guess_char in word_to_guess:
            positions.append(2)
        else:
            positions.append(0)

    return 0, positions


def get_guess() -> str | None:
    """
    Description:
        Get a valid guess from standard input. A valid guess is an 5
        letter words consisting of alphanumeric characters.
    Arguements:
        guess_num: int, the current guess number.
    Returns:
        guess: string, a valid guess.
    """
    for _ in range(5):
        guess: str = input(f"\nGuess a word: ").upper()

        if len(guess) != 5:
            console.print("Please enter a guess of length 5.")
        elif all([_.isalnum() for _ in guess]):
            return guess.upper()
        else:
            console.print("Please enter all alphanumeric characters.")
    
    console.print("Max number of guess attempts reached.")
    return None


def get_guess_word() -> str:
    """
    Description: This is a function that grabs the word that will be used 
    as the word to guess for the wyrdle game.

    Returns: A string representing the word to guess.
    """
    with open("wordlist.txt") as wordlist:
        word_to_guess: str = choice(wordlist.readlines())
        
    return word_to_guess.strip().upper()


if __name__ == "__main__":
    main()
