import logging

from flask import Flask, request, jsonify

from config import Config
from utils.models import GenerateWordRequest, GenerateWordResponse
from utils.openai_helper import OpenAIHelper
from utils.word_validator import WordValidator

# Configure logging
logging.basicConfig(level=Config.LOG_LEVEL, format=Config.LOG_FORMAT)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initialize helpers
openai_helper = OpenAIHelper()
word_validator = WordValidator()


@app.route('/generate-word', methods=['POST'])
def generate_word():
    """
    REST API endpoint to generate the longest possible words from provided letters and language.

    Expects a JSON payload with 'letters' and 'language'.
    Returns a JSON response with a list of the longest valid words.

    Returns:
        Response object: JSON response containing the list of words or an error message.
    """
    try:
        data = request.get_json()
        generate_request = GenerateWordRequest.from_dict(data)

        # Validate input letters
        if not generate_request.letters:
            logger.warning("Empty letters list received.")
            return jsonify({'error': 'Letters list cannot be empty'}), 400
        if not all(isinstance(letter, str) and letter.isalpha() and len(letter) == 1 for letter in
                   generate_request.letters):
            logger.warning("Invalid letters received.")
            return jsonify({'error': 'All letters must be single alphabetic characters'}), 400

        # Validate language
        if not generate_request.language:
            logger.warning("No language specified.")
            return jsonify({'error': 'Language must be specified'}), 400

        letters = [letter.lower() for letter in generate_request.letters]
        language = generate_request.language

        # Generate words using OpenAI API
        chatgpt_reply = openai_helper.generate_words(letters, language)

        # Process and validate words
        raw_words = [word.strip() for word in chatgpt_reply.split(',') if word.strip()]
        valid_words = word_validator.validate_words(raw_words, letters)

        # Find the maximum length of the valid words
        if valid_words:
            max_length = max(len(word) for word in valid_words)
            # Keep only the words that have the maximum length
            longest_words = [word for word in valid_words if len(word) == max_length]
        else:
            longest_words = []

        generate_response = GenerateWordResponse(words=longest_words)
        return jsonify(generate_response.to_dict()), 200

    except Exception as e:
        logger.exception("An error occurred while processing the request.")
        return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run(host=Config.FLASK_HOST, port=Config.FLASK_PORT)
