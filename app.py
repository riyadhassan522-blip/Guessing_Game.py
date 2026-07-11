import streamlit as st
import base64

# 1. PLATFORM LOBBY MODULE FRAMEWORK
st.set_page_config(
    page_title="Lord's Arcade Realm", 
    page_icon="🌸", 
    layout="centered"
)

# Graphic pipeline asset encoder
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""

bg_base64 = get_base64_image("themes/bg.jpg")

# =========================================================================
# THE CEL-SHADED ARCADE THEME ENGINE (Matches Guessing Game perfectly)
# =========================================================================
css_style = f"""
<style>
/* Full screen high-contrast canvas wallpaper overlay layer */
.stApp, [data-testid='stAppViewContainer'], .stAppHeader, [data-testid='stHeader'] {{
    background-image: linear-gradient(rgba(26, 12, 18, 0.45), rgba(26, 12, 18, 0.65)), 
                url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important;
    background-position: center center !important;
    background-attachment: fixed !important;
}}

/* Unifies premium monospace typography guidelines */
html, body, p, span, label, div, h1, h2, h3, a {{
    font-family: 'Courier New', Courier, monospace !important;
    font-weight: bold !important;
}}

/* THE GLASS SIDEBAR PANEL EFFECT */
[data-testid='stSidebar'], [data-testid='stSidebarUserContent'], section[data-testid='stSidebar'] > div:first-child {{
    background-color: rgba(30, 15, 23, 0.20) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border-right: 3px solid #ff66aa !important;
}}

/* Unify navigation list links inside custom cherry rows */
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

/* REVERTED TO THE ELEGANT MAIN CONTENT PANEL CONTAINER */
.stMainBlockContainer {{
    background-color: rgba(35, 16, 25, 0.75) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 4px solid #1a0c12 !important;
    border-radius: 12px !important;
    box-shadow: 8px 8px 0px #1a0c12 !important;
    padding: 35px !important;
    margin-top: 50px !important;
}}

/* Wipes out platform arrow controllers to prevent layout overlaps */
button[aria-label="Collapse sidebar"], button[aria-label="Expand sidebar"] {{
    display: none !important;
}}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# =========================================================================
# LOBBY ARCADE GATE OVERLAY PANEL
# =========================================================================
banner_html = (
    "<div style='background-color: rgba(45, 20, 32, 0.82); backdrop-filter: blur(10px); padding: 25px; border-radius: 12px; text-align: center; border: 4px solid #1a0c12; box-shadow: 8px 8px 0px #1a0c12; margin-bottom: 35px;'>\n"
    "    <h1 style='color: #ff66aa; margin: 0; font-family: \"Courier New\", monospace; font-size: 2.3rem; letter-spacing: 2px; font-weight: 900; text-shadow: 3px 3px 0px #1a0c12;'>\n"
    "        🌸 LORD'S ARCADE REALM 🌸\n"
    "    </h1>\n"
    "    <p style='color: #ffffff; margin: 8px 0 0 0; font-size: 1rem; font-family: \"Courier New\", monospace; font-weight: bold; letter-spacing: 1px;'>\n"
    "        [ SYSTEM CORE MODULES // ENGINEERED BY: LORDDARKNESS393 ]\n"
    "    </p>\n"
    "</div>"
)
st.markdown(banner_html, unsafe_allow_html=True)

st.markdown("### 🕹️ LOBBY MAIN RECOVERY CORE")
st.markdown("---")
st.markdown("Your retro gaming console framework has been successfully updated and re-aligned.")
st.info("💡 TRANSMISSION: Slide open the left system matrix panel to choose and switch between your active game modules natively!")

footer_html = "<div style='text-align: center; padding: 10px; margin-top: 50px;'><p style='color: #ff66aa; font-family: \"Courier New\", monospace; font-size: 1rem; margin: 5px 0 0 0; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</p></div>"
st.markdown("---")
st.markdown(footer_html, unsafe_allow_html=True)
