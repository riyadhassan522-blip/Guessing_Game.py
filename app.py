import streamlit as st
import base64

# 1. APPLICATION ENVIRONMENT FRAMEWORK
st.set_page_config(
    page_title="Lord's Arcade Realm", 
    page_icon="🌸", 
    layout="centered"
)

# =========================================================================
# GRAPHIC LAYER ENCODER MODULE
# =========================================================================
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""

bg_base64 = get_base64_image("themes/bg.jpg")

# =========================================================================
# THE LOBBY INTERFACE ENGINE: ULTRA-SLIM STYLE OVERRIDES
# =========================================================================
css_style = f"""
<style>
/* Stretch the custom wallpaper across the entire layout grid frame safely */
.stApp, [data-testid='stAppViewContainer'], .stAppHeader, [data-testid='stHeader'] {{
    background-image: linear-gradient(rgba(26, 12, 18, 0.45), rgba(26, 12, 18, 0.65)), 
                url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important;
    background-position: center center !important;
    background-attachment: fixed !important;
}}

/* Clean custom monospace typography blueprint */
html, body, p, span, label, div, h1, h2, h3, a {{
    font-family: 'Courier New', Courier, monospace !important;
    font-weight: bold !important;
}}

/* THE GLASS SIDEBAR NAVIGATION DRAWERS: Completely restored and visible */
[data-testid='stSidebar'], [data-testid='stSidebarUserContent'], section[data-testid='stSidebar'] > div:first-child {{
    background-color: rgba(30, 15, 23, 0.35) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border-right: 3px solid #ff66aa !important;
    display: block !important;
    visibility: visible !important;
}}

/* Unify navigation lists into beautiful glowing arcade selection rows */
[data-testid="stSidebarNav"] {{
    display: block !important;
    visibility: visible !important;
}}

[data-testid="stSidebarNav"] ul {{
    background-color: rgba(37, 22, 31, 0.70) !important;
    border-radius: 8px !important;
    border: 2px solid rgba(255, 102, 170, 0.4) !important;
    padding: 10px !important;
    margin-top: 30px !important;
}}

[data-testid="stSidebarNav"] span {{
    color: #ffffff !important;
    font-size: 1.05rem !important;
}}

/* Remove default header bars while keeping mobile toggle logic fully functional */
[data-testid="stHeader"] {{
    background: transparent !important;
    background-color: transparent !important;
}}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# =========================================================================
# CENTRAL ARCADE LOBBY: THE REFINED MINIMALIST OVERLAY PANEL
# =========================================================================
st.markdown(
    "<div style='background-color: rgba(45, 20, 32, 0.50); backdrop-filter: blur(12px); padding: 40px 25px; border-radius: 16px; text-align: center; border: 1px solid rgba(255, 102, 170, 0.25); box-shadow: 0px 8px 32px rgba(255, 102, 170, 0.15); margin-top: 100px;'>\n"
    "    <h1 style='color: #ff66aa; margin: 0; font-size: 2.5rem; letter-spacing: 3px; text-shadow: 3px 3px 0px #1a0c12;'>🌸 LORD'S ARCADE REALM 🌸</h1>\n"
    "    <p style='color: #ffffff; margin: 15px 0 0 0; font-size: 1.05rem; letter-spacing: 1px; opacity: 0.9;'>[ CHIEF ENGINEER: LORDDARKNESS393 ]</p>\n"
    "</div>",
    unsafe_allow_html=True
)

# 4. SYSTEM PRODUCTION INSIGNIA
footer_html = "<div style='text-align: center; padding: 10px; margin-top: 120px;'><p style='color: #614653; font-family: \"Courier New\", monospace; font-size: 0.85rem; margin: 0; font-weight: bold;'>© 2026 DARKNESS GAMING LABS | ALL RIGHTS RESERVED</p></div>"
st.markdown(footer_html, unsafe_allow_html=True)
