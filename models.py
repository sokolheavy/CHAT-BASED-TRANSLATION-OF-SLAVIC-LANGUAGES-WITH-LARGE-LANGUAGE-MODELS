import requests
import json
import torch
from transformers import MarianMTModel, MarianTokenizer, AutoModelForSeq2SeqLM, AutoTokenizer
from sentence_transformers import SentenceTransformer
from config import OPENROUTER_API_KEY
from comet import download_model, load_from_checkpoint

# Initialize models
MODEL = SentenceTransformer('paraphrase-MiniLM-L6-v2')
comet_model_path = download_model("Unbabel/wmt22-comet-da")
comet_model = load_from_checkpoint(comet_model_path)


def translate_transformer(text, lang_2):
    model_name = f"Helsinki-NLP/opus-mt-en-{lang_2}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    translated = model.generate(**inputs)
    return tokenizer.batch_decode(translated, skip_special_tokens=True)[0]


def t5(text, max_length=512):
    model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
    tokenizer = AutoTokenizer.from_pretrained("t5-base")
    chunks = [text[i:i + max_length] for i in range(0, len(text), max_length)]

    translated_chunks = []
    for chunk in chunks:
        inputs = tokenizer(chunk, return_tensors="pt", padding=True, truncation=True, max_length=max_length)
        with torch.no_grad():
            translated = model.generate(**inputs, max_length=max_length, num_beams=4, length_penalty=0.6,
                                        early_stopping=True)
        translated_chunks.append(tokenizer.batch_decode(translated, skip_special_tokens=True)[0])

    return ' '.join(translated_chunks)


def gp4_model_new(prompt):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
        data=json.dumps({"model": "openai/o1-preview-2024-09-12", "messages": [{"role": "user", "content": prompt}]})
    )
    res = response.json().get('choices', [{}])[0].get('message', {}).get('content', str(response.json()))
    return res
