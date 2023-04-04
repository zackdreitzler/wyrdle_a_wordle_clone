import wyrdle

class TestWyrdle:

    def test_check_guess_not_winner(self):
        """
        Description:
            This test checks to make sure the check_guess function correctly 
            assigns a not winner condition with the correct values in the
            positions list.
        """
        word_to_guess = "SNAKE"
        guess = "SHIRK"

        winner, positions = wyrdle.check_guess(guess, word_to_guess)
        assert not winner 
        assert positions == [1, 0, 0, 0, 2]


    def test_check_guess_winner(self):
        """
        Description:
            This test checks to make sure the check_guess function correctly 
            assigns a winner condition with the correct values in the
            positions list.
        """
        word_to_guess = "SNAKE"
        guess = "SNAKE"

        winner, positions = wyrdle.check_guess(guess, word_to_guess)
        assert winner 
        assert positions == [1, 1, 1, 1, 1]
    
    def test_get_guess_success(self, monkeypatch):
        """
        This test checks to make sure we receive a valid input from the 
        user. 
        
        A valid input is a string of 5 alphanumeric characters.
        """
        monkeypatch.setattr('builtins.input', lambda _: "SNEAK")
        guess = wyrdle.get_guess()
        assert guess == "SNEAK"

    def test_get_guess_not_all_alphanumeric(self, monkeypatch, capsys):
        """
        This test checks to make sure we receive a the default input and
        the print message about alphanumeric characters after a user 
        fails to input a valid input. 
        
        A valid input is a string of 5 alphanumeric characters.
        """
        monkeypatch.setattr('builtins.input', lambda _: "@@@@@")
        guess = wyrdle.get_guess()
        captured_output = capsys.readouterr()
        assert guess == "ABCDE"
        assert "Please enter all alphanumeric characters." in captured_output.out
        assert "Max number of guess attempts reached." in captured_output.out

    def test_get_guess_incorrect_length(self, monkeypatch, capsys):
        """
        This test checks to make sure we receive a the default input and
        the print message about alphanumeric characters after a user 
        fails to input a valid input. 
        
        A valid input is a string of 5 alphanumeric characters.
        """
        monkeypatch.setattr('builtins.input', lambda _: "ABCDEF")
        guess = wyrdle.get_guess()
        captured_output = capsys.readouterr()
        assert guess == "ABCDE"
        assert "Please enter a guess of length 5." in captured_output.out
        assert "Max number of guess attempts reached." in captured_output.out

    def test_get_rich_formatted_str(self):
        """
        This test confirms that each character in  a guess is properly formatted
        for output by the rich console.
        """
        guess = 'HELLO'
        positions = [0,1,2,0,0]
        output = wyrdle.get_rich_formatted_str(positions, guess)
        assert output == "[white on #666666]H[/][bold white on green]E[/][bold white on yellow]L[/][white on #666666]L[/][white on #666666]O[/]"

    def test_get_guess_word(self):
        """
        This test confirms that get_guess_word returns a valid word from the word list.
        A valid word is one that is of length 5 and consists of all alphanumeric characters.
        """
        word_to_guess = wyrdle.get_guess_word()
        with open("wordlist.txt") as wordlist:
            word_list = list(wordlist.readlines())

        assert len(word_to_guess) == 5
        assert all([letter.isalnum() for letter in word_to_guess])
        assert word_to_guess + '\n' in word_list