import streamlit as st
import random
import base64
import time

# 1. SETUP ENVIRONMENT VIEWPORT
st.set_page_config(
    page_title="Lord's Arcade Realm", 
    page_icon="🌸", 
    layout="centered"
)

# Initialize Absolute Platform Core State Variables
if "active_channel" not in st.session_state: st.session_state.active_channel = "LOBBY"
if "gg_played" not in st.session_state: st.session_state.gg_played = 0
if "gg_wins" not in st.session_state: st.session_state.gg_wins = 0
if "gg_losses" not in st.session_state: st.session_state.gg_losses = 0
if "gg_total_guesses" not in st.session_state: st.session_state.gg_total_guesses = 0
if "gg_best_score" not in st.session_state: st.session_state.gg_best_score = None
if "gg_active" not in st.session_state: st.session_state.gg_active = False
if "gg_current_difficulty" not in st.session_state: st.session_state.gg_current_difficulty = None
if "ttt_played" not in st.session_state: st.session_state.ttt_played = 0
if "ttt_wins" not in st.session_state: st.session_state.ttt_wins = 0
if "ttt_losses" not in st.session_state: st.session_state.ttt_losses = 0
if "ttt_ties" not in st.session_state: st.session_state.ttt_ties = 0
if "ttt_board" not in st.session_state: st.session_state.ttt_board = [" " for _ in range(9)]
if "ttt_score_locked" not in st.session_state: st.session_state.ttt_score_locked = False

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file: return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError: return ""

bg_base64 = get_base64_image("themes/bg.jpg")

def trigger_arcade_synth():
    st.markdown("""<audio autoplay style="display:none;"><source src="data:audio/wav;base64,UklGRigAAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQQAAAAAf39/fw==" type="audio/wav"></audio>""", unsafe_allow_html=True)

# =========================================================================
# THE ULTIMATE UNIFIED GLASS INTERFACE STYLING CONFIGURATION
# =========================================================================
css_style = f"""
<style>
.stApp, [data-testid='stAppViewContainer'], .stAppHeader, [data-testid='stHeader'] {{
    background-image: linear-gradient(rgba(26, 12, 18, 0.45), rgba(26, 12, 18, 0.65)), url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important; background-position: center center !important; background-attachment: fixed !important;
}}
html, body, p, span, label, div, h1, h2, h3, button, input {{ font-family: 'Courier New', Courier, monospace !important; font-weight: bold !important; }}

/* PREVENTS TOP CUTOFF BY DROPPING INTERFACE DOWN COMFORTABLY */
.main .block-container {{ padding-top: 50px !important; }}

/* PREMIUM TRANSLUCENT GLOWING GLASS HOUSING WINDOW PANELS */
div[data-testid='stForm'], div[data-testid='stVerticalBlock'] > div[style*="border"], .stMainBlockContainer > div {{
    background-color: rgba(37, 22, 31, 0.45) !important; backdrop-filter: blur(16px) !important; -webkit-backdrop-filter: blur(16px) !important;
    border: 2px solid rgba(255, 102, 170, 0.4) !important; border-radius: 24px !important; padding: 30px !important;
    box-shadow: 0px 8px 32px rgba(255, 102, 170, 0.15) !important; margin-bottom: 25px !important;
}}
.stMainBlockContainer {{ background: transparent !important; padding: 0 !important; max-width: 100% !important; }}

/* RETRO ARCADE 3D COMMAND NAVIGATION ACTION BUTTONS */
div.stButton > button {{
    background: #ff66aa !important; color: #1a0c12 !important; border: 3px solid #1a0c12 !important; font-weight: 900 !important;
    font-size: 1.1rem !important; text-transform: uppercase !important; letter-spacing: 2px !important; border-radius: 8px !important;
    box-shadow: 0px 6px 0px #992255 !important; transition: all 0.1s ease-in-out !important; width: 100% !important; height: 48px !important;
}}
div.stButton > button:active {{ transform: translateY(4px) !important; box-shadow: 0px 2px 0px #992255 !important; }}
div[data-testid="stTextInput"] [data-baseweb="input"] {{ background-color: rgba(37, 22, 31, 0.90) !important; border: 2px solid rgba(255, 102, 170, 0.5) !important; border-radius: 8px !important; }}
div[data-testid="stTextInput"] input {{ background-color: transparent !important; color: #ff66aa !important; font-size: 1.1rem !important; }}
div[data-testid="stTextInput"] [data-baseweb="input"] + div {{ display: none !important; }}
div[data-testid='stMetricValue'] {{ font-weight: 900 !important; color: #ff66aa !important; text-shadow: 2px 2px 0px #1a0c12 !important; font-size: 1.5rem !important; }}

/* 🎯 HIGH-DENSITY HIGH-COMPACT TIC-TAC-TOE MATRIX CELLS */
.ttt-container {{ display: flex; justify-content: center; margin: 15px 0; }}
.ttt-table {{ border-collapse: collapse; border: 3px solid rgba(255, 102, 170, 0.6) !important; border-radius: 12px !important; overflow: hidden; }}
.ttt-cell {{ width: 66px !important; height: 68px !important; text-align: center; border: 2px solid rgba(255, 102, 170, 0.3) !important; padding: 0 !important; margin: 0 !important; }}
.ttt-btn {{
    width: 100% !important; height: 100% !important; background-color: rgba(37, 22, 31, 0.60) !important; backdrop-filter: blur(10px) !important;
    color: #ff66aa !important; border: none !important; font-size: 1.6rem !important; font-weight: 900 !important; cursor: pointer; transition: all 0.1s;
}}
.ttt-btn:hover:not(:disabled) {{ background-color: rgba(255, 102, 170, 0.15) !important; }}

/* 🚨 PERMANENT SIDEBAR DESTRUCTION: Wipes out sidebar containers, toggles, headers, and text labels completely */
[data-testid="stSidebar"], [data-testid="collapsedControl"], [data-testid="stHeader"], .stAppHeader, div.stAppViewContainer > div:first-child {{
    display: none !important; visibility: hidden !important; opacity: 0 !important; height: 0px !important; width: 0px !important;
}}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# Global Branding Header Box Layout
st.markdown("<div style='background-color: rgba(45, 20, 32, 0.40); backdrop-filter: blur(10px); padding: 25px; border-radius: 16px; text-align: center; border: 1px solid rgba(255, 102, 170, 0.25); box-shadow: 0px 4px 15px rgba(255, 102, 170, 0.1); margin-bottom: 35px;'><h1 style='color: #ff66aa; margin: 0; font-family: \"Courier New\", monospace; font-size: 2.3rem; letter-spacing: 2px; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>🌸 LORD'S ARCADE REALM 🌸</h1></div>", unsafe_allow_html=True)
