import json
import unittest
from unittest.mock import patch

from app import app


class TestApp(unittest.TestCase):
    """
    Unit tests for the Flask application.
    """

    def setUp(self):
        """
        Set up the test client before each test.
        """
        self.app = app.test_client()

    @patch('openai.Completion.create')
    def test_generate_word_success(self, mock_openai):
        """
        Test the /generate-word endpoint with valid input, expecting longest words only.
        """
        # Mock OpenAI response
        mock_openai.return_value = {
            'choices': [{
                'text': 'rot, tor'
            }]
        }
        payload = {
            "letters": ["r", "t", "o"],
            "language": "English"
        }
        response = self.app.post('/generate-word', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('words', data)
        # Expect only the longest words
        self.assertEqual(data['words'], ['rot', 'tor'])

    # Other tests remain the same...


if __name__ == '__main__':
    unittest.main()
