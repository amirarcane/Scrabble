import unittest
from collections import Counter

from utils.word_validator import WordValidator


class TestWordValidator(unittest.TestCase):
    """
    Unit tests for the WordValidator class.
    """

    def setUp(self):
        """
        Set up the WordValidator instance before each test.
        """
        self.validator = WordValidator()

    def test_is_valid_word_true(self):
        """
        Test is_valid_word method with a valid word.
        """
        letters = ['r', 't', 'o']
        word = 'rot'
        result = self.validator.is_valid_word(word, Counter(letters))
        self.assertTrue(result)

    def test_is_valid_word_false(self):
        """
        Test is_valid_word method with an invalid word.
        """
        letters = ['r', 't', 'o']
        word = 'root'
        result = self.validator.is_valid_word(word, Counter(letters))
        self.assertFalse(result)

    def test_validate_words(self):
        """
        Test validate_words method with a list of words.
        """
        letters = ['r', 't', 'o']
        words = ['rot', 'tor', 'root', 'to']
        result = self.validator.validate_words(words, letters)
        self.assertEqual(result, ['rot', 'tor', 'to'])


if __name__ == '__main__':
    unittest.main()
