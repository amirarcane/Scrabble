import unittest
from unittest.mock import patch

from utils.openai_helper import OpenAIHelper


class TestOpenAIHelper(unittest.TestCase):
    """
    Unit tests for the OpenAIHelper class.
    """

    @patch('openai.Completion.create')
    def test_generate_words_success(self, mock_openai):
        """
        Test generate_words method with a successful OpenAI API response.
        """
        mock_openai.return_value = {
            'choices': [{
                'text': 'rot, tor, or, to'
            }]
        }
        openai_helper = OpenAIHelper()
        result = openai_helper.generate_words(['r', 't', 'o'], 'English')
        self.assertEqual(result, 'rot, tor, or, to')

    @patch('openai.Completion.create')
    def test_generate_words_failure(self, mock_openai):
        """
        Test generate_words method with an OpenAI API error.
        """
        mock_openai.side_effect = Exception('OpenAI API Error')
        openai_helper = OpenAIHelper()
        with self.assertRaises(Exception):
            openai_helper.generate_words(['r', 't', 'o'], 'English')


if __name__ == '__main__':
    unittest.main()
