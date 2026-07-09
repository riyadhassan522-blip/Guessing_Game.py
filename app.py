import streamlit as st
import random

# 1. PAGE SETUP
st.set_page_config(page_title="Ultimate Guessing Game", page_icon="🎮", layout="centered")

st.markdown(
    """
    <div style="background-color: #1e1e2f; padding: 20px; border-radius: 12px; text-align: center; border: 2px solid #4a4a6a; margin-bottom: 25px;">
        <h1 style="color: #00ffcc; margin: 0; font-family: 'Courier New', monospace; font-size: 2rem; letter-spacing: 2px;">⚡ ULTIMATE GUESSING GAME ⚡</h1>
        <p style="color: #a0a0c0; margin: 5px 0 0 0; font-size: 0.9rem;">Powered directly by your custom python code engine!</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 2. MATCHING YOUR EXACT DIFFICULTY STATS
if "games_played" not in st.session_state:
    st.session_state.games_played = 0
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.total_attempts = 0
    st.session_state.best_score = None
    st.session_state.game_active = False
    st.session_state.current_difficulty = None

with st.sidebar:
    st.markdown("### ⚙️ GAME SETTINGS")
    difficulty = st.selectbox(
        "Select Difficulty Rank:",
        ["1. Novice (1-20, 8 lives)", "2. Easy (1-50, 10 lives)", "3. Medium (1-100, 7 lives)", "4. Hard (1-200, 5 lives)", "5. Expert (1-500, 3 lives)"]
    )
    
    # Reading your exact numbers from your original choice logic
    if "1." in difficulty: max_lives, max_range = 8, 20
    elif "2." in difficulty: max_lives, max_range = 10, 50
    elif "3." in difficulty: max_lives, max_range = 7, 100
    elif "4." in difficulty: max_lives, max_range = 5, 200
    else: max_lives, max_range = 3, 500

    # SAFETY CHECK: If difficulty is changed mid-game, safely deactivate the round to prevent errors
    if st.session_state.game_active and st.session_state.current_difficulty != difficulty:
        st.session_state.game_active = False
        st.session_state.feedback = "⚠️ Difficulty changed mid-game! Press the button below to initialize the new modules."
        st.session_state.feedback_type = "info"

    if st.button("🚀 START / RESET GAME", use_container_width=True, type="primary"):
        st.session_state.secret_number = random.randint(1, max_range)
        st.session_state.lives_left = max_lives
        st.session_state.round_attempts = 0
        st.session_state.game_active = True
        st.session_state.current_difficulty = difficulty
        st.session_state.feedback = "🎯 Core system initialized! Enter your first guess below."
        st.session_state.feedback_type = "info"

    st.markdown("---")
    st.markdown("### 📊 DASHBOARD STATS")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Played", value=st.session_state.games_played)
        st.metric(label="Wins 🏆", value=st.session_state.wins)
    with col2:
        st.metric(label="Total Guesses", value=st.session_state.total_attempts)
        st.metric(label="Losses 💀", value=st.session_state.losses)
        
    st.markdown("---")
    best_display = f"⭐ {st.session_state.best_score} attempts" if st.session_state.best_score else "No wins yet"
    st.markdown(f"**Personal Best Record:**\n`{best_display}`")

# 3. INTERFACE PROCESSOR USING YOUR LOGIC RULES
if st.session_state.game_active:
    with st.container(border=True):
        st.markdown(f"##### ❤️ Vital Signs: **{st.session_state.lives_left} / {max_lives} Lives Remaining**")
        
        # FIXED: Safety clamp function locks values securely between 0.0 and 1.0 to prevent server crashes
        raw_percentage = float(st.session_state.lives_left / max_lives)
        health_percentage = max(0.0, min(1.0, raw_percentage))
        st.progress(health_percentage)

    st.markdown(" ")

    with st.form(key="guess_form", clear_on_submit=True):
        guess = st.number_input(f"Target Scan Range [1 to {max_range}]:", min_value=1, max_value=max_range, step=1, value=None, placeholder="Tap here to input your guess...")
        submit_guess = st.form_submit_button("💥 SUBMIT GUESS ANALYSIS", use_container_width=True)

    if submit_guess and guess is not None:
        st.session_state.round_attempts += 1
        st.session_state.total_attempts += 1
        
        warm_threshold = max(3, max_range // 15)
        secret = st.session_state.secret_number

        if guess < secret:
            st.session_state.lives_left -= 1
            msg = f"📉 {guess} is Too Low!"
            if secret - guess <= warm_threshold:
                msg += " 👉 But you are getting warm!!"
            st.session_state.feedback = msg
            st.session_state.feedback_type = "warning"
            
        elif guess > secret:
            st.session_state.lives_left -= 1
            msg = f"📈 {guess} is Too High!"
            if guess - secret <= warm_threshold:
                msg += " 👉 But you are getting warm!!"
            st.session_state.feedback = msg
            st.session_state.feedback_type = "warning"
            
        else:
            st.session_state.feedback = f"🎉 EXCELLENT! You cracked the system code in {st.session_state.round_attempts} attempts!"
            st.session_state.feedback_type = "success"
            st.session_state.wins += 1
            st.session_state.games_played += 1
            if st.session_state.best_score is None or st.session_state.round_attempts < st.session_state.best_score:
                st.session_state.best_score = st.session_state.round_attempts
                st.toast("🔥 NEW GLOBAL RECORD SET! 🔥")
            st.session_state.game_active = False

        if st.session_state.lives_left <= 0 and st.session_state.game_active:
            st.session_state.feedback = f"💀 SYSTEM CRASH! You ran out of lives. Critical signature number was: {secret}."
            st.session_state.feedback_type = "error"
            st.session_state.losses += 1
            st.session_state.games_played += 1
            st.session_state.game_active = False

    if "feedback" in st.session_state:
        if st.session_state.feedback_type == "success": st.success(st.session_state.feedback)
        elif st.session_state.feedback_type == "warning": st.warning(st.session_state.feedback)
        elif st.session_state.feedback_type == "error": st.error(st.session_state.feedback)
        else: st.info(st.session_state.feedback)
else:
    if "feedback" in st.session_state and "Difficulty changed" in st.session_state.feedback:
        st.info(st.session_state.feedback)
    else:
        st.markdown(
            """
            <div style="text-align: center; padding: 40px 20px; background-color: #1a1a24; border-radius: 8px; border: 1px dashed #444;">
                <p style="font-size: 1.2rem; color: #a0a0b0; margin-bottom: 20px;">🎮 System Idle. Engine ready for configuration.</p>
                <p style="font-size: 0.9rem; color: #707080;">Open the <b>left sidebar panel</b> to choose your difficulty target range and launch your game module!</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
