# Scrabble Word Finder

Scrabble Word Finder is a Python application that helps users find the **longest possible valid words** from a given set of letters in a specified language, similar to a Scrabble word lookup. It includes a Flask RESTful API and a Streamlit user interface.

**Features:**

- Generates the longest possible words using the OpenAI GPT API.
- Validates words to ensure they use each provided letter at most as many times as it appears in the input list.
- Provides a REST API endpoint for word generation.
- Includes a user-friendly interface built with Streamlit.
- Contains unit tests for code reliability.

---

## How to Run the Project

### Prerequisites

- **Python 3.7** or higher.
- **OpenAI API Key**: Required to access the OpenAI GPT API.

### Installation Steps

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

2. **Set Up Environment Variables:**

- **Using a .env File:** Replace your-openai-api-key with your actual OpenAI API key.

  ```bash
  OPENAI_API_KEY=your-openai-api-key
  FLASK_HOST=0.0.0.0
  FLASK_PORT=8888
  LOG_LEVEL=INFO
  
3. **Run the Flask API:**

- The API will start and listen on http://0.0.0.0:8888

   ```bash
   python app.py

4. **Run the Streamlit Interface:**

- Open a new terminal window (activate the virtual environment if used), and run:

   ```bash
   streamlit run streamlit_app.py

5. **Running Tests:**

   ```bash
   python -m unittest discover tests