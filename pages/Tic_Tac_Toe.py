import streamlit as st
import random
import time
import base64

st.set_page_config(
    page_title="Mainframe Tic-Tac-Toe", 
    page_icon="❌", 
    layout="centered"
)

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

/* SAFE TYPOGRAPHY: Excludes icons completely so font labels function natively */
h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stMetric, input, button, span:not([class*="Icon"]):not([class*="icon"]):not([class*="material"]) {{
    font-family: 'Courier New', Courier, monospace !important;
    font-weight: bold !important;
}}

[data-testid='stSidebar'], [data-testid='stSidebarUserContent'] {{ background-color: rgba(30, 15, 23, 0.25) !important; backdrop-filter: blur(16px) !important; border-right: 3px solid #ff66aa !important; }}
[data-testid="stSidebarNav"] ul {{ background-color: rgba(37, 22, 31, 0.70) !important; border-radius: 8px !important; border: 1px solid rgba(255, 102, 170, 0.4) !important; padding: 10px !important; }}
[data-testid="stSidebarNav"] span {{ color: #ffffff !important; }}

.main .block-container {{ padding-top: 60px !important; }}

.stMainBlockContainer {{
    background-color: rgba(37, 22, 31, 0.45) !important; backdrop-filter: blur(16px) !important;
    border: 2px solid rgba(255, 102, 170, 0.4) !important; 
    border-radius: 24px !important; /* Perfect uniform capsule rounded borders */
    box-shadow: 0px 8px 32px rgba(255, 102, 170, 0.15) !important; padding: 35px !important;
}}

/* 🎯 COMPACT NATIVE HTML ARENA GRID TABLE ENGINE */
.ttt-container {{ display: flex; justify-content: center; margin: 15px 0; }}
.ttt-table {{ border-collapse: collapse; border: 3px solid rgba(255, 102, 170, 0.6) !important; border-radius: 12px !important; overflow: hidden; }}
.ttt-cell {{ width: 68px !important; height: 68px !important; text-align: center; border: 2px solid rgba(255, 102, 170, 0.3) !important; padding: 0 !important; margin: 0 !important; }}
.ttt-btn {{
    width: 100% !important; height: 100% !important; background-color: rgba(37, 22, 31, 0.45) !important; backdrop-filter: blur(10px) !important;
    color: #ff66aa !important; border: none !important; font-size: 1.6rem !important; font-weight: 900 !important; cursor: pointer; transition: all 0.15s;
}}
.ttt-btn:hover:not(:disabled) {{ background-color: rgba(255, 102, 170, 0.15) !important; }}
div.stButton > button[type="primary"] {{
    background: #ff66aa !important; color: #1a0c12 !important; border: none !important; font-size: 1.1rem !important; height: 45px !important; border-radius: 8px !important;
}}
div[data-testid='stMetricValue'] {{ font-weight: 900 !important; color: #ff66aa !important; text-shadow: 2px 2px 0px #1a0c12 !important; font-size: 1.5rem !important; }}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

st.markdown("<div style='background-color: rgba(45, 20, 32, 0.40); backdrop-filter: blur(10px); padding: 25px; border-radius: 16px; text-align: center; border: 1px solid rgba(255, 102, 170, 0.25); box-shadow: 0px 4px 15px rgba(255, 102, 170, 0.1); margin-bottom: 35px;'><h1 style='color: #ff66aa; margin: 0; font-family: \"Courier New\", monospace; font-size: 2.1rem; letter-spacing: 2px; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>❌ NEURAL MATRIX GRID ⭕</h1></div>", unsafe_allow_html=True)

for r in range(3):
    for c in range(3):
        key = f"ttt_hit_{r}_{c}"
        if key in st.query_params:
            idx = r * 3 + c
            if st.session_state.ttt_board[idx] == " ":
                st.session_state.ttt_board[idx] = "X"

board = st.session_state.ttt_board

def evaluate_game_state(b):
    win_lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for vector in win_lines:
        if b[vector[0]] == b[vector[1]] == b[vector[2]] and b[vector[0]] != " ": return b[vector[0]]
    if " " not in b: return "TIE"
    return None

current_match_status = evaluate_game_state(board)

if not current_match_status and board.count("X") > board.count("O"):
    win_lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    moved = False
    for vector in win_lines:
        tokens = [board[vector[0]], board[vector[1]], board[vector[2]]]
        if tokens.count("O") == 2 and tokens.count(" ") == 1:
            board[vector[tokens.index(" ")]] = "O"; moved = True; break
    if not moved:
        for vector in win_lines:
            tokens = [board[vector[0]], board[vector[1]], board[vector[2]]]
            if tokens.count("X") == 2 and tokens.count(" ") == 1:
                board[vector[tokens.index(" ")]] = "O"; moved = True; break
    if not moved and board[4] == " ": board[4] = "O"; moved = True
    if not moved:
        open_nodes = [i for i, cell in enumerate(board) if cell == " "]
        if open_nodes: board[random.choice(open_nodes)] = "O"
    current_match_status = evaluate_game_state(board)

if current_match_status and not st.session_state.ttt_score_locked:
    st.session_state.ttt_played += 1
    if current_match_status == "X": st.session_state.ttt_wins += 1
    elif current_match_status == "O": st.session_state.ttt_losses += 1
    elif current_match_status == "TIE": st.session_state.ttt_ties += 1
    st.session_state.ttt_score_locked = True

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

if current_match_status:
    if current_match_status == "X": st.success("🎉 MAINFRAME ACCESS GRANTED! Player Wins!")
    elif current_match_status == "O": st.error("💀 PROTOCOL ABORTED! The Neural Bot Core claims victory.")
    else: st.warning("🤝 SYSTEM LOCKOUT! It's a draw matrix layout.")
else: st.markdown("##### 📝 TARGET VECTOR SECTORS:")

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

if st.button("🔄 RE-INITIALIZE GAME FIELD MATRIX", use_container_width=True, type="primary"):
    st.session_state.ttt_board = [" " for _ in range(9)]
    st.session_state.ttt_score_locked = False
    st.query_params.clear()
    st.rerun()

footer_html = "<div style='text-align: center; padding: 10px; margin-top: 20px;'><p style='color: #ff66aa; font-family: \"Courier New\", monospace; font-size: 1rem; margin: 0; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</p></div>"
st.markdown("---"); st.markdown(footer_html, unsafe_allow_html=True)
