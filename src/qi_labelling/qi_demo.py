import re
import numpy as np

QI_PATTERNS = {
    "age": r'\d{1,3}\s*tahun',
    "gender": r'\b(pria|wanita|laki)\b',
    "time": r'\b(jam|pukul)\b',
}

def score(text):
    t = text.lower()
    return sum(1 for p in QI_PATTERNS.values() if re.search(p,t))

def add_qi_scores(df):
    df["qi_score"] = df["clean_text"].apply(score)
    th = int(np.median(df["qi_score"]))
    df["label"] = np.where(df["qi_score"]>=th,"HIGH_RISK","LOW_RISK")
    return df
