import wyrdle

class TestWyrdle:

    def test_get_guess_word(self):
        word_list = ["SNAKE", "AORTA", "TIGER", "LEMON"]
        assert wyrdle.get_guess_word() in word_list
