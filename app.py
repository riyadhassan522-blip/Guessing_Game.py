import streamlit as st
import random
import base64
import time

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
# PROCEDURAL RETRO AUDIO SYNTH ENGINE
# =========================================================================
def trigger_arcade_synth():
    """Generates an embedded, retro chiptune bleep directly through code"""
    audio_html = """
    <audio autoplay style="display:none;">
        <source src="data:audio/wav;base64,UklGRigAAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQQAAAAAf39/fw==" type="audio/wav">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# =========================================================================
# THE REVERTED CYBER ARCADE THEME ENGINE (WITH FIXED SIDEBAR DROPDOWN)
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

/* THE FROSTED GLASS SIDEBAR EFFECT */
[data-testid='stSidebar'], [data-testid='stSidebarUserContent'], section[data-testid='stSidebar'] > div:first-child {{
    background-color: rgba(30, 15, 23, 0.25) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border-right: 3px solid #ff66aa !important;
}}

/* 🌸 MAINFRAME INPUT SCANNER OVERRIDE: Fixes the invisible white text bug */
input[type="number"], [data-baseweb="input"] > div, .stNumberInput input {{
    background-color: rgba(37, 22, 31, 0.90) !important; /* Premium dark plum background */
    color: #ff66aa !important; /* High-contrast glowing pink text for your numbers */
    border: 2px solid rgba(255, 102, 170, 0.5) !important; /* Matching neon pink border line */
    border-radius: 8px !important;
    font-family: monospace !important;
    font-weight: bold !important;
}}

/* Ensure text stays bright pink while typing inside the scanner field */
.stNumberInput input:focus {{
    color: #ff66aa !important;
}}

/* Style the placeholder text safely */
input[type="number"]::placeholder {{
    color: rgba(255, 255, 255, 0.3) !important;
}}

/* 🌸 FIX FOR STARK WHITE SIDEBAR DROPDOWN BOXES 🌸 */
div[data-baseweb="select"] > div, 
div[data-baseweb="select"] ul {{
    background-color: rgba(37, 22, 31, 0.85) !important; /* Translucent cherry/plum box */
    border: 1px solid rgba(255, 102, 170, 0.4) !important; /* Neon outline */
    color: #ffffff !important; /* Crisp white input text */
}}

/* Force selection dropdown options text to match the dark color scheme */
div[data-baseweb="popover"] div, 
li[role="option"] {{
    background-color: #25161f !important;
    color: #ffffff !important;
}}

.stSelectbox div {{
    color: #ffffff !important;
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
}}
div.stButton > button:first-child:active {{
    transform: translateY(4px) !important;
    box-shadow: 0px 2px 0px #992255 !important;
}}
div.stButton > button:first-child:hover {{
    background: #ff88bb !important;
    color: #1a0c12 !important;
    border-color: #1a0c12 !important;
}}

/* Floating UI Panel Containers - Clear Glass Style */
div[data-testid='stForm'], .stMainBlockContainer {{
    background: transparent !important;                 
    background-color: transparent !important;
    backdrop-filter: none !important;                   
    -webkit-backdrop-filter: none !important;
    border: none !important;                            
    box-shadow: none !important;                        
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

# 2. BRANDING BANNER: SINGLE SYSTEM RECOVERY MODULE
banner_html = (
    "<div style='background-color: rgba(45, 20, 32, 0.40); backdrop-filter: blur(10px); padding: 25px; border-radius: 12px; text-align: center; border: 1px solid rgba(255, 102, 170, 0.25); box-shadow: 0px 4px 15px rgba(255, 102, 170, 0.1); margin-bottom: 35px;'>\n"
    "    <h1 style='color: #ff66aa; margin: 0; font-family: \"Courier New\", monospace; font-size: 2.3rem; letter-spacing: 2px; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>\n"
    "        🌸 LORD'S ARCADE REALM 🌸\n"
    "    </h1>\n"
    "    <p style='color: #ffffff; margin: 8px 0 0 0; font-size: 1rem; font-family: \"Courier New\", monospace; font-weight: bold; letter-spacing: 1px;'>\n"
    "        [ SYSTEM CORE MODULES // ENGINEERED BY: LORDDARKNESS393 ]\n"
    "    </p>\n"
    "</div>"
)
st.markdown(banner_html, unsafe_allow_html=True)

# 3. CONTROL PANEL CONFIGURATION
with st.sidebar:
    st.markdown("### ⚙️ SYSTEM SETTINGS")
    difficulty = st.selectbox(
        "Select Rank Boundary:", 
        ["1. Novice (1-20, 8 lives)", "2. Easy (1-50, 10 lives)", "3. Medium (1-100, 7 lives)", "4. Hard (1-200, 5 lives)", "5. Expert (1-500, 3 lives)"]
    )
    
    if "1." in difficulty: max_lives, max_range = 8, 20
    elif "2." in difficulty: max_lives, max_range = 10, 50
    elif "3." in difficulty: max_lives, max_range = 7, 100
    elif "4." in difficulty: max_lives, max_range = 5, 200
    else: max_lives, max_range = 3, 500

    if st.session_state.gg_active and st.session_state.gg_current_difficulty != difficulty:
        st.session_state.gg_active = False
        st.session_state.gg_feedback = "⚠️ BOUNDARY BREAK! Difficulty was switched. Re-initialize round engine."
        st.session_state.gg_feedback_type = "info"

    if st.button("🚀 DEPLOY CORE MATCH", use_container_width=True, type="primary"):
        # ANIMATED LOADING SCREEN TRANSITION
        with st.spinner("🔄 INITIALIZING MAINFRAME MODULE SYSTEM..."):
            time.sleep(1.2)  # Simulated processing loop delay
            trigger_arcade_synth()
            
        st.session_state.gg_secret_number = random.randint(1, max_range)
        st.session_state.gg_lives_left = max_lives
        st.session_state.gg_round_attempts = 0
        st.session_state.gg_active = True
        st.session_state.gg_current_difficulty = difficulty
        st.session_state.gg_feedback = "🎯 SYSTEM ENGINE LOADED. DISPATCH YOUR FIRST GUESS ANALYSIS."
        st.session_state.gg_feedback_type = "info"

    # PERSISTENT SCOREBOARD DASHBOARD
    st.markdown("---")
    st.markdown("### 📊 DASHBOARD STATS")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="PLAYED MATCHES", value=st.session_state.gg_played)
        st.metric(label="WINS RECORDED 🏆", value=st.session_state.gg_wins)
    with col2:
        st.metric(label="TOTAL GUESSES", value=st.session_state.gg_total_guesses)
        st.metric(label="CRASH LOSSES 💀", value=st.session_state.gg_losses)
        
    st.markdown("---")
    best_display = f"{st.session_state.gg_best_score} attempts" if st.session_state.gg_best_score else "No wins recorded"
    st.markdown(f"<p style='color: #ff66aa; font-family: monospace; font-size: 0.9rem; font-weight: bold; margin-top: 15px;'>🏆 BEST RECORD: <span style='color: #ffffff;'>{best_display}</span></p>", unsafe_allow_html=True)

# 4. INTERFACE PROCESSOR ROUTINE
if st.session_state.gg_active:
    with st.container(border=True):
        st.markdown(f"##### 🌸 Core Integrity: **{st.session_state.gg_lives_left} / {max_lives} Lives Remaining**")
        current_lives = max(0, st.session_state.gg_lives_left)
        st.progress(float(current_lives / max_lives))

    st.markdown(" ")

    with st.form(key="guess_form", clear_on_submit=True):
        guess = st.number_input(
            f"Target Scan Range [1 to {max_range}]:", 
            min_value=1, 
            max_value=max_range, 
            step=1, 
            value=None, 
            placeholder="Tap here to analyze a number path..."
        )
        submit_guess = st.form_submit_button("💥 SUBMIT SCAN RADAR", use_container_width=True)

    if submit_guess and guess is not None:
        trigger_arcade_synth()
        st.session_state.gg_round_attempts += 1
        st.session_state.gg_total_guesses += 1
        
        warm_threshold = max(3, max_range // 15)
        secret = st.session_state.gg_secret_number

        if guess < secret:
            st.session_state.gg_lives_left -= 1
            msg = f"📉 {guess} is Too Low!"
            if secret - guess <= warm_threshold: msg += " 👉 Radar signature getting warm!!"
            st.session_state.gg_feedback = msg
            st.session_state.gg_feedback_type = "warning"
        elif guess > secret:
            st.session_state.gg_lives_left -= 1
            msg = f"📈 {guess} is Too High!"
            if guess - secret <= warm_threshold: msg += " 👉 Radar signature getting warm!!"
            st.session_state.gg_feedback = msg
            st.session_state.gg_feedback_type = "warning"
        else:
            st.session_state.gg_feedback = f"🎉 MAINFRAME ACCESS SECURED! Encryption cracked in {st.session_state.gg_round_attempts} attempts!"
            st.session_state.gg_feedback_type = "success"
            st.session_state.gg_wins += 1
            st.session_state.gg_played += 1
            if st.session_state.gg_best_score is None or st.session_state.gg_round_attempts < st.session_state.gg_best_score:
                st.session_state.gg_best_score = st.session_state.gg_round_attempts
                st.toast("🌸 NEW MAINFRAME CORE SPEED-RECORD SET! 🌸")
            st.session_state.gg_active = False

        if st.session_state.gg_lives_left <= 0 and st.session_state.gg_active:
            st.session_state.gg_feedback = f"💀 PROTOCOL ABORTED! System crashed. Core signature code was: {secret}."
            st.session_state.gg_feedback_type = "error"
            st.session_state.gg_losses += 1
            st.session_state.gg_played += 1
            st.session_state.gg_active = False

    if "gg_feedback" in st.session_state:
        if st.session_state.gg_feedback_type == "success": st.success(st.session_state.gg_feedback)
        elif st.session_state.gg_feedback_type == "warning": st.warning(st.session_state.gg_feedback)
        elif st.session_state.gg_feedback_type == "error": st.error(st.session_state.gg_feedback)
        else: st.info(st.session_state.gg_feedback)
else:
    if "gg_feedback" in st.session_state and "changed mid-game" in st.session_state.gg_feedback:
        st.info(st.session_state.gg_feedback)
    else:
        idle_html = (
            "<div style='text-align: center; padding: 40px 20px; background-color: rgba(45, 20, 32, 0.40); backdrop-filter: blur(10px); border: 4px dashed #ff66aa; box-shadow: 0px 4px 15px rgba(255, 102, 170, 0.15);'>"
            "<p style='font-size: 1.3rem; color: #ff66aa; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>STATUS // PLATFORM IDLE</p>"
            "<p style='font-size: 0.95rem; color: #ffffff; font-weight: bold; margin-top: 10px;'>Initialize the left matrix panel to deploy your first gameplay module round!</p>"
            "</div>"
        )
        st.markdown(idle_html, unsafe_allow_html=True)

# 5. STUDIO PRODUCTION INSIGNIA
footer_html = "<div style='text-align: center; padding: 10px; margin-top: 30px;'><p style='color: #614653; font-family: \"Courier New\", monospace; font-size: 0.85rem; margin: 0; font-weight: bold;'>© 2026 DARKNESS GAMING LABS | ALL RIGHTS RESERVED</p><p style='color: #ff66aa; font-family: \"Courier New\", monospace; font-size: 1rem; margin: 5px 0 0 0; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</p></div>"
st.markdown("---")
st.markdown(footer_html, unsafe_allow_html=True)
