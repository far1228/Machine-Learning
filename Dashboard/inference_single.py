# ============================================
# inference.py
# FINAL - Privacy Risk Inference (QI-based)
# ============================================

import joblib
import numpy as np
import torch
import pandas as pd

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from peft import PeftModel

from utils.preprocess import clean_text

# ============================================
# GLOBAL
# ============================================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
LABEL_MAP = {0: "LOW_RISK", 1: "HIGH_RISK"}
MAX_LEN = 150   # sesuai training LSTM

# ============================================
# LOAD LR (BEST MODEL)
# ============================================
tfidf = joblib.load("models/tfidf_vectorizer.pkl")
lr_model = joblib.load("models/lr_model.pkl")

# fitur saat TRAINING LR (1000 fitur)
LR_FEATURES = lr_model.feature_names_in_

# ============================================
# LOAD LSTM (COMPARISON)
# ============================================
lstm_model = load_model("models/ft_lstm.h5")
tokenizer_lstm = joblib.load("models/tokenizer_lstm.pkl")

# ============================================
# LOAD LoRA-BERT (COMPARISON)
# ============================================
BASE_BERT = "cahya/bert-base-indonesian-1.5G"

bert_tokenizer = AutoTokenizer.from_pretrained(BASE_BERT)

_base_bert = AutoModelForSequenceClassification.from_pretrained(
    BASE_BERT,
    num_labels=2
).to(DEVICE)

bert_model = PeftModel.from_pretrained(
    _base_bert,
    "models/lora_bert"
).to(DEVICE)
bert_model.eval()

# ============================================
# SINGLE PREDICTION
# ============================================
def predict_single(text: str, model_name: str = "BEST") -> str:
    text_clean = clean_text(text)

    # ================= BEST MODEL (LR) =================
    if model_name == "BEST" or model_name == "TF-IDF + Logistic Regression":
        vec = tfidf.transform([text_clean])

        # 🔑 FIX UTAMA: samakan fitur ke training
        vec_df = pd.DataFrame(
            vec.toarray(),
            columns=tfidf.get_feature_names_out()
        )

        vec_df = vec_df.reindex(
            columns=LR_FEATURES,
            fill_value=0
        )

        pred = lr_model.predict(vec_df)[0]
        return pred if isinstance(pred, str) else LABEL_MAP[int(pred)]

    # ================= FT-LSTM =================
    elif model_name == "FT-LSTM":
        seq = tokenizer_lstm.texts_to_sequences([text_clean])
        pad = pad_sequences(seq, maxlen=MAX_LEN, padding="post")
        prob = lstm_model.predict(pad, verbose=0)[0][0]
        return LABEL_MAP[int(prob >= 0.5)]

    # ================= LoRA-BERT =================
    elif model_name == "LoRA-BERT":
        inputs = bert_tokenizer(
            text_clean,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )
        inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

        with torch.no_grad():
            logits = bert_model(**inputs).logits
            idx = torch.argmax(logits, dim=1).item()

        return LABEL_MAP[idx]

    else:
        raise ValueError("Model tidak dikenali")
