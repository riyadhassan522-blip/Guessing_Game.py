import streamlit as st
import base64

st.set_page_config(
    page_title="Lord's Arcade Realm", 
    page_icon="🌸", 
    layout="centered"
)

# =========================================================================
# UNIVERSAL MEMORY MATRIX SETTINGS
# =========================================================================
if "theme_glow" not in st.session_state:
    st.session_state.theme_glow = "🌸 Cyber Cherry Blossom"
if "theme_bg_file" not in st.session_state:
    st.session_state.theme_bg_file = "Pagoda Waterfall (Default)"

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""

# Dynamic asset loader based on sidebar switcher adjustments
if st.session_state.theme_bg_file == "Retro Arcade Cabinet Room":
    bg_base64 = get_base64_image("themes/bg2.jpg")  # Tries loading your second artwork file safely
else:
    bg_base64 = get_base64_image("themes/bg.jpg")   # Default Pagoda landscape art path

# Active color palette selection matrix data maps
if "🧪 Toxic Lime Green" in st.session_state.theme_glow:
    glow_color = "#39ff14"
    shadow_color = "#139900"
    glass_base = "rgba(18, 30, 20, 0.45)"
elif "🔥 Synthwave Laser Orange" in st.session_state.theme_glow:
    glow_color = "#ff6600"
    shadow_color = "#992200"
    glass_base = "rgba(35, 18, 14, 0.45)"
else:
    glow_color = "#ff66aa"  # Default Cyber Cherry Blossom parameters
    shadow_color = "#992255"
    glass_base = "rgba(37, 22, 31, 0.45)"

# =========================================================================
# THE REBUILD COMPACT GRAPHICS MATRIX ENGINE
# =========================================================================
css_style = f"""
<style>
.stApp, [data-testid='stAppViewContainer'], .stAppHeader, [data-testid='stHeader'] {{
    background-image: linear-gradient(rgba(15, 10, 14, 0.50), rgba(15, 10, 14, 0.70)), 
                url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important; background-position: center center !important; background-attachment: fixed !important;
}}

/* Safe Monospace Typography: Leaves default system icon font bundles uninfected */
h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stMetric, input, button, span:not([class*="Icon"]):not([class*="icon"]):not([class*="material"]) {{
    font-family: 'Courier New', Courier, monospace !important; font-weight: bold !important;
}}

[data-testid='stSidebar'], [data-testid='stSidebarUserContent'], section[data-testid='stSidebar'] > div:first-child {{
    background-color: rgba(30, 15, 23, 0.20) !important; backdrop-filter: blur(16px) !important; border-right: 3px solid {glow_color} !important;
    display: block !important; visibility: visible !important;
}}
[data-testid="stSidebarNav"] ul {{
    background-color: rgba(30, 15, 23, 0.75) !important; border-radius: 8px !important; border: 1px solid rgba(255, 102, 170, 0.2) !important; padding: 10px !important; margin-top: 15px !important;
}}
[data-testid="stSidebarNav"] span {{ color: #ffffff !important; }}

.main .block-container {{ padding-top: 60px !important; }}
.stMainBlockContainer {{
    background-color: {glass_base} !important; backdrop-filter: blur(16px) !important; -webkit-backdrop-filter: blur(16px) !important;
    border: 2px solid {glow_color}44 !important; border-radius: 24px !important; box-shadow: 0px 8px 32px rgba(0,0,0,0.2) !important; padding: 35px !important;
}}

/* Selective Toolbar Eraser Block */
[data-testid="stHeader"], .stAppHeader, div.stAppViewContainer > div:first-child, [data-testid="collapsedControl"] {{
    display: none !important; opacity: 0 !important; height: 0px !important; width: 0px !important;
}}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# =========================================================================
# DYNAMIC THEME CONTROLLER SIDEBAR TOOLBAR PANEL
# =========================================================================
with st.sidebar:
    st.markdown("---")
    st.markdown("### 🎨 CABINET INTERFACE")
    
    # Live variables processing toggles natively mapping values across system state parameters
    sel_glow = st.selectbox("NEON NEON COLOR:", ["🌸 Cyber Cherry Blossom", "🧪 Toxic Lime Green", "🔥 Synthwave Laser Orange"], index=["🌸 Cyber Cherry Blossom", "🧪 Toxic Lime Green", "🔥 Synthwave Laser Orange"].index(st.session_state.theme_glow))
    sel_bg = st.selectbox("BACKGROUND ARTWORK:", ["Pagoda Waterfall (Default)", "Retro Arcade Cabinet Room"], index=["Pagoda Waterfall (Default)", "Retro Arcade Cabinet Room"].index(st.session_state.theme_bg_file))
    
    if sel_glow != st.session_state.theme_glow or sel_bg != st.session_state.theme_bg_file:
        st.session_state.theme_glow = sel_glow
        st.session_state.theme_bg_file = sel_bg
        st.rerun()
    st.markdown("---")

banner_html = f"""
<div style='background-color: rgba(45, 20, 32, 0.45); backdrop-filter: blur(12px); padding: 25px; border-radius: 12px; text-align: center; border: 1px solid {glow_color}44; box-shadow: 0px 4px 15px rgba(0,0,0,0.2); margin-bottom: 35px;'>
    <h1 style='color: {glow_color}; margin: 0; font-family: "Courier New", monospace; font-size: 2.3rem; letter-spacing: 2px; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>
        🌸 LORD'S ARCADE REALM 🌸
    </h1>
    <p style='color: #ffffff; margin: 8px 0 0 0; font-size: 1rem; font-family: "Courier New", monospace; font-weight: bold; letter-spacing: 1px;'>
        [ SYSTEM THEME MATRIX REVOLVER // CHIEF: LORDDARKNESS393 ]
    </p>
</div>
"""
st.markdown(banner_html, unsafe_allow_html=True)

st.markdown("### 🕹️ LOBBY MAIN CENTRAL RECOVERY CORE")
st.markdown("---")
st.markdown(f"Your retro custom terminal interface has been re-aligned. Currently processing variant grid parameters for theme selection profile matrix: **{st.session_state.theme_glow}**.")
st.info("💡 TRANSMISSION PANEL: Pop open your left-side matrix link drawer options to deploy your game channels natively!")

footer_html = f"<div style='text-align: center; padding: 10px; margin-top: 50px;'><p style='color: {glow_color}; font-family: \"Courier New\", monospace; font-size: 1rem; margin: 5px 0 0 0; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</p></div>"
st.markdown("---"); st.markdown(footer_html, unsafe_allow_html=True)
