import get_word

class TestGetWord:

    def test_get_guess_word(self):
        word_list = ["SNAKE", "AORTA", "TIGER", "LEMON"]
        assert get_word.get_guess_word() in word_list

