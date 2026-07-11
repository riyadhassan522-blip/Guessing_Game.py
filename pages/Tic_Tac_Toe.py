import streamlit as st
import random
import time
import base64

st.set_page_config(
    page_title="Mainframe Tic-Tac-Toe", 
    page_icon="❌", 
    layout="centered"
)

# Initialize Isolated Tic-Tac-Toe Score Tracking Counters inside persistent memory arrays
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

css_style = f"""
<style>
.stApp, [data-testid='stAppViewContainer'], .stAppHeader, [data-testid='stHeader'] {{
    background-image: linear-gradient(rgba(26, 12, 18, 0.45), rgba(26, 12, 18, 0.65)), url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important; background-position: center center !important; background-attachment: fixed !important;
}}
html, body, p, span, label, div, h1, h2, h3, button {{ font-family: 'Courier New', Courier, monospace !important; font-weight: bold !important; }}
[data-testid='stSidebar'], [data-testid='stSidebarUserContent'] {{ background-color: rgba(30, 15, 23, 0.25) !important; backdrop-filter: blur(16px) !important; border-right: 3px solid #ff66aa !important; }}
[data-testid="stSidebarNav"] ul {{ background-color: rgba(37, 22, 31, 0.70) !important; border-radius: 8px !important; border: 1px solid rgba(255, 102, 170, 0.4) !important; padding: 10px !important; }}
[data-testid="stSidebarNav"] span {{ color: #ffffff !important; }}

.main .block-container {{ padding-top: 110px !important; }}
div[data-testid='stForm'], .stMainBlockContainer {{ background: transparent !important; padding: 25px !important; max-width: 100% !important; }}

/* 🎯 PREMIUM GLASS INTERACTIVE MATRIX SQUARES */
div.stButton > button:first-child {{
    background-color: rgba(37, 22, 31, 0.45) !important; backdrop-filter: blur(12px) !important; -webkit-backdrop-filter: blur(12px) !important;
    color: #ff66aa !important; border: 2px solid rgba(255, 102, 170, 0.4) !important; font-size: 2.1rem !important; font-weight: 900 !important;
    height: 85px !important; border-radius: 12px !important; box-shadow: 0px 4px 20px rgba(255, 102, 170, 0.1) !important;
    transition: all 0.2s ease-in-out !important; width: 100% !important; margin-bottom: 15px !important;
}}
div.stButton > button:first-child:hover {{
    background-color: rgba(255, 102, 170, 0.15) !important; border-color: #ff66aa !important; box-shadow: 0px 0px 15px rgba(255, 102, 170, 0.35) !important; transform: scale(1.02) !important;
}}
div.stButton > button[type="primary"] {{
    background: #ff66aa !important; color: #1a0c12 !important; border: none !important; font-size: 1.1rem !important; height: 45px !important; box-shadow: none !important; border-radius: 8px !important;
}}
div[data-testid='stMetricValue'] {{ font-weight: 900 !important; color: #ff66aa !important; text-shadow: 2px 2px 0px #1a0c12 !important; font-size: 1.6rem !important; }}

div.stAppViewContainer > div:first-child, [data-testid="collapsedControl"], [data-testid="stHeader"], .stAppHeader {{
    display: none !important; visibility: hidden !important; opacity: 0 !important; height: 0px !important; width: 0px !important;
}}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

st.markdown("<div style='background-color: rgba(45, 20, 32, 0.40); backdrop-filter: blur(10px); padding: 25px; border-radius: 12px; text-align: center; border: 1px solid rgba(255, 102, 170, 0.25); box-shadow: 0px 4px 15px rgba(255, 102, 170, 0.1); margin-bottom: 35px;'><h1 style='color: #ff66aa; margin: 0; font-family: \"Courier New\", monospace; font-size: 2.1rem; letter-spacing: 2px; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>❌ NEURAL MATRIX GRID ⭕</h1></div>", unsafe_allow_html=True)
# =========================================================================
# SYSTEM GRID COORDINATE DICTIONARY MAPS
# =========================================================================
v1 = [0, 1, 2]
v2 = [3, 4, 5]
v3 = [6, 7, 8]
v4 = [0, 3, 6]
v5 = [1, 4, 7]
v6 = [2, 5, 8]
v7 = [0, 4, 8]
v8 = [2, 4, 6]

def evaluate_game_state(b):
    win_lines = [v1, v2, v3, v4, v5, v6, v7, v8]
    for vector in win_lines:
        if b[vector[0]] == b[vector[1]] == b[vector[2]] and b[vector[0]] != " ":
            return b[vector[0]]
    if " " not in b:
        return "TIE"
    return None

def calculate_bot_vector(b):
    win_lines = [v1, v2, v3, v4, v5, v6, v7, v8]
    
    # 1. Immediate Win Checking
    for vector in win_lines:
        tokens = [b[vector[0]], b[vector[1]], b[vector[2]]]
        if tokens.count("O") == 2 and tokens.count(" ") == 1:
            return vector[tokens.index(" ")]
            
    # 2. Deflection block checking
    for vector in win_lines:
        tokens = [b[vector[0]], b[vector[1]], b[vector[2]]]
        if tokens.count("X") == 2 and tokens.count(" ") == 1:
            return vector[tokens.index(" ")]
            
    # 3. Center square priority
    if b[4] == " ": 
        return 4
        
    # 4. Perimeter fallback random checking
    open_nodes = [i for i, cell in enumerate(b) if cell == " "]
    return random.choice(open_nodes) if open_nodes else None

board = st.session_state.ttt_board
current_match_status = evaluate_game_state(board)

# Live Score Tracking Automation Logic Core
if current_match_status and not st.session_state.ttt_score_locked:
    st.session_state.ttt_played += 1
    if current_match_status == "X":
        st.session_state.ttt_wins += 1
    elif current_match_status == "O":
        st.session_state.ttt_losses += 1
    elif current_match_status == "TIE":
        st.session_state.ttt_ties += 1
    st.session_state.ttt_score_locked = True

# 📊 THE REAL-TIME PERSISTENT SIDEBAR SCOREBOARD
with st.sidebar:
    st.markdown("---")
    st.markdown("### 📊 NEURAL SCOREBOARD")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="MATCHES PLAYED", value=st.session_state.ttt_played)
        st.metric(label="VICTORIES 🏆", value=st.session_state.ttt_wins)
    with col2:
        st.metric(label="BOT CRASHES 💀", value=st.session_state.ttt_losses)
        st.metric(label="GRID TIES 🤝", value=st.session_state.ttt_ties)
    st.markdown("---")

# Match evaluation display alerts
if current_match_status:
    if current_match_status == "X": st.success("🎉 MAINFRAME ACCESS GRANTED! Player Wins!")
    elif current_match_status == "O": st.error("💀 PROTOCOL ABORTED! The Neural Bot Core claims victory.")
    else: st.warning("🤝 SYSTEM LOCKOUT! It's a draw matrix layout.")
else:
    st.markdown("##### 📝 TARGET VECTOR SECTORS:")

st.markdown(" ")

# =========================================================================
# SYSTEM GRID ARENA RENDERING LOOP
# =========================================================================
for row_idx in range(3):
    grid_cols = st.columns(3)
    for col_idx in range(3):
        idx = row_idx * 3 + col_idx
        with grid_cols[col_idx]:
            cell_value = board[idx]
            display_char = cell_value if cell_value != " " else " "
            is_inactive = current_match_status is not None or cell_value != " "
            
            if st.button(display_char, key=f"cell_{idx}", use_container_width=True, disabled=is_inactive):
                board[idx] = "X"
                current_match_status = evaluate_game_state(board)
                
                # Run bot logic instantly if match is ongoing without forcing hard reboots
                if not current_match_status:
                    bot_move_idx = calculate_bot_vector(board)
                    if bot_move_idx is not None:
                        board[bot_move_idx] = "O"
                st.rerun()

st.markdown(" ")

if st.button("🔄 RE-INITIALIZE GAME FIELD MATRIX", use_container_width=True, type="primary"):
    st.session_state.ttt_board = [" " for _ in range(9)]
    st.session_state.ttt_score_locked = False
    st.rerun()

# Studio Production Insignia Card Anchor
footer_html = "<div style='text-align: center; padding: 10px; margin-top: 20px;'><p style='color: #ff66aa; font-family: \"Courier New\", monospace; font-size: 1rem; margin: 0; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</p></div>"
st.markdown("---"); st.markdown(footer_html, unsafe_allow_html=True)
