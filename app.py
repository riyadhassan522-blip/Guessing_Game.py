import streamlit as st
import random

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

import base64

# =========================================================================
# GRAPHIC LAYER ENCODER MODULE
# =========================================================================
def get_base64_image(image_path):
    """Converts your local background file directly into safe web graphics string"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""

# Convert your local waterfall background layout asset
bg_base64 = get_base64_image("themes/bg.jpg")

# =========================================================================
# 3D CEL-SHADED GAMING ENGINE (Safe Flat String CSS Engine with Sidebar Blur)
# =========================================================================
css_style = f"""
<style>
@keyframes entryPop {{
    0% {{ transform: scale(0.96); opacity: 0; }}
    100% {{ transform: scale(1); opacity: 1; }}
}}
/* Targets both main view containers to load your raw Japanese pagoda background art */
.stApp, [data-testid='stAppViewContainer'] {{
    background-image: linear-gradient(rgba(26, 12, 18, 0.65), rgba(26, 12, 18, 0.78)), url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important;
    background-position: center center !important;
    background-attachment: fixed !important;
    animation: entryPop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards !important;
}}
/* FIXED SIDEBAR: Destroys the solid sidebar layout to force clean glass blur */
[data-testid='stSidebar'], [data-testid='stSidebarUserContent'], section[data-testid='stSidebar'] > div:first-child {{
    background-color: rgba(30, 15, 23, 0.30) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    border-right: 3px solid #ff66aa !important;
}}
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
div[data-testid='stForm'], .stMainBlockContainer {{
    background-color: rgba(45, 20, 32, 0.85) !important;
    backdrop-filter: blur(10px) !important;
    border: 4px solid #1a0c12 !important;
    border-radius: 12px !important;
    box-shadow: 8px 8px 0px #1a0c12 !important;
    padding: 20px !important;
    max-width: 100% !important;
}}
div[data-testid='stMetricValue'] {{
    font-weight: 900 !important;
    color: #ff66aa !important;
    text-shadow: 2px 2px 0px #1a0c12 !important;
    font-size: 1.8rem !important;
}}
@media (max-width: 768px) {{
    div[style*='padding: 25px'] {{
        padding: 15px !important;
    }}
    h1 {{
        font-size: 1.8rem !important;
    }}
}}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 2. BRANDING BANNER: SAKURA REALM OVERLAY
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

# 2. BRANDING BANNER: SAKURA REALM OVERLAY
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
    best_display = f"⭐ {st.session_state.gg_best_score} attempts" if st.session_state.gg_best_score else "No wins recorded"
    st.markdown(f"**Personal Best Record:**\n`{best_display}`")

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
            
    # Line 207 has EXACTLY 4 spaces at the front
    if "gg_feedback" in st.session_state:
        # These lines below MUST have EXACTLY 8 spaces (or 2 tabs) at the front
        if st.session_state.gg_feedback_type == "success": st.success(st.session_state.gg_feedback)
        elif st.session_state.gg_feedback_type == "warning": st.warning(st.session_state.gg_feedback)
        elif st.session_state.gg_feedback_type == "error": st.error(st.session_state.gg_feedback)
        else: st.info(st.session_state.gg_feedback)

else:
    if "gg_feedback" in st.session_state and "changed mid-game" in st.session_state.gg_feedback:
        st.info(st.session_state.gg_feedback)
    else:
        idle_html = (
            "<div style='text-align: center; padding: 40px 20px; background-color: rgba(45, 20, 32, 0.85); backdrop-filter: blur(10px); border: 4px dashed #ff66aa; box-shadow: 6px 6px 0px #1a0c12;'>"
            "<p style='font-size: 1.3rem; color: #ff66aa; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>STATUS // PLATFORM IDLE</p>"
            "<p style='font-size: 0.95rem; color: #ffffff; font-weight: bold; margin-top: 10px;'>Initialize the left matrix panel to deploy your first gameplay module round!</p>"
            "</div>"
        )
        st.markdown(idle_html, unsafe_allow_html=True)

