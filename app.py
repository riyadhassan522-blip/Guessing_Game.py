import streamlit as st
import random

# 1. VISUAL LAYER HEADLESS INITIALIZATION
st.set_page_config(
    page_title="LordDarkness Sakura Engine", 
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

# ==========================================
# ADVANCED JAPANESE VISUAL ENGINE (Injected CSS)
# ==========================================
st.markdown(
    """
    <style>
    /* Keyframe 1: Dynamic flowing Sakura gradient backdrop */
    @keyframes blossomFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    /* Keyframe 2: Gentle continuous floating pulse for headers */
    @keyframes floatingHeader {
        0% { transform: translateY(0px); filter: drop-shadow(0 2px 8px rgba(255,183,197,0.3)); }
        50% { transform: translateY(-6px); filter: drop-shadow(0 12px 20px rgba(255,183,197,0.6)); }
        100% { transform: translateY(0px); filter: drop-shadow(0 2px 8px rgba(255,183,197,0.3)); }
    }
    
    /* Inject moving backdrop into the application skin */
    .stApp {
        background: linear-gradient(-45deg, #180d12, #29121c, #1f0f15, #140b0f) !important;
        background-size: 400% 400% !important;
        animation: blossomFlow 10s ease infinite !important;
    }
    
    /* Re-engineer standard Streamlit buttons into tactile gaming tiles */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #ffb7c5 0%, #ff85a7 100%) !important;
        color: #2b111c !important;
        border: 2px solid #ffb7c5 !important;
        font-weight: 900 !important;
        letter-spacing: 1px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(255, 183, 197, 0.2) !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.02) !important;
        box-shadow: 0 0 25px rgba(255, 133, 167, 0.6) !important;
        color: #ffffff !important;
        border-color: #ff85a7 !important;
    }
    
    /* Style form input blocks with neon borders */
    div[data-testid="stForm"] {
        background-color: rgba(37, 22, 31, 0.7) !important;
        border: 2px solid #ffb7c5 !important;
        border-radius: 16px !important;
        box-shadow: 0 0 15px rgba(255, 183, 197, 0.1) !important;
    }
    
    .sakura-header-container {
        animation: floatingHeader 4s ease-in-out infinite !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# PREMIUM STRUCTURAL BRAND BANNER
st.markdown(
    """
    <div class="sakura-header-container" style="background-color: #25161f; padding: 25px; border-radius: 16px; text-align: center; border: 2px solid #ffb7c5; margin-bottom: 25px;">
        <h1 style="color: #ffb7c5; margin: 0; font-family: 'Courier New', monospace; font-size: 2.3rem; letter-spacing: 3px; font-weight: 800;">
            🌸 桜 GUESSING CORE 🌸
        </h1>
        <p style="color: #d1b2bf; margin: 8px 0 0 0; font-size: 0.95rem; font-family: 'Courier New', monospace; letter-spacing: 1px;">
            SYSTEM PROTOCOLS RUNNING // DESIGNED BY LORDDARKNESS393
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
    
    # Read core attributes directly corresponding to your original logic code structure
    if "1." in difficulty: max_lives, max_range = 8, 20
    elif "2." in difficulty: max_lives, max_range = 10, 50
    elif "3." in difficulty: max_lives, max_range = 7, 100
    elif "4." in difficulty: max_lives, max_range = 5, 200
    else: max_lives, max_range = 3, 500

    # Safety trap monitors choices mid-game to prevent mathematical breaks
    if st.session_state.gg_active and st.session_state.gg_current_difficulty != difficulty:
        st.session_state.gg_active = False
        st.session_state.gg_feedback = "⚠️ Difficulty boundary changed mid-game! Re-initialize system modules."
        st.session_state.gg_feedback_type = "info"

    if st.button("🚀 INITIALIZE MATRIX ROUND", use_container_width=True, type="primary"):
        st.session_state.gg_secret_number = random.randint(1, max_range)
        st.session_state.gg_lives_left = max_lives
        st.session_state.gg_round_attempts = 0
        st.session_state.gg_active = True
        st.session_state.gg_current_difficulty = difficulty
        st.session_state.gg_feedback = "🎯 Core system online. Input your scan guess below."
        st.session_state.gg_feedback_type = "info"

    # PERSISTENT SCOREBOARD DASHBOARD
    st.markdown("---")
    st.markdown("### 📊 DASHBOARD STATS")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Played Matches", value=st.session_state.gg_played)
        st.metric(label="Wins 🏆", value=st.session_state.gg_wins)
    with col2:
        st.metric(label="Total Guesses", value=st.session_state.gg_total_guesses)
        st.metric(label="Losses 💀", value=st.session_state.gg_losses)
        
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
        submit_guess = st.form_submit_button("💥 RUN MATRIX ANALYZER", use_container_width=True)

    if submit_guess and guess is not None:
        st.session_state.gg_round_attempts += 1
        st.session_state.gg_total_guesses += 1
        
        warm_threshold = max(3, max_range // 15)
        secret = st.session_state.gg_secret_number

        if guess < secret:
            st.session_state.gg_lives_left -= 1
            msg = f"📉 {guess} is Too Low!"
            if secret - guess <= warm_threshold: msg += " 👉 But you are getting warm!!"
            st.session_state.gg_feedback = msg
            st.session_state.gg_feedback_type = "warning"
        elif guess > secret:
            st.session_state.gg_lives_left -= 1
            msg = f"📈 {guess} is Too High!"
            if guess - secret <= warm_threshold: msg += " 👉 But you are getting warm!!"
            st.session_state.gg_feedback = msg
            st.session_state.gg_feedback_type = "warning"
        else:
            st.session_state.gg_feedback = f"🎉 SYSTEM CODE CRACKED! You secured victory in {st.session_state.gg_round_attempts} attempts!"
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
        st.markdown(
            """
            <div style="text-align: center; padding: 40px 20px; background-color: rgba(37, 22, 31, 0.5); border-radius: 12px; border: 1px dashed #ffb7c5;">
                <p style="font-size: 1.2rem; color: #ffb7c5; font-weight: bold;">🌸 Game Module Offline</p>
                <p style="font-size: 0.9rem; color: #a09098;">Open the left operational console to pick your difficulty matrix and launch the module core!</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

# STUDIO PRODUCTION INSIGNIA
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; padding: 10px; margin-top: 30px;">
        <p style="color: #614653; font-family: 'Courier New', monospace; font-size: 0.85rem; margin: 0;">
            © 2026 DARKNESS GAMING LABS | ALL RIGHTS RESERVED
        </p>
