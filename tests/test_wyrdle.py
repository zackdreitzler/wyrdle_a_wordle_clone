import wyrdle
from pytest import raises

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
