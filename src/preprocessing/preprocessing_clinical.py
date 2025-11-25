import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

stop_words = set(stopwords.words("indonesian")) | set(stopwords.words("english"))

def preprocess_clinical_text(text):
    if not isinstance(text,str): return ""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]',' ', text)
    tokens = [w for w in text.split() if w not in stop_words]
    return " ".join(tokens)
