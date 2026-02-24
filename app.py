from pathlib import Path
import os
import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv

# Load .env file
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

# --------------------------------------------------
# 1️⃣ PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Sales Agent",
    page_icon="📞",
    layout="wide"
)

# --------------------------------------------------
# 2️⃣ LOAD ENV FILE
# --------------------------------------------------
AGENT_ID = None

# Try Streamlit Cloud secrets first
try:
    AGENT_ID = st.secrets["AGENT_ID"]
except Exception:
    pass

# If not found in secrets, try environment variable
if not AGENT_ID:
    AGENT_ID = os.getenv("AGENT_ID")

# --------------------------------------------------
# 3️⃣ PREMIUM DARK THEME CSS
# --------------------------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0b0e14;
}

.capability-card {
    background: linear-gradient(145deg, #151921, #0f1218);
    padding: 10px;
    border-radius: 14px;
    border: 1px solid #232a35;
    box-shadow: 0 6px 25px rgba(0,0,0,0.4);
    margin-bottom: 5px;
    min-height: 100px;
    transition: all 0.3s ease;
}

.capability-card:hover {
    border-color: #00d4ff;
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.25);
    transform: translateY(-4px);
}

.card-title {
    color: #00d4ff;
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 5px;
}

.card-text {
    color: #94a3b8;
    font-size: 0.95rem;
    line-height: 1.6;
}

.hero-title {
    text-align: center;
    margin-bottom: 5px;
}

.hero-subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 5px;
}

.footer-text {
    color: #6b7280;
    text-align: center;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 4️⃣ HERO SECTION
# --------------------------------------------------
st.markdown('<h1 class="hero-title">📞 AI Sales Representative</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="hero-subtitle">Accelerate your sales cycle with Voice AI.</h3>', unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# 5️⃣ FEATURES SECTION
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="capability-card">
        <div class="card-title">🔍 Knowledge Engine</div>
        <div class="card-text">
            Access technical specs and pricing instantly to provide customers with precise data.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="capability-card">
        <div class="card-title">🎯 Smart Discovery</div>
        <div class="card-text">
            Qualify leads in real-time by identifying pain points through natural conversation.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# 6️⃣ ELEVENLABS AGENT
# --------------------------------------------------
if not AGENT_ID:
    st.error("⚠️ AGENT_ID not found in .env file or Streamlit Cloud secrets.")
    st.info("Add AGENT_ID either in .env file (local) or in Streamlit Cloud Secrets.")
else:
    components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://elevenlabs.io/convai-widget/index.js"></script>
            <style>
                body {{
                    margin: 0;
                    background: transparent;
                }}
            </style>
        </head>
        <body>
            <elevenlabs-convai agent-id="{AGENT_ID}"></elevenlabs-convai>
        </body>
        </html>
        """,
        height=150
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown('<p class="footer-text">© 2026 Sales Intelligence Systems | Premium AI Solutions</p>', unsafe_allow_html=True)