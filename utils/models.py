from typing import List


class GenerateWordRequest:
    """
    Data model for the word generation request.

    Attributes:
        letters (List[str]): List of letters provided by the user.
        language (str): The language in which to generate words.
    """

    def __init__(self, letters: List[str], language: str):
        self.letters = letters
        self.language = language

    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates an instance of GenerateWordRequest from a dictionary.

        Args:
            data (dict): Dictionary containing 'letters' and 'language' keys.

        Returns:
            GenerateWordRequest: An instance of the request model.
        """
        return cls(
            letters=data.get('letters', []),
            language=data.get('language', '')
        )


class GenerateWordResponse:
    """
    Data model for the word generation response.

    Attributes:
        words (List[str]): List of valid words generated.
    """

    def __init__(self, words: List[str]):
        self.words = words

    def to_dict(self):
        """
        Converts the response object to a dictionary.

        Returns:
            dict: Dictionary representation of the response.
        """
        return {'words': self.words}
