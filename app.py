import streamlit as st
import random

# 1. APPLICATION ENVIRONMENT FRAMEWORK
st.set_page_config(
    page_title="LordDarkness Arcade Core", 
    page_icon="🥊", 
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

# ==========================================
# 3D CEL-SHADED GAMING ENGINE (CSS Injection)
# ==========================================
st.markdown(
    """
    <style>
    /* Keyframe 1: Pop compression scale transition when items render */
    @keyframes entryPop {
        0% { transform: scale(0.96); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    /* Global application structure override */
    .stApp {
        background: linear-gradient(180deg, #160c13 0%, #0d060b 100%) !important;
        animation: entryPop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) once !important;
    }
    
    /* Re-engineer standard flat buttons into chunky, tactile 3D action tiles */
    div.stButton > button:first-child {
        background: #ff66aa !important;
        color: #110b11 !important;
        border: 3px solid #110b11 !important;
        font-weight: 900 !important;
        font-size: 1.1rem !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        border-radius: 8px !important;
        box-shadow: 0px 6px 0px #991155 !important; /* Thick geometric 3D shadow */
        transition: all 0.1s ease-in-out !important;
        margin-bottom: 6px !important;
    }
    
    /* CRITICAL GAMING MECHANIC: The physical click compression bounce down */
    div.stButton > button:first-child:active {
        transform: translateY(4px) !important;
        box-shadow: 0px 2px 0px #991155 !important;
    }
    div.stButton > button:first-child:hover {
        background: #ff88bb !important;
        color: #110b11 !important;
        border-color: #110b11 !important;
    }
    
    /* Format entry panels into heavy console modules */
    div[data-testid="stForm"] {
        background-color: #2d1622 !important;
        border: 4px solid #110b11 !important;
        border-radius: 12px !important;
        box-shadow: 8px 8px 0px #110b11 !important; /* Sharp pop-art dropshadow */
        padding: 25px !important;
    }
    
    /* Force bold text highlighting on metrics indicators */
    div[data-testid="stMetricValue"] {
        font-weight: 900 !important;
        color: #ff66aa !important;
        text-shadow: 2px 2px 0px #110b11 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HEAVY IMPACT COMIC HEADER BRAND BANNER
st.markdown(
    """
    <div style="background-color: #2d1622; padding: 25px; border-radius: 12px; text-align: center; border: 4px solid #110b11; box-shadow: 8px 8px 0px #110b11; margin-bottom: 35px;">
        <h1 style="color: #ff66aa; margin: 0; font-family: 'Courier New', monospace; font-size: 2.5rem; letter-spacing: 2px; font-weight: 900; text-shadow: 3px 3px 0px #110b11;">
            🌸 桜 GUESS CORE v2 🌸
        </h1>
        <p style="color: #ffffff; margin: 8px 0 0 0; font-size: 1rem; font-family: 'Courier New', monospace; font-weight: bold; letter-spacing: 1px;">
            [ ARCADE ENGINE // ENGINE CREDITS: LORDDARKNESS393 ]
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 2. CONTROL PANEL CONFIGURATION
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

# 3. INTERFACE PROCESSOR ROUTINE
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
            st.session_state.gg_feedback = f"💀 MODULE CRASH! Out of lives. Core signature code was: {secret}."
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
        st.markdown(
            """
            <div style="text-align: center; padding: 40px 20px; background-color: #2d1622; border-radius: 12px; border: 4px dashed #ff66aa; box-shadow: 6px 6px 0px #110b11;">
                <p style="font-size: 1.3rem; color: #ff66aa; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #110b11;">STATUS // SYSTEM IDLE</p>
                <p style="font-size: 0.95rem; color: #ffffff; font-weight: bold; margin-top: 10px;">Deploy the left operational module console to clear the terminal grids!</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

# STUDIO PRODUCTION INSIGNIA
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; padding: 10px; margin-top: 30px;">
        <p style="color: #614653; font-family: 'Courier New', monospace; font-size: 0.85rem; margin: 0; font-weight: bold;">
            © 2026 DARKNESS GAMING LABS | ALL RIGHTS RESERVED
        </p>
