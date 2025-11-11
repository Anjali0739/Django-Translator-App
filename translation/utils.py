import requests

def translate_text(text, source, target):
    url = "https://655.mtis.workers.dev/translate"
    params = {
        "text": text,
        "source_lang": source,
        "target_lang": target
    }
    resp = requests.get(url, params=params)
    translated = resp.json().get("response").get("translated_text")
    return translated