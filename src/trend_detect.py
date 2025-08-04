from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")
nltk.download("stopwords")

def extract_keywords(tweets, top_n=10):
    all_words = []
    stop_words = set(stopwords.words("english"))

    for tweet in tweets:
        words = word_tokenize(tweet.lower())
        all_words.extend([w for w in words if w.isalpha() and w not in stop_words])

    most_common = Counter(all_words).most_common(top_n)
    return most_common
