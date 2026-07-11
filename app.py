import streamlit as st
import random
import base64
import time

# 1. SETUP ENVIRONMENT VIEWPORT
st.set_page_config(
    page_title="Lord's Arcade Realm", 
    page_icon="🌸", 
    layout="centered"
)

# Initialize Absolute Platform Core State Variables
if "active_channel" not in st.session_state: st.session_state.active_channel = "LOBBY"
if "gg_played" not in st.session_state: st.session_state.gg_played = 0
if "gg_wins" not in st.session_state: st.session_state.gg_wins = 0
if "gg_losses" not in st.session_state: st.session_state.gg_losses = 0
if "gg_total_guesses" not in st.session_state: st.session_state.gg_total_guesses = 0
if "gg_best_score" not in st.session_state: st.session_state.gg_best_score = None
if "gg_active" not in st.session_state: st.session_state.gg_active = False
if "gg_current_difficulty" not in st.session_state: st.session_state.gg_current_difficulty = None
if "ttt_played" not in st.session_state: st.session_state.ttt_played = 0
if "ttt_wins" not in st.session_state: st.session_state.ttt_wins = 0
if "ttt_losses" not in st.session_state: st.session_state.ttt_losses = 0
if "ttt_ties" not in st.session_state: st.session_state.ttt_ties = 0
if "ttt_board" not in st.session_state: st.session_state.ttt_board = [" " for _ in range(9)]
if "ttt_score_locked" not in st.session_state: st.session_state.ttt_score_locked = False

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file: return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError: return ""

bg_base64 = get_base64_image("themes/bg.jpg")

def trigger_arcade_synth():
    st.markdown("""<audio autoplay style="display:none;"><source src="data:audio/wav;base64,UklGRigAAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQQAAAAAf39/fw==" type="audio/wav"></audio>""", unsafe_allow_html=True)

