# app.py
import streamlit as st
import base64
import importlib

st.set_page_config(page_title="Lord's Arcade Realm", page_icon="🌸", layout="centered")

# --- helpers ---------------------------------------------------------------
def get_base64_image(path: str):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return None

# --- styling ---------------------------------------------------------------
bg_b64 = get_base64_image("themes/bg.jpg")
bg_css = (
    f"background-image: linear-gradient(rgba(26,12,18,0.45), rgba(26,12,18,0.65)), url('data:image/jpeg;base64,{bg_b64}');"
    if bg_b64 else "background-color: #110b11;"
)

st.markdown(
    f"""
    <style>
    [data-testid='stAppViewContainer'] {{
        {bg_css}
        background-size: cover !important;
        background-position: center center !important;
    }}
    .frosted {{
        background: rgba(30,15,23,0.28);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,102,170,0.18);
        border-radius: 14px;
        padding: 18px;
    }}
    [data-testid='stSidebar'] {{
        background: linear-gradient(rgba(20,10,15,0.35), rgba(20,10,15,0.25));
        backdrop-filter: blur(14px);
        border-right: 3px solid #ff66aa !important;
    }}
    h1,h2,h3,p,label,.stMarkdown,.stMetric,input,button {{
        font-family: 'Courier New', monospace !important;
        font-weight: 700 !important;
        color: #ffffff !important;
    }}
    .main .block-container {{ padding-top: 48px !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- header ---------------------------------------------------------------
st.markdown(
    """
    <div class="frosted" style="text-align:center; margin-bottom:18px;">
      <h1 style="color:#ff66aa; margin:0;">🌸 LORD'S ARCADE REALM 🌸</h1>
      <p style="margin:6px 0 0 0; color:#fff;">
