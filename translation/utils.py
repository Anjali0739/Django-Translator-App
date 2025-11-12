import requests
from django.conf import settings

def translate_text(text, source, target):
    url = settings.TRANSLATOR_URL
    params = {
        "text": text,
        "source_lang": source,
        "target_lang": target
    }
    resp = requests.get(url, params=params)
    translated = resp.json().get("response").get("translated_text")
    return translated