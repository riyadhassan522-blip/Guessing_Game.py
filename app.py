import streamlit as st
import random

# 1. APPLICATION ENVIRONMENT FRAMEWORK
st.set_page_config(
    page_title="Lord's Gaming Hub", 
    page_icon="🎮", 
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
# ⚙️ GITHUB FOLDER SOURCE: PULLS FROM YOUR CUSTOM ASSET DIRECTORY
# =========================================================================
WALLPAPER_URL = "https://githubusercontent.com"

# ==========================================
# 3D CEL-SHADED GAMING ENGINE (Safe Flat String CSS Engine)
# ==========================================
css_style = (
    "<style>\n"
    "@keyframes entryPop {\n"
    "    0% { transform: scale(0.96); opacity: 0; }\n"
    "    100% { transform: scale(1); opacity: 1; }\n"
    "}\n"
    ".stApp {\n"
    "    background-image: linear-gradient(rgba(13, 6, 11, 0.75), rgba(13, 6, 11, 0.85)), url('" + WALLPAPER_URL + "') !important;\n"
    "    background-size: cover !important;\n"
    "    background-position: center center !important;\n"
    "    background-attachment: fixed !important;\n"
    "    animation: entryPop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) once !important;\n"
    "}\n"
    "div.stButton > button:first-child {\n"
    "    background: #ff66aa !important;\n"
    "    color: #110b11 !important;\n"
    "    border: 3px solid #110b11 !important;\n"
    "    font-weight: 900 !important;\n"
    "    font-size: 1.1rem !important;\n"
    "    text-transform: uppercase !important;\n"
    "    letter-spacing: 2px !important;\n"
    "    border-radius: 8px !important;\n"
    "    box-shadow: 0px 6px 0px #991155 !important;\n"
    "    transition: all 0.1s ease-in-out !important;\n"
    "    margin-bottom: 6px !important;\n"
    "    width: 100% !important;\n"
    "}\n"
    "div.stButton > button:first-child:active {\n"
    "    transform: translateY(4px) !important;\n"
    "    box-shadow: 0px 2px 0px #991155 !important;\n"
    "}\n"
    "div.stButton > button:first-child:hover {\n"
    "    background: #ff88bb !important;\n"
    "    color: #110b11 !important;\n"
    "    border-color: #110b11 !important;\n"
    "}\n"
    "div[data-testid='stForm'] {\n"
    "    background-color: rgba(45, 22, 34, 0.85) !important;\n"
    "    backdrop-filter: blur(8px) !important;\n"
    "    border: 4px solid #110b11 !important;\n"
    "    border-radius: 12px !important;\n"
    "    box-shadow: 8px 8px 0px #110b11 !important;\n"
    "    padding: 20px !important;\n"
    "    max-width: 100% !important;\n"
    "}\n"
    "div[data-testid='stMetricValue'] {\n"
    "    font-weight: 900 !important;\n"
    "    color: #ff66aa !important;\n"
    "    text-shadow: 2px 2px 0px #110b11 !important;\n"
    "    font-size: 1.8rem !important;\n"
    "}\n"
    "@media (max-width: 768px) {\n"
    "    div[style*='padding: 25px'] {\n"
    "        padding: 15px !important;\n"
    "    }\n"
    "    h1 {\n"
    "        font-size: 1.8rem !important;\n"
    "    }\n"
    "}\n"
    "</style>"
)
st.markdown(css_style, unsafe_allow_html=True)

# 2. BRANDING BANNER
banner_html = (
    "<div style='background-color: rgba(45, 22, 34, 0.85); backdrop-filter: blur(8px); padding: 25px; border-radius: 12px; text-align: center; border: 4px solid #110b11; box-shadow: 8px 8px 0px #110b11; margin-bottom: 35px;'>\n"
    "    <h1 style='color: #ff66aa; margin: 0; font-family: \"Courier New\", monospace; font-size: 2.5rem; letter-spacing: 2px; font-weight: 900; text-shadow: 3px 3px 0px #110b11;'>\n"
    "        🌸 LORD'S GAMING HUB 🌸\n"
    "    </h1>\n"
    "    <p style='color: #ffffff; margin: 8px 0 0 0; font-size: 1rem; font-family: \"Courier New\", monospace; font-weight: bold; letter-spacing: 1px;'>\n"
    "        [ ARCADE STATION ENGINE // ENG CREDITS: LORDDARKNESS393 ]\n"
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
            if secret - guess <= warm_threshold: msg += " 👉 Getting warm!!"
            st.session_state.gg_feedback = msg
            st.session_state.gg_feedback_type = "warning"
        elif guess > secret:
            st.session_state.gg_lives_left -= 1
            msg = f"📈 {guess} is Too High!"
            if guess - secret <= warm_threshold: msg += " 👉 Getting warm!!"
            st.session_state.gg_feedback = msg
            st.session_state.gg_feedback_type = "warning"
        else:
            st.session_state.gg_feedback = f"🎉 MAINFRAME CRACKED! You secured system victory in {st.session_state.gg_round_attempts} attempts!"
            st.session_state.gg_feedback_type = "success"
            st.session_state.gg_wins += 1
            st.session_state.gg_played += 1
            if st.session_state.gg_best_score is None or st.session_state.gg_round_attempts < st.session_state.gg_best_score:
                st.session_state.gg_best_score = st.session_state.gg_round_attempts
                st.toast("🌸 NEW GLOBAL RECORD UNLOCKED! 🌸")
            st.session_state.gg_active = False

        if st.session_state.gg_lives_left <= 0 and st.session_state.gg_active:
            st.session_state.gg_feedback = f"💀 MODULE CRASH! Out of lives. Critical signature code was: {secret}."
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
            "<div style='text-align: center; padding: 40px 20px; background-color: rgba(45, 22, 34, 0.85); backdrop-filter: blur(8px); border: 4px dashed #ff66aa; box-shadow: 6px 6px 0px #110b11;'>"
            "<p style='font-size: 1.3rem; color: #ff66aa; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #110b11;'>STATUS // SYSTEM IDLE</p>"
            "<p style='font-size: 0.95rem; color: #ffffff; font-weight: bold; margin-top: 10px;'>Deploy the left operational module console to clear the terminal grids!</p>"
            "</div>"
        )
        st.markdown(idle_html, unsafe_allow_html=True)
