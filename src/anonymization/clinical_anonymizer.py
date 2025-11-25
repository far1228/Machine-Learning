import re
import random
from hashlib import blake2b

def pseudo(v,p): return f"{p}_{blake2b(v.encode(),digest_size=2).hexdigest().upper()}"

def generalize_age(text):
    m = re.search(r'(berusia|umur)\s*(\d+)', text)
    if not m: return text
    age = int(m.group(2))
    if age <20: r="0–19 tahun"
    elif age<40: r="20–39 tahun"
    elif age<60: r="40–59 tahun"
    else: r="60+ tahun"
    return re.sub(r'(berusia|umur)\s*\d+', f"berusia {r}", text)

def perturb(text):
    pairs = {
        "hipertensi": random.choice(["hipertensi ringan","tekanan darah tinggi"]),
        "kanker": "penyakit serius"
    }
    for k,v in pairs.items():
        text = re.sub(k, v, text, flags=re.IGNORECASE)
    return text

def anonymize_text(text):
    if not isinstance(text,str): return text
    text = generalize_age(text)
    text = perturb(text)
    text = re.sub(r'nomor identifikasi\s*(\d+)', lambda m: pseudo(m.group(1),"Patient"), text, flags=re.IGNORECASE)
    return text
