import streamlit as st

def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #fef6f6 0%, #fff0f0 100%);
        font-family: 'Inter', sans-serif;
    }

    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, #ffc1c1 0%, #ffb3ba 100%);
        padding: 48px 32px;
        border-radius: 20px;
        margin-bottom: 32px;
        box-shadow: 0 10px 40px rgba(255, 179, 186, 0.3);
        border: 1px solid rgba(255,255,255,0.5);
    }

    .main-header h1 {
        color: #7c2d3a;
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 12px;
        letter-spacing: -1px;
        text-align: center;
    }

    .main-header p {
        color: #9d4855;
        font-size: 17px;
        text-align: center;
        line-height: 1.6;
        max-width: 900px;
        margin: 0 auto;
    }

    /* Section Headers */
    .section-header {
        background: linear-gradient(135deg, #ffffff 0%, #fff5f5 100%);
        padding: 24px 28px;
        border-radius: 16px;
        margin: 32px 0 20px 0;
        border-left: 6px solid #ffb3ba;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    }

    .section-header h2 {
        color: #7c2d3a;
        font-size: 1.6rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }

    /* Card Containers */
    .elevated-card {
        background: #ffffff;
        padding: 32px;
        border-radius: 16px;
        border: 1px solid #ffe4e6;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }

    .elevated-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(255, 179, 186, 0.15);
    }

    /* Input Section */
    .input-section {
        background: linear-gradient(135deg, #fff5f5 0%, #ffeded 100%);
        padding: 28px;
        border-radius: 16px;
        border: 2px solid #ffd4d4;
        margin-bottom: 24px;
    }

    .input-section h3 {
        color: #7c2d3a;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 16px;
    }

    /* Metrics Grid */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin: 24px 0;
    }

    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #fff5f5 100%);
        padding: 24px 20px;
        border-radius: 14px;
        border: 1px solid #ffe4e6;
        box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        text-align: center;
        transition: all 0.3s ease;
    }

    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(255, 179, 186, 0.15);
        border-color: #ffc1c1;
    }

    .metric-label {
        color: #9d4855;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 10px;
    }

    .metric-value {
        color: #7c2d3a;
        font-size: 32px;
        font-weight: 900;
        letter-spacing: -1px;
    }
    
    /* Streamlit Metric Overrides */
    [data-testid="stMetricValue"] {
        font-size: 32px !important;
        font-weight: 900 !important;
        color: #7c2d3a !important;
        letter-spacing: -1px !important;
    }

    [data-testid="stMetricLabel"] {
        color: #9d4855 !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        letter-spacing: 1.2px !important;
    }

    [data-testid="stMetricDelta"] {
        color: #e85d75 !important;
        font-weight: 700 !important;
        font-size: 14px !important;
    }

    /* Risk Card - Full Height */
    .risk-card {
        padding: 48px 32px;
        border-radius: 16px;
        text-align: center;
        margin-top: 24px;
        background: #ffffff;
        box-shadow: 0 8px 32px rgba(0,0,0,0.08);
        transition: all 0.4s ease;
        animation: fadeIn 0.5s ease-out;
        position: relative;
        overflow: hidden;
        min-height: 500px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        border: 1px solid #ffe4e6;
    }

    .risk-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 5px;
    }

    .high-risk::before {
        background: linear-gradient(90deg, #ffb3ba 0%, #ffc1c1 100%);
    }

    .low-risk::before {
        background: linear-gradient(90deg, #bae1ff 0%, #a8d8ff 100%);
    }

    .risk-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 16px 48px rgba(0,0,0,0.12);
    }

    .risk-icon-container {
        width: 120px;
        height: 120px;
        border-radius: 20px;
        margin: 0 auto 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease;
    }

    .high-risk .risk-icon-container {
        background: linear-gradient(135deg, #ffe4e6 0%, #ffd4d4 100%);
        border: 3px solid #ffb3ba;
    }

    .low-risk .risk-icon-container {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border: 3px solid #93c5fd;
    }

    .risk-label {
        display: inline-block;
        background: rgba(255, 255, 255, 0.6);
        padding: 8px 20px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2.5px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }

    .high-risk .risk-label {
        color: #9d4855;
        border: 1.5px solid #ffb3ba;
    }

    .low-risk .risk-label {
        color: #1e3a8a;
        border: 1.5px solid #93c5fd;
    }

    .risk-result {
        font-size: 48px;
        font-weight: 900;
        margin-top: 16px;
        letter-spacing: -2px;
        line-height: 1;
        text-transform: uppercase;
    }

    .high-risk .risk-result {
        background: linear-gradient(135deg, #e85d75 0%, #ff6b9d 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .low-risk .risk-result {
        background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .risk-subtitle {
        margin-top: 28px;
        padding: 16px 24px;
        background: linear-gradient(135deg, rgba(248, 250, 252, 0.8) 0%, rgba(241, 245, 249, 0.8) 100%);
        border-radius: 12px;
        font-size: 15px;
        color: #475569;
        font-weight: 500;
        line-height: 1.7;
        border: 1px solid rgba(226, 232, 240, 0.6);
    }

    .risk-icon {
        font-size: 64px;
    }

    /* Decision Summary Box */
    .decision-summary {
        background: linear-gradient(135deg, #fff5f5 0%, #ffeded 100%);
        padding: 24px;
        border-radius: 14px;
        border: 2px solid #ffe4e6;
        margin: 20px 0;
    }

    .decision-summary h4 {
        color: #7c2d3a;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 16px;
    }

    /* QI Analysis Panel */
    .qi-panel {
        background: #ffffff;
        padding: 28px;
        border-radius: 16px;
        border: 1px solid #ffe4e6;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    }

    .qi-panel h3 {
        color: #7c2d3a;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 20px;
        padding-bottom: 12px;
        border-bottom: 2px solid #ffe4e6;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #ffb3ba 0%, #ffc1c1 100%);
        color: #7c2d3a;
        border: none;
        padding: 14px 32px;
        border-radius: 10px;
        font-weight: 700;
        font-size: 15px;
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 16px rgba(255, 179, 186, 0.35);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #ffc1c1 0%, #ffd4d4 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(255, 179, 186, 0.45);
    }

    /* Form Elements */
    .stTextArea textarea {
        border: 2px solid #ffe4e6 !important;
        border-radius: 12px !important;
        font-size: 15px !important;
        padding: 16px !important;
        transition: all 0.2s ease !important;
    }

    .stTextArea textarea:focus {
        border-color: #ffb3ba !important;
        box-shadow: 0 0 0 3px rgba(255, 179, 186, 0.15) !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffb3ba 0%, #ffc1c1 100%);
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] p {
        color: #7c2d3a !important;
    }

    /* File Uploader */
    .stFileUploader {
        background: #ffffff;
        padding: 24px;
        border-radius: 12px;
        border: 2px dashed #ffc1c1;
    }

    /* Animation */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #ffe4e6, transparent);
        margin: 40px 0;
    }
    </style>
    """, unsafe_allow_html=True)


def risk_card(label: str):
    css = "high-risk" if label == "HIGH_RISK" else "low-risk"
    icon = "⚠" if label == "HIGH_RISK" else "✓"
    display_text = "HIGH RISK" if label == "HIGH_RISK" else "LOW RISK"
    subtitle = "Patient data is potentially identifiable. Enhanced anonymization required to protect privacy." if label == "HIGH_RISK" else "Patient data is well anonymized. Risk of re-identification is low."

    st.markdown(f"""
    <div class="risk-card {css}">
        <div class="risk-icon-container">
            <div class="risk-icon">{icon}</div>
        </div>
        <div class="risk-label">Prediction Result</div>
        <div class="risk-result">{display_text}</div>
        <div class="risk-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)