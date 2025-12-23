import os
import streamlit as st
import pandas as pd
import plotly.express as px
from inference_single import predict_single
from styles.ui_style import inject_css, risk_card

# ======================================================
# PATH CONFIG (WAJIB – FIX UTAMA)
# ======================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

DATASETS = {
    "Clinical Data (Anonymized)": "ClinicalData_anonymized.csv",
    "Demographics (Anonymized)": "demographics_anoon.csv"
}

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="Privacy Risk Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_css()

# ======================================================
# HEADER
# ======================================================
st.markdown("""
<div style="padding:16px 8px;">
    <h1 style="text-align:center; margin-bottom:6px;">
        🔐 Privacy Risk Analysis Dashboard
    </h1>
    <p style="text-align:center; font-size:16px; opacity:0.85;">
        Analisis Risiko Privasi Data Pasien berbasis
        <b>Quasi-Identifier (QI)</b> dengan pendekatan
        <b>Hybrid Rule-based & Machine Learning</b>
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================================================
# SYSTEM OVERVIEW
# ======================================================
st.markdown("## 📌 System Overview")

ov1, ov2, ov3, ov4 = st.columns(4)
ov1.metric("Pendekatan", "Hybrid")
ov2.metric("Jumlah QI", "6 Atribut")
ov3.metric("Threshold", "Default = 4")
ov4.metric("Mode", "Analytical")

st.divider()

# ======================================================
# SIDEBAR
# ======================================================
st.sidebar.header("⚙️ System Configuration")

MODEL_OPTIONS = [
    "BEST (TF-IDF + Logistic Regression)",
    "TF-IDF + Logistic Regression",
    "FT-LSTM",
    "LoRA-BERT"
]

model_ui = st.sidebar.selectbox("Model Evaluasi", MODEL_OPTIONS)
model_choice = "BEST" if model_ui.startswith("BEST") else model_ui

QI_THRESHOLD = st.sidebar.slider(
    "QI Threshold",
    2, 6, 4,
    help="Semakin tinggi threshold, semakin ketat risiko HIGH"
)

st.sidebar.markdown("""
**Decision Rule:**
- QI ≥ threshold → **HIGH_RISK**
- QI < threshold → hasil **Model ML**
""")

# ======================================================
# QI RULES
# ======================================================
QI_RULES = {
    "Age": ["0-17","18-39","40-59","60-79","80-99"],
    "Gender": ["laki-laki","perempuan","male","female"],
    "Ethnicity": ["kulit hitam","afrika-amerika","kulit putih","asia","hispanik"],
    "Location": ["rumah sakit","hospital","rs","suny"],
    "Temporal": [
        "senin","selasa","rabu","kamis","jumat",
        "sabtu","minggu",
        "januari","februari","maret","april",
        "mei","juni","juli","agustus",
        "september","oktober","november","desember"
    ],
    "Outcome": ["deceased","passed away","meninggal","expired","wafat","dunia"]
}

def qi_breakdown(text: str):
    t = text.lower()
    detected = {}
    score = 0
    for k, v in QI_RULES.items():
        found = any(x in t for x in v)
        detected[k] = found
        score += int(found)
    return score, detected

# ======================================================
# MAIN ANALYSIS (SINGLE INPUT – DIBIARKAN)
# ======================================================
st.markdown("## 🧪 Privacy Risk Evaluation")

left, right = st.columns([1.15, 1])

with left:
    st.markdown("### 🔎 Input & Decision")

    text = st.text_area(
        "Input Teks (hasil anonimisasi)",
        height=220,
        placeholder="Masukkan teks hasil anonimisasi..."
    )

    run = st.button("🚀 Run Risk Analysis")

    if run:
        if not text.strip():
            st.warning("Teks tidak boleh kosong.")
        else:
            qi_score, qi_map = qi_breakdown(text)
            model_pred = predict_single(text, model_choice)

            if qi_score >= QI_THRESHOLD:
                final_pred = "HIGH_RISK"
                source = "Rule-based QI"
            else:
                final_pred = model_pred
                source = "Machine Learning"

            st.markdown("#### 📊 Decision Summary")
            c1, c2 = st.columns(2)
            c1.metric("QI Score", qi_score)
            c2.metric("Decision Source", source)

            risk_card(final_pred)

with right:
    st.markdown("### 📌 Quasi-Identifier Analysis")

    if 'qi_map' in locals():
        qi_df = pd.DataFrame({
            "QI Attribute": qi_map.keys(),
            "Detected": ["Yes" if v else "No" for v in qi_map.values()],
            "Value": [1 if v else 0 for v in qi_map.values()]
        })

        fig = px.bar(
            qi_df,
            x="QI Attribute",
            y="Value",
            color="Value",
            range_y=[0, 1],
            title="QI Detection per Attribute"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.dataframe(qi_df[["QI Attribute", "Detected"]])

st.divider()

# ======================================================
# DATASET ANALYSIS (BATCH – 2 DATASET)
# ======================================================
st.markdown("## 📂 Dataset-Level Risk Analysis")

dataset_label = st.selectbox(
    "Pilih Dataset",
    list(DATASETS.keys())
)

dataset_path = os.path.join(DATA_DIR, DATASETS[dataset_label])
df = pd.read_csv(dataset_path)

st.success(f"Dataset dimuat: {DATASETS[dataset_label]}")
st.dataframe(df.head(), use_container_width=True)

col = st.selectbox("Kolom Teks", df.columns)

if st.button("📊 Analyze Dataset"):
    scores, preds = [], []

    for txt in df[col].astype(str):
        s, _ = qi_breakdown(txt)
        p = predict_single(txt, model_choice)
        preds.append("HIGH_RISK" if s >= QI_THRESHOLD else p)
        scores.append(s)

    df["qi_score"] = scores
    df["risk"] = preds

    st.success("Analisis dataset selesai")

    g1, g2 = st.columns([1, 1.2])

    with g1:
        st.dataframe(df, use_container_width=True)

    with g2:
        fig = px.histogram(
            df,
            x="qi_score",
            color="risk",
            nbins=6,
            title="Distribusi QI Score vs Risk"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.download_button(
        "⬇️ Download Results",
        df.to_csv(index=False).encode(),
        "privacy_risk_results.csv"
    )
