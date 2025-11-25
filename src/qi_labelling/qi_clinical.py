import re
import numpy as np

PATS = {
    "age": r'(0–19|20–39|40–59|60+)',
    "event": r'\b(meninggal|selamat)\b',
}

def count(text):
    t=text.lower()
    return sum(1 for p in PATS.values() if re.search(p,t))

def add_qi_scores(df):
    df["qi_score"]=df["clean_text"].apply(count)
    th=int(np.median(df["qi_score"]))
    df["label"]=np.where(df["qi_score"]>=th,"HIGH_RISK","LOW_RISK")
    return df
