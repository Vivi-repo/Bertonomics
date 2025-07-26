from newsapi import NewsApiClient  # type: ignore
from transformers import BertTokenizer, BertForSequenceClassification  # type: ignore
import torch  # type: ignore
from googletrans import Translator  # type: ignore

newsapi = NewsApiClient(api_key='NEWSAPI_KEY')
tokenizer = BertTokenizer.from_pretrained("yiyanghkust/finbert-tone")
model = BertForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone")
translator = Translator()

def fetch_headlines():
    articles = newsapi.get_everything(
        q='bitcoin OR stock OR finance',
        language='en',
        sort_by='publishedAt',
        page_size=5
    )
    print("API RESPONSE:", articles)  # Debug
    titles = [article['title'] for article in articles.get('articles', [])]
    if not titles:
        titles = ["No headlines found."]
    return titles

def translate_to_english(text):
    try:
        detected_lang = translator.detect(text).lang
        if detected_lang != 'en':
            translated = translator.translate(text, src=detected_lang, dest='en')
            return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
    return text

def finbert_score(text):
    try:
        english_text = translate_to_english(text)
        inputs = tokenizer(english_text, return_tensors="pt", truncation=True)
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        sentiment = ["Negative", "Neutral", "Positive"]
        scores = dict(zip(sentiment, probs[0].detach().numpy()))
        return scores["Positive"] - scores["Negative"]
    except Exception as e:
        print(f"FinBERT error: {e}")
        return 0.0

def interpret_sentiment(score):
    if score > 0.2:
        return "Positive"
    elif score < -0.2:
        return "Negative"
    else:
        return "Neutral"

def average_sentiment():
    headlines = fetch_headlines()
    if not headlines or headlines == ["No headlines found."]:
        return 0.0, "Neutral"
    total_score = sum(finbert_score(headline) for headline in headlines)
    avg_score = total_score / len(headlines)
    return avg_score, interpret_sentiment(avg_score)

