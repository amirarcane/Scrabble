import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Configuration class for managing environment variables and application settings.
    """
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
    FLASK_PORT = int(os.getenv('FLASK_PORT', 8888))
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
