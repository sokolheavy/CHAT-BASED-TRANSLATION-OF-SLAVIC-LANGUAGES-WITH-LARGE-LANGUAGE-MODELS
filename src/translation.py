from deep_translator import GoogleTranslator
from config import OPENROUTER_API_KEY
import requests

def google_translator(text, source_language, target_language):
    translator = GoogleTranslator(source=source_language, target=target_language)
    return translator.translate(text)

def translate_text_google(text, target_lang):
    base_url = 'https://translate.google.com/m'
    params = {'sl': 'auto', 'tl': target_lang, 'q': text}
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            translated_text = soup.find('div', {'class': 'result-container'})

            if translated_text:
                return translated_text.text.strip()
            else:
                return "Translation not found."
        except requests.exceptions.RequestException as e:
            if attempt < 2:
                time.sleep(2 ** attempt)
                continue
            return f"Error: {str(e)}"
