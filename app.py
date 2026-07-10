import streamlit as st
import random
import base64

# 1. APPLICATION ENVIRONMENT FRAMEWORK
st.set_page_config(
    page_title="Lord's Arcade Realm", 
    page_icon="🌸", 
    layout="centered"
)

# Initialize Session Memory exactly matching your core logic variables
if "gg_played" not in st.session_state:
    st.session_state.gg_played = 0
    st.session_state.gg_wins = 0
    st.session_state.gg_losses = 0
    st.session_state.gg_total_guesses = 0
    st.session_state.gg_best_score = None
    st.session_state.gg_active = False
    st.session_state.gg_current_difficulty = None

# =========================================================================
# NATIVE IMAGE ENCODER FOR LOCAL BACKGROUND FILES
# =========================================================================
def get_base64_image(image_path):
    """Converts local repository image bytes to embedded web graphics"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""

# Pull your custom waterfall pagoda art straight from your correct GitHub path
bg_base64 = get_base64_image("themes/bg.jpg")

# =========================================================================
# 3D CEL-SHADED GAMING ENGINE (With Frosted Glass Sidebar Layout)
# =========================================================================
css_style = f"""
<style>
/* Forces the web engine to prioritize your background image over config colors */
.stApp, [data-testid='stAppViewContainer'], .stAppHeader, [data-testid='stHeader'] {{
    background: linear-gradient(rgba(26, 12, 18, 0.45), rgba(26, 12, 18, 0.65)), 
                url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important;
    background-position: center center !important;
    background-attachment: fixed !important;
}}

/* THE FROSTED GLASS SIDEBAR EFFECT: Low opacity layer with deep backdrop pixel blurring */
[data-testid='stSidebar'], [data-testid='stSidebarUserContent'], section[data-testid='stSidebar'] > div:first-child {{
    background-color: rgba(30, 15, 23, 0.20) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border-right: 3px solid #ff66aa !important;
}}

/* Retro Arcade 3D Button Style */
div.stButton > button:first-child {{
    background: #ff66aa !important;
    color: #1a0c12 !important;
    border: 3px solid #1a0c12 !important;
    font-weight: 900 !important;
    font-size: 1.1rem !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    border-radius: 8px !important;
    box-shadow: 0px 6px 0px #992255 !important;
    transition: all 0.1s ease-in-out !important;
    margin-bottom: 6px !important;
    width: 100% !important;
}
div.stButton > button:first-child:active {{
    transform: translateY(4px) !important;
    box-shadow: 0px 2px 0px #992255 !important;
}}
div.stButton > button:first-child:hover {{
    background: #ff88bb !important;
    color: #1a0c12 !important;
    border-color: #1a0c12 !important;
}}

/* Floating Semi-Transparent UI Panel Containers - Glassmorphism touch */
div[data-testid='stForm'], .stMainBlockContainer, .stCustomComponentV1 {{
    background-color: rgba(35, 16, 25, 0.75) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 4px solid #1a0c12 !important;
    border-radius: 12px !important;
    box-shadow: 8px 8px 0px #1a0c12 !important;
    padding: 25px !important;
    max-width: 100% !important;
}}
div[data-testid='stMetricValue'] {{
    font-weight: 900 !important;
    color: #ff66aa !important;
    text-shadow: 2px 2px 0px #1a0c12 !important;
    font-size: 1.8rem !important;
}}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)
