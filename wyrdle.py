from get_word import get_guess_word

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
    guesses_to_print: str = ""
    for guess_num in range(1,7):
        
        refresh_console(f"Guess: {guess_num}")
        print_guesses(guesses_to_print)

        guess: str = get_guess()
        winner, positions = check_guess(guess, word_to_guess)

        guesses_to_print += get_rich_formatted_str(positions, guess)

        if winner:
            print(f"Congrats! You Won!")
            break            
    else:
        print(f"The word was {word_to_guess}")


def refresh_console(headline: str) -> None:
    """
    Description: 
        This refreshes the console and displays game information for the user.
    Arguments:
        headline: string, the headline to print at the top of the console.
    """
    console.clear()
    console.rule(f"[bold blue]:computer: {headline} :computer:[/]\n")


def print_guesses(guesses_to_print: str) -> None:
    """
    Description:
        This prints the guesses to the display based on the following style.
    Arguments:
        guesses_to_print: str, a rich formatted string for printing each guess to the console.
    """
    console.print(guesses_to_print, justify="center")


def get_rich_formatted_str(positions: list(int), guess: str) -> str:
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
    for p, g in positions, guess:
        if p == 0:
            result += (f"[white on #666666]{g}[/]")
        elif p == 1:
            result += (f"[bold white on green]{g}[/]")
        else:
            result += (f"[bold white on yellow]{g}[/]")
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
    for _ in range(len(word_to_guess)):
        if guess[_] == word_to_guess[_]:
            positions.append(1)
        elif guess[_] in word_to_guess:
            positions.append(2)
        else:
            positions.append(0)

    return 0, positions


def get_guess() -> str:
    """
    Description:
        Get a valid guess from standard input. A valid guess is an 5
        letter words consisting of alphanumeric characters.
    Arguements:
        guess_num: int, the current guess number.
    Returns:
        guess: string, a valid guess.
    """
    for _ in range(100):
        guess: str = input(f"\nGuess a word: ").upper()

        if len(guess) != 5:
            print("Please enter a guess of length 5.", flush=True)
        elif all([_.isalnum() for _ in guess]):
            return guess.upper()
        else:
            print("Please enter all alphanumeric characters.", flush=True)
    
    print("Max number of guess attempts reached.")
    return 'ABCDE'


if __name__ == "__main__":
    main()
