import logging
from typing import List

from openai import AzureOpenAI

from config import Config

logger = logging.getLogger(__name__)


class OpenAIHelper:
    """
    Helper class for interacting with the OpenAI API.
    """

    def __init__(self):
        """
        Initializes the OpenAIHelper with the API key.
        """
        self.client = AzureOpenAI(
            api_key=Config.OPENAI_API_KEY,
            api_version="2024-02-01",
            azure_endpoint="https://ai-homework.openai.azure.com/"
        )

        if not self.client.api_key:
            logger.error("OpenAI API key not set")
            raise Exception("OpenAI API key not set")

    def construct_prompt(self, letters: List[str], language: str) -> str:
        """
        Constructs the prompt to be sent to the OpenAI API.

        Args:
            letters (List[str]): List of letters provided by the user.
            language (str): The language in which to generate words.

        Returns:
            str: The constructed prompt string.
        """
        letters_str = ', '.join(letters)
        prompt = (
            f"Return the longest possible valid words in {language} using only the letters provided."
            f"The letters are: {letters_str}. "
            f"Each letter can be used at most as many times as it appears in the list. "
            f"Provide only the longest words, separated by commas with no further explanation."
            f"If no word can be found, an empty string is returned."
        )
        return prompt

    def generate_words(self, letters: List[str], language: str) -> str:
        """
        Generates words using the OpenAI API based on provided letters and language.

        Args:
            letters (List[str]): List of letters.
            language (str): Language for word generation.

        Returns:
            str: The response text from the OpenAI API containing generated words.

        Raises:
            Exception: If there is an error communicating with the OpenAI API.
        """
        prompt = self.construct_prompt(letters, language)

        messages = [{"role": "user", "content": prompt}]

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0,
                max_tokens=100,
            )

            if response and response.choices:
                return response.choices[0].message.content
            else:
                logger.error("Invalid response from OpenAI API")
                raise Exception("Invalid response from OpenAI API")
        except Exception as e:
            logger.exception("Error communicating with OpenAI API")
            raise
