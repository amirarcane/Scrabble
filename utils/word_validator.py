from collections import Counter
from typing import List


class WordValidator:
    """
    Class responsible for validating words based on provided letters.
    """

    def is_valid_word(self, word: str, letter_counts: Counter) -> bool:
        """
        Checks if a word is valid by ensuring it uses only the provided letters
        and does not exceed the count of any letter.

        Args:
            word (str): The word to validate.
            letter_counts (Counter): Counter of available letters.

        Returns:
            bool: True if the word is valid, False otherwise.
        """
        word = word.lower()
        word_letter_counts = Counter(word)
        for letter, count in word_letter_counts.items():
            if letter_counts.get(letter, 0) < count:
                return False
        return True

    def validate_words(self, words: List[str], letters: List[str]) -> List[str]:
        """
        Filters a list of words, returning only those that are valid.

        Args:
            words (List[str]): List of words to validate.
            letters (List[str]): List of available letters.

        Returns:
            List[str]: List of valid words.
        """
        letter_counts = Counter(letters)
        valid_words = [word for word in words if self.is_valid_word(word, letter_counts)]
        return valid_words
