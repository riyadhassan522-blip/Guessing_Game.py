import streamlit as st
import base64

# 1. SETUP MASTER REPOSITORY PROPERTIES
st.set_page_config(
    page_title="Lord's Arcade Realm", 
    page_icon="🌸", 
    layout="centered"
)

# 2. DEFINITIVE ARCADES DICTIONARY CONFIGURATION
st.navigation([
    st.Page("app.py", title="🌸 MAIN LOBBY"),
    st.Page("pages/Guessing_Game.py", title="🎯 RADAR SCANNER")
])

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""

bg_base64 = get_base64_image("themes/bg.jpg")

css_style = f"""
<style>
.stApp, [data-testid='stAppViewContainer'], .stAppHeader, [data-testid='stHeader'] {{
    background-image: linear-gradient(rgba(26, 12, 18, 0.45), rgba(26, 12, 18, 0.65)), 
                url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important; background-position: center center !important; background-attachment: fixed !important;
}}

/* 🎯 SAFE TYPOGRAPHY FILTER: Explicitly skips icon elements so the browser icons load natively */
*:not(i):not([class*="icon"]):not([class*="Icon"]):not([class*="material"]) {{
    font-family: 'Courier New', Courier, monospace !important;
    font-weight: bold !important;
}}

/* THE GLORIOUS FROSTED GLASS SIDEBAR AREA */
[data-testid='stSidebar'], [data-testid='stSidebarUserContent'], section[data-testid='stSidebar'] > div:first-child {{
    background-color: rgba(30, 15, 23, 0.20) !important; backdrop-filter: blur(16px) !important; border-right: 3px solid #ff66aa !important;
}}
[data-testid="stSidebarNav"] ul {{
    background-color: rgba(37, 22, 31, 0.70) !important; border-radius: 12px !important; border: 1px solid rgba(255, 102, 170, 0.4) !important; padding: 10px !important; margin-top: 15px !important;
}}
[data-testid="stSidebarNav"] span {{ color: #ffffff !important; font-size: 1.05rem !important; }}

.main .block-container {{ padding-top: 60px !important; }}
.stMainBlockContainer {{
    background-color: rgba(37, 22, 31, 0.45) !important; backdrop-filter: blur(16px) !important;
    border: 2px solid rgba(255, 102, 170, 0.4) !important; border-radius: 24px !important; box-shadow: 0px 8px 32px rgba(255, 102, 170, 0.15) !important; padding: 35px !important;
}}

/* Clean up upper layout utility background headers safely */
[data-testid="stHeader"], .stAppHeader, div.stAppViewContainer > div:first-child {{
    display: none !important; opacity: 0 !important; height: 0px !important;
}}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

banner_html = (
    "<div style='background-color: rgba(45, 20, 32, 0.45); backdrop-filter: blur(12px); padding: 25px; border-radius: 16px; text-align: center; border: 1px solid rgba(255, 102, 170, 0.25); box-shadow: 0px 4px 15px rgba(255, 102, 170, 0.1); margin-bottom: 35px;'>\n"
    "    <h1 style='color: #ff66aa; margin: 0; font-family: \"Courier New\", monospace; font-size: 2.3rem; letter-spacing: 2px; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>\n"
    "        🌸 LORD'S ARCADE REALM 🌸\n"
    "    </h1>\n"
    "    <p style='color: #ffffff; margin: 8px 0 0 0; font-size: 1rem; font-family: \"Courier New\", monospace; font-weight: bold; letter-spacing: 1px;'>\n"
    "        [ SYSTEM CORE MODULES // CHIEF ENGINEER: LORDDARKNESS393 ]\n"
    "    </p>\n"
    "</div>"
)
st.markdown(banner_html, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("---")
    st.markdown("### 🖥️ DIAGNOSTIC CORE")
    st.markdown("● **STATUS:** `ONLINE` ⚡")
    st.markdown("● **ENGINES:** `01 MODULE` 💾")
    st.markdown("---")

st.markdown("### 🕹️ LOBBY TERMINAL HUB ONLINE")
st.markdown("---")
st.markdown("Your retro gaming console framework has been successfully updated and re-aligned to full cross-platform glass dictionary specs.")
st.info("💡 TRANSMISSION PANEL: Pop open your left-side matrix link drawer options to deploy your game channels natively!")

footer_html = "<div style='text-align: center; padding: 10px; margin-top: 50px;'><p style='color: #ff66aa; font-family: \"Courier New\", monospace; font-size: 1rem; margin: 5px 0 0 0; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</p></div>"
st.markdown("---"); st.markdown(footer_html, unsafe_allow_html=True)
