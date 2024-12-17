import json
import urllib.parse
from bs4 import BeautifulSoup

def create_query(original_translation, GPT4_response, Claude_response, llama_response, T5_response, google_trans_response):
    return f"""Which translation is better (use English for answer) - 1.ChatGPT, 2.Claude, 3. Llama, 4.T5_model, 5. google_trans? Choose one option. The answer should be one word. Considering the best translation should be similar to "{original_translation}".

    1. ChatGPT - "{GPT4_response}"
    2. Claude - "{Claude_response}"
    3. Llama - "{llama_response}"
    4. T5_model - "{T5_response}"
    5. google_trans - "{google_trans_response}" """

def main(language_to_translate: str, original_text: str, original_translation: str, lang_2) -> None:
    message = f"""Translate the following chat-based text from English to {language_to_translate} while maintaining the informal tone, slang, and cultural nuances:

    [ {original_text} ]"""
    # Add logic for handling translation
