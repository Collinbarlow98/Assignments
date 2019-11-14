import unittest

class Palindrometest(unittest.TestCase):

    def setUp(self):
        self.word = "word"
        self.reversed_word = ""

    def test_reverse_word(self):
        for index in range(len(self.word) - 1, -1, -1):
            self.reversed_word += self.word[index]

    def test_reverse_word_to_word(self):
        if self.reversed_word == self.word:
            print("Palindrome")
        elif self.reversed_word != self.word:
            print("Not Palindrome")

unittest.main()
