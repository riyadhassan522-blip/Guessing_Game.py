import streamlit as st
import base64

# 1. APPLICATION LOBBY INSTANCE DEFINITION
st.set_page_config(
    page_title="Lord's Arcade Realm", 
    page_icon="🌸", 
    layout="centered"
)

# =========================================================================
# GRAPHIC LAYER ENCODER MODULE
# =========================================================================
def get_base64_image(image_path):
    """Converts local repository image bytes to embedded web graphics"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""

# Pull your custom waterfall pagoda art straight from your themes directory
bg_base64 = get_base64_image("themes/bg.jpg")

# =========================================================================
# LOBBY DISPLAY ENGINE: UNIFIED MONOSPACE BALANCING
# =========================================================================
css_style = f"""
<style>
/* Forces your local background image to stretch beautifully across the screen */
.stApp, [data-testid='stAppViewContainer'], .stAppHeader, [data-testid='stHeader'] {{
    background-image: linear-gradient(rgba(26, 12, 18, 0.45), rgba(26, 12, 18, 0.65)), 
                url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important;
    background-position: center center !important;
    background-attachment: fixed !important;
}}

/* Set premium uniform typography matching the arcade portal aesthetic */
html, body, p, span, label, div, h1, h2, h3 {{
    font-family: 'Courier New', Courier, monospace !important;
    font-weight: bold !important;
}}

/* THE FROSTED GLASS SIDEBAR NAVIGATION MANAGEMENT DRAWERS */
[data-testid='stSidebar'], [data-testid='stSidebarUserContent'], section[data-testid='stSidebar'] > div:first-child {{
    background-color: rgba(30, 15, 23, 0.25) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border-right: 3px solid #ff66aa !important;
}}

/* Clean typography panel styling inside the automatic pages links loop */
[data-testid="stSidebarNav"] ul {{
    background-color: rgba(37, 22, 31, 0.60) !important;
    border-radius: 8px !important;
    border: 1px solid rgba(255, 102, 170, 0.2) !important;
    padding: 12px !important;
    margin-top: 20px !important;
}}

[data-testid="stSidebarNav"] span {{
    color: #ffffff !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.5px !important;
}}

/* Wipes out native collapse controllers to prevent mobile alignment overlaps */
button[aria-label="Collapse sidebar"], 
button[aria-label="Expand sidebar"] {{
    display: none !important;
    opacity: 0 !important;
}}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# =========================================================================
# CENTRAL ARCADE TERMINAL INTERFACE MATRIX OVERLAY PANEL
# =========================================================================
st.markdown(
    "<div style='background-color: rgba(45, 20, 32, 0.45); backdrop-filter: blur(12px); padding: 35px; border-radius: 16px; text-align: center; border: 1px solid rgba(255, 102, 170, 0.25); box-shadow: 0px 8px 32px rgba(255, 102, 170, 0.15); margin-top: 60px;'>\n"
    "    <h1 style='color: #ff66aa; margin: 0; font-size: 2.6rem; letter-spacing: 2px; text-shadow: 3px 3px 0px #1a0c12;'>🌸 WELCOME TO THE REALM 🌸</h1>\n"
    "    <p style='color: #ffffff; margin: 15px 0 0 0; font-size: 1.1rem; letter-spacing: 1px; font-weight: bold;'>[ ARCADE CENTRAL MAINFRAME HUB // CHIEF ENGINEER: LORDDARKNESS393 ]</p>\n"
    "    <hr style='border: none; border-top: 2px dashed rgba(255, 102, 170, 0.25); margin: 30px 0;'>\n"
    "    <p style='color: #ff88bb; font-size: 1.05rem; line-height: 1.6; margin-bottom: 5px;'>The terminal framework database has been successfully updated and re-organized.</p>\n"
    "    <p style='color: #ffffff; font-size: 0.95rem; opacity: 0.9;'>Deploy and swap your active gameplay engine cores natively from the left side matrix link options panel!</p>\n"
    "</div>",
    unsafe_allow_html=True
)

# 4. PLATFORM FOOTER SIGN-OFF BRANDING INSIGNIA
footer_html = "<div style='text-align: center; padding: 10px; margin-top: 50px;'><p style='color: #614653; font-family: \"Courier New\", monospace; font-size: 0.85rem; margin: 0; font-weight: bold;'>© 2026 DARKNESS GAMING LABS | ALL RIGHTS RESERVED</p><p style='color: #ff66aa; font-family: \"Courier New\", monospace; font-size: 1rem; margin: 5px 0 0 0; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</p></div>"
st.markdown("---")
st.markdown(footer_html, unsafe_allow_html=True)