# =========================================================================
# THE ULTIMATE UNIFIED GLASS INTERFACE STYLING CONFIGURATION
# =========================================================================
css_style = f"""
<style>
.stApp, [data-testid='stAppViewContainer'], .stAppHeader, [data-testid='stHeader'] {{
    background-image: linear-gradient(rgba(26, 12, 18, 0.45), rgba(26, 12, 18, 0.65)), url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important; background-position: center center !important; background-attachment: fixed !important;
}}
html, body, p, span, label, div, h1, h2, h3, button, input {{ font-family: 'Courier New', Courier, monospace !important; font-weight: bold !important; }}

/* PREVENTS TOP CUTOFF BY DROPPING INTERFACE DOWN COMFORTABLY */
.main .block-container {{ padding-top: 50px !important; }}

/* PREMIUM TRANSLUCENT GLOWING GLASS HOUSING WINDOW PANELS */
div[data-testid='stForm'], div[data-testid='stVerticalBlock'] > div[style*="border"], .stMainBlockContainer > div {{
    background-color: rgba(37, 22, 31, 0.45) !important; backdrop-filter: blur(16px) !important; -webkit-backdrop-filter: blur(16px) !important;
    border: 2px solid rgba(255, 102, 170, 0.4) !important; border-radius: 24px !important; padding: 30px !important;
    box-shadow: 0px 8px 32px rgba(255, 102, 170, 0.15) !important; margin-bottom: 25px !important;
}}
.stMainBlockContainer {{ background: transparent !important; padding: 0 !important; max-width: 100% !important; }}

/* RETRO ARCADE 3D COMMAND NAVIGATION ACTION BUTTONS */
div.stButton > button {{
    background: #ff66aa !important; color: #1a0c12 !important; border: 3px solid #1a0c12 !important; font-weight: 900 !important;
    font-size: 1.1rem !important; text-transform: uppercase !important; letter-spacing: 2px !important; border-radius: 8px !important;
    box-shadow: 0px 6px 0px #992255 !important; transition: all 0.1s ease-in-out !important; width: 100% !important; height: 48px !important;
}}
div.stButton > button:active {{ transform: translateY(4px) !important; box-shadow: 0px 2px 0px #992255 !important; }}
div[data-testid="stTextInput"] [data-baseweb="input"] {{ background-color: rgba(37, 22, 31, 0.90) !important; border: 2px solid rgba(255, 102, 170, 0.5) !important; border-radius: 8px !important; }}
div[data-testid="stTextInput"] input {{ background-color: transparent !important; color: #ff66aa !important; font-size: 1.1rem !important; }}
div[data-testid="stTextInput"] [data-baseweb="input"] + div {{ display: none !important; }}
div[data-testid='stMetricValue'] {{ font-weight: 900 !important; color: #ff66aa !important; text-shadow: 2px 2px 0px #1a0c12 !important; font-size: 1.5rem !important; }}

/* 🎯 HIGH-DENSITY HIGH-COMPACT TIC-TAC-TOE MATRIX CELLS */
.ttt-container {{ display: flex; justify-content: center; margin: 15px 0; }}
.ttt-table {{ border-collapse: collapse; border: 3px solid rgba(255, 102, 170, 0.6) !important; border-radius: 12px !important; overflow: hidden; }}
.ttt-cell {{ width: 66px !important; height: 68px !important; text-align: center; border: 2px solid rgba(255, 102, 170, 0.3) !important; padding: 0 !important; margin: 0 !important; }}
.ttt-btn {{
    width: 100% !important; height: 100% !important; background-color: rgba(37, 22, 31, 0.60) !important; backdrop-filter: blur(10px) !important;
    color: #ff66aa !important; border: none !important; font-size: 1.6rem !important; font-weight: 900 !important; cursor: pointer; transition: all 0.1s;
}}
.ttt-btn:hover:not(:disabled) {{ background-color: rgba(255, 102, 170, 0.15) !important; }}

/* 🚨 PERMANENT SIDEBAR ABOLISHMENT: Safely drops all native drawers and header components */
[data-testid="stSidebar"], [data-testid="collapsedControl"], [data-testid="stHeader"], .stAppHeader, div.stAppViewContainer > div:first-child {{
    display: none !important; visibility: hidden !important; opacity: 0 !important; height: 0px !important; width: 0px !important;
}}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

st.markdown("<div style='background-color: rgba(45, 20, 32, 0.40); backdrop-filter: blur(10px); padding: 25px; border-radius: 16px; text-align: center; border: 1px solid rgba(255, 102, 170, 0.25); box-shadow: 0px 4px 15px rgba(255, 102, 170, 0.1); margin-bottom: 35px;'><h1 style='color: #ff66aa; margin: 0; font-family: \"Courier New\", monospace; font-size: 2.3rem; letter-spacing: 2px; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>🌸 LORD'S ARCADE REALM 🌸</h1></div>", unsafe_allow_html=True)

nav_lobby, nav_game1, nav_game2 = st.columns(3)
with nav_lobby:
    if st.button("🌸 LOBBY HUB", use_container_width=True):
        st.session_state.active_channel = "LOBBY"
        trigger_arcade_synth(); st.rerun()
with nav_game1:
    if st.button("🎯 RADAR GAME", use_container_width=True):
        st.session_state.active_channel = "RADAR"
        trigger_arcade_synth(); st.rerun()
with nav_game2:
    if st.button("❌ MATRIX ARENA", use_container_width=True):
        st.session_state.active_channel = "TIC_TAC_TOE"
        trigger_arcade_synth(); st.rerun()

st.markdown("<hr style='border: none; border-top: 2px dashed rgba(255, 102, 170, 0.25); margin: 15px 0;'>", unsafe_allow_html=True)
# =========================================================================
# SECTOR 1: THE MAIN MENU HOME DASHBOARD HUB
# =========================================================================
if st.session_state.active_channel == "LOBBY":
    st.markdown("### 🕹️ TERMINAL DASHBOARD MAINFRAME")
    st.markdown("Your custom retro arcade layout has been successfully re-aligned to zero-sidebar glass specifications.")
    st.info("💡 INSTRUCTION: Tap any of the pink navigation buttons above to load and swap active game terminals instantly in place!")
    
    st.markdown(" ")
    st.markdown("##### 📊 GLOBAL ARENA SCOREBOARD:")
    col_stat1, col_metric1, col_metric2 = st.columns(3)
    with col_stat1:
        st.markdown(f"<p style='color: #ffffff; font-size: 0.95rem; margin-top: 10px;'>● **RADAR WINS:** <span style='color: #ff66aa;'>{st.session_state.gg_wins} Matches</span></p>", unsafe_allow_html=True)
    with col_metric1:
        st.markdown(f"<p style='color: #ffffff; font-size: 0.95rem; margin-top: 10px;'>● **ARENA VICTORIES:** <span style='color: #ff66aa;'>{st.session_state.ttt_wins} Wins</span></p>", unsafe_allow_html=True)
    with col_metric2:
        st.markdown(f"<p style='color: #ffffff; font-size: 0.95rem; margin-top: 10px;'>● **BOT CRASHES:** <span style='color: #ff66aa;'>{st.session_state.ttt_losses} Defeats</span></p>", unsafe_allow_html=True)

# =========================================================================
# SECTOR 2: THE ISOLATED RADAR NUMBER SCANNER MODULE
# =========================================================================
elif st.session_state.active_channel == "RADAR":
    st.markdown("### 🎯 RADAR NUMBER SCANNER")
    
    difficulty = st.selectbox("Select Rank Boundary Sequence:", ["1. Novice (1-20, 8 lives)", "2. Easy (1-50, 10 lives)", "3. Medium (1-100, 7 lives)", "4. Hard (1-200, 5 lives)", "5. Expert (1-500, 3 lives)"])
    if "1." in difficulty: max_lives, max_range = 8, 20
    elif "2." in difficulty: max_lives, max_range = 10, 50
    elif "3." in difficulty: max_lives, max_range = 7, 100
    elif "4." in difficulty: max_lives, max_range = 5, 200
    else: max_lives, max_range = 3, 500

    col_btn, col_blank = st.columns(2)
    with col_btn:
        if st.button("🚀 DEPLOY CORE MATCH PHASE", use_container_width=True, type="primary"):
            trigger_arcade_synth()
            st.session_state.gg_secret_number = random.randint(1, max_range)
            st.session_state.gg_lives_left = max_lives
            st.session_state.gg_round_attempts = 0
            st.session_state.gg_active = True
            st.session_state.gg_current_difficulty = difficulty
            st.session_state.gg_feedback = "🎯 SYSTEM ENGINE LOADED. DISPATCH YOUR FIRST GUESS ANALYSIS."
            st.session_state.gg_feedback_type = "info"

    st.markdown(" ")
    if st.session_state.gg_active:
        st.markdown(f"##### 🌸 Core Integrity: **{st.session_state.gg_lives_left} / {max_lives} Lives Remaining**")
        st.progress(float(min(1.0, max(0, st.session_state.gg_lives_left) / max_lives)))
        
        with st.form(key="guess_form", clear_on_submit=True):
            guess_input = st.text_input(f"Target Scan Range [1 to {max_range}]:", value="", placeholder="Type your number analysis here and click submit...")
            submit_guess = st.form_submit_button("💥 SUBMIT SCAN RADAR", use_container_width=True)

        if submit_guess and guess_input.strip().isdigit():
            guess = int(guess_input.strip())
            trigger_arcade_synth()
            st.session_state.gg_round_attempts += 1
            st.session_state.gg_total_guesses += 1
            warm_threshold = max(3, max_range // 15)
            secret = st.session_state.gg_secret_number

            if guess < secret:
                st.session_state.gg_lives_left -= 1
                msg = f"📉 {guess} is Too Low!"
                if secret - guess <= warm_threshold: msg += " 👉 Radar signature warm!!"
                st.session_state.gg_feedback, st.session_state.gg_feedback_type = msg, "warning"
            elif guess > secret:
                st.session_state.gg_lives_left -= 1
                msg = f"📈 {guess} is Too High!"
                if guess - secret <= warm_threshold: msg += " 👉 Radar signature warm!!"
                st.session_state.gg_feedback, st.session_state.gg_feedback_type = msg, "warning"
            else:
                st.session_state.gg_feedback = f"🎉 ACCESS SECURED! Encryption cracked in {st.session_state.gg_round_attempts} attempts!"
                st.session_state.gg_feedback_type = "success"
                st.session_state.gg_wins += 1; st.session_state.gg_played += 1
                if st.session_state.gg_best_score is None or st.session_state.gg_round_attempts < st.session_state.gg_best_score:
                    st.session_state.gg_best_score = st.session_state.gg_round_attempts
                st.session_state.gg_active = False

            if st.session_state.gg_lives_left <= 0 and st.session_state.gg_active:
                st.session_state.gg_feedback = f"💀 SYSTEM CRASHED! Core signature was: {secret}."
                st.session_state.gg_feedback_type = "error"
                st.session_state.gg_losses += 1; st.session_state.gg_played += 1
                st.session_state.gg_active = False
            st.rerun()

    if "gg_feedback" in st.session_state and st.session_state.gg_active:
        if st.session_state.gg_feedback_type == "success": st.success(st.session_state.gg_feedback)
        elif st.session_state.gg_feedback_type == "warning": st.warning(st.session_state.gg_feedback)
        elif st.session_state.gg_feedback_type == "error": st.error(st.session_state.gg_feedback)
        else: st.info(st.session_state.gg_feedback)
    elif not st.session_state.gg_active and "gg_feedback" in st.session_state:
        if st.session_state.gg_feedback_type == "success": st.success(st.session_state.gg_feedback)
        else: st.error(st.session_state.gg_feedback)
# =========================================================================
# SECTOR 3: THE COMPACT HIGH-DENSITY TIC-TAC-TOE MATRIX ARENA
# =========================================================================
elif st.session_state.active_channel == "TIC_TAC_TOE":
    st.markdown("### ❌ NEURAL MATRIX ARENA ⭕")
    
    # Process cell hit query parameter payloads directly before rendering
    for r in range(3):
        for c in range(3):
            key = f"ttt_hit_{r}_{c}"
            if key in st.query_params:
                idx = r * 3 + c
                if st.session_state.ttt_board[idx] == " ":
                    st.session_state.ttt_board[idx] = "X"
                    
                    # Core Win Matrix Evaluation (Hardcoded index checks)
                    current_status = None
                    w_lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
                    for vector in w_lines:
                        if st.session_state.ttt_board[vector[0]] == st.session_state.ttt_board[vector[1]] == st.session_state.ttt_board[vector[2]] and st.session_state.ttt_board[vector[0]] != " ":
                            current_status = st.session_state.ttt_board[vector[0]]
                    if " " not in st.session_state.ttt_board and not current_status: 
                        current_status = "TIE"
                    
                    # Bot defensive move tracker calculation loop
                    if not current_status:
                        moved = False
                        for vector in w_lines:
                            tokens = [st.session_state.ttt_board[v] for v in vector]
                            if tokens.count("O") == 2 and tokens.count(" ") == 1:
                                st.session_state.ttt_board[vector[tokens.index(" ")]] = "O"; moved = True; break
                        if not moved:
                            for vector in w_lines:
                                tokens = [st.session_state.ttt_board[v] for v in vector]
                                if tokens.count("X") == 2 and tokens.count(" ") == 1:
                                    st.session_state.ttt_board[vector[tokens.index(" ")]] = "O"; moved = True; break
                        if not moved and st.session_state.ttt_board[4] == " ":
                            st.session_state.ttt_board[4] = "O"; moved = True
                        if not moved:
                            open_nodes = [i for i, cell in enumerate(st.session_state.ttt_board) if cell == " "]
                            if open_nodes: st.session_state.ttt_board[random.choice(open_nodes)] = "O"

    board = st.session_state.ttt_board
    
    # Re-evaluate final match sequences to save scores cleanly
    current_match_status = None
    w_lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for vector in w_lines:
        if board[vector[0]] == board[vector[1]] == board[vector[2]] and board[vector[0]] != " ":
            current_match_status = board[vector[0]]
    if " " not in board and not current_match_status: 
        current_match_status = "TIE"

    if current_match_status and not st.session_state.ttt_score_locked:
        st.session_state.ttt_played += 1
        if current_match_status == "X": st.session_state.ttt_wins += 1
        elif current_match_status == "O": st.session_state.ttt_losses += 1
        elif current_match_status == "TIE": st.session_state.ttt_ties += 1
        st.session_state.ttt_score_locked = True

    # Real-time integrated sidebar-replacement metric scores display
    st.markdown("##### 📊 CURRENT CHANNEL SCOREBOARD:")
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    with stat_col1: st.metric(label="MATCHES PLAYED", value=st.session_state.ttt_played)
    with stat_col2: st.metric(label="VICTORIES 🏆", value=st.session_state.ttt_wins)
    with col_stat1: pass # Avoid namespace overlaps
    with stat_col3: st.metric(label="BOT CRASHES 💀", value=st.session_state.ttt_losses)
    with stat_col4: st.metric(label="GRID TIES 🤝", value=st.session_state.ttt_ties)
    st.markdown("---")

    if current_match_status:
        if current_match_status == "X": st.success("🎉 SECURITY MAINFRAME CRACKED! Player Wins!")
        elif current_match_status == "O": st.error("💀 PROTOCOL ABORTED! The Neural Bot Core claims victory.")
        else: st.warning("🤝 SYSTEM LOCKOUT! It's a draw matrix layout.")
    else: 
        st.markdown("##### 📝 TARGET VECTOR SECTORS:")

    # Compact Mobile Responsive HTML 3x3 Table Element Drawing Engine
    table_html = "<div class='ttt-container'><table class='ttt-table'>"
    for r in range(3):
        table_html += "<tr>"
        for c in range(3):
            idx = r * 3 + c
            cell_val = board[idx]
            disabled_attr = "disabled" if (current_match_status is not None or cell_val != " ") else ""
            table_html += f"<td class='ttt-cell'><button class='ttt-btn' {disabled_attr} onclick=\"const url=new URL(window.location); url.searchParams.set('ttt_hit_{r}_{c}', '1'); window.history.replaceState({{}}, '', url); location.reload();\">{cell_val}</button></td>"
    table_html += "</table></div>"
    st.markdown(table_html, unsafe_allow_html=True)

    if st.button("🔄 RE-INITIALIZE MATRIX", use_container_width=True, type="primary"):
        st.session_state.ttt_board = [" " for _ in range(9)]
        st.session_state.ttt_score_locked = False
        st.query_params.clear(); st.rerun()

# 4. PLATFORM FOOTER SIGN-OFF BRANDING INSIGNIA
footer_html = "<div style='text-align: center; padding: 10px; margin-top: 40px;'><p style='color: #614653; font-family: \"Courier New\", monospace; font-size: 0.85rem; margin: 0; font-weight: bold;'>© 2026 DARKNESS GAMING LABS | ALL RIGHTS RESERVED</p><p style='color: #ff66aa; font-family: \"Courier New\", monospace; font-size: 1rem; margin: 5px 0 0 0; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</p></div>"
st.markdown(footer_html, unsafe_allow_html=True)
