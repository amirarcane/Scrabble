import requests
import streamlit as st

from utils.models import GenerateWordRequest

API_URL = 'http://localhost:8888/generate-word'


def main():
    """
    Main function to run the Streamlit app.
    """
    st.title('Scrabble Word Finder')

    st.markdown('Enter the letters and select the language to find the longest possible words.')

    letters_input = st.text_input('Letters (comma-separated)', 'r, t, o')
    language_input = st.text_input('Language', 'English')

    if st.button('Generate Words'):
        letters = [letter.strip() for letter in letters_input.split(',')]
        language = language_input.strip()

        generate_request = GenerateWordRequest(letters=letters, language=language)
        response = requests.post(API_URL, json=generate_request.__dict__)

        if response.status_code == 200:
            data = response.json()
            words = data.get('words', [])
            if words:
                st.success('Words Generated Successfully!')
                st.write(f"Total words found: {len(words)}")
                for word in words:
                    st.write(word)
            else:
                st.warning('No valid words found.')
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")


if __name__ == '__main__':
    main()
