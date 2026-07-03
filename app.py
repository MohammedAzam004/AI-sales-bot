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
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #0b0e14;
}

.stApp {
    background-color: #0b0e14;
}

/* Glassmorphic cards with glowing border */
.capability-card {
    background: linear-gradient(145deg, rgba(21, 25, 33, 0.7), rgba(15, 18, 24, 0.7));
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 24px;
    border-radius: 16px;
    border: 1px solid rgba(35, 42, 53, 0.8);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    margin-bottom: 15px;
    min-height: 120px;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.capability-card:hover {
    border-color: rgba(0, 212, 255, 0.6);
    box-shadow: 0 0 25px rgba(0, 212, 255, 0.2);
    transform: translateY(-5px);
}

.card-title {
    color: #00d4ff;
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 8px;
    letter-spacing: -0.02em;
}

.card-text {
    color: #94a3b8;
    font-size: 0.95rem;
    line-height: 1.6;
}

.hero-title {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 10px;
    font-weight: 800;
    font-size: 2.8rem;
    letter-spacing: -0.03em;
}

.gradient-text {
    background: linear-gradient(135deg, #ffffff 40%, #00d4ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 1.25rem;
    font-weight: 400;
    margin-bottom: 15px;
}

.footer-text {
    color: #4b5563;
    text-align: center;
    margin-top: 25px;
    font-size: 0.85rem;
}

/* Custom premium divider styling */
hr {
    border: 0;
    height: 1px;
    background: linear-gradient(to right, rgba(0, 212, 255, 0), rgba(0, 212, 255, 0.25), rgba(0, 212, 255, 0));
    margin: 20px 0;
}

/* Responsive typography and paddings */
@media (max-width: 768px) {
    .hero-title {
        font-size: 2.0rem !important;
    }
    .hero-subtitle {
        font-size: 1.05rem !important;
    }
    .card-title {
        font-size: 1.15rem !important;
    }
    .card-text {
        font-size: 0.88rem !important;
    }
    .capability-card {
        padding: 16px;
        min-height: auto;
        margin-bottom: 10px;
    }
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 4️⃣ HERO SECTION
# --------------------------------------------------
st.markdown('<h1 class="hero-title">📞 <span class="gradient-text">AI Sales Representative</span></h1>', unsafe_allow_html=True)
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
                html, body {{
                    margin: 0;
                    padding: 0;
                    background: transparent;
                    overflow-x: hidden;
                    overflow-y: auto;
                    display: flex;
                    justify-content: center;
                    align-items: flex-start;
                    height: 100%;
                    width: 100%;
                }}
                elevenlabs-convai {{
                    margin-top: 10px;
                }}
            </style>
        </head>
        <body>
            <elevenlabs-convai agent-id="{AGENT_ID}"></elevenlabs-convai>
        </body>
        </html>
        """,
        height=380
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown('<p class="footer-text">© 2026 Sales Intelligence Systems | Premium AI Solutions</p>', unsafe_allow_html=True)