import re
import random
from hashlib import blake2b

def pseudo_token(value, prefix):
    h = blake2b(value.encode(), digest_size=2).hexdigest().upper()
    return f"{prefix}_{h}"

def generalize_age(text):
    match = re.search(r'(\d{1,3})\s*tahun', text)
    if not match:
        return text
    age = int(match.group(1))
    if age < 20: r = "0–19 tahun"
    elif age < 40: r = "20–39 tahun"
    elif age < 60: r = "40–59 tahun"
    elif age < 80: r = "60–79 tahun"
    else: r = "80–99 tahun"
    return re.sub(r'\d{1,3}\s*tahun', r, text)

def perturb_sensitive(text):
    variants = {
        "hipertensi": random.choice(["tekanan darah tinggi","hipertensi ringan"]),
        "diabetes": random.choice(["kadar gula tinggi","diabetes mellitus"])
    }
    for k,v in variants.items():
        text = re.sub(k, v, text, flags=re.IGNORECASE)
    return text

def anonymize_text(text):
    if not isinstance(text,str): return text
    text = generalize_age(text)
    text = perturb_sensitive(text)
    text = re.sub(r'(ID\s*\d+)', lambda m: pseudo_token(m.group(0),"Patient"), text)
    return text
