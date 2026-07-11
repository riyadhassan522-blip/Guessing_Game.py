import streamlit as st
import random
import time
import base64

st.set_page_config(
    page_title="Mainframe Tic-Tac-Toe", 
    page_icon="❌", 
    layout="centered"
)

# Universal theme synchronization parameters
if "theme_glow" not in st.session_state: st.session_state.theme_glow = "🌸 Cyber Cherry Blossom"
if "theme_bg_file" not in st.session_state: st.session_state.theme_bg_file = "Pagoda Waterfall (Default)"

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file: return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError: return ""

if st.session_state.theme_bg_file == "Retro Arcade Cabinet Room": bg_base64 = get_base64_image("themes/bg2.jpg")
else: bg_base64 = get_base64_image("themes/bg.jpg")

if "🧪 Toxic Lime Green" in st.session_state.theme_glow:
    glow_color, shadow_color, glass_base = "#39ff14", "#139900", "rgba(18, 30, 20, 0.45)"
elif "🔥 Synthwave Laser Orange" in st.session_state.theme_glow:
    glow_color, shadow_color, glass_base = "#ff6600", "#992200", "rgba(35, 18, 14, 0.45)"
else:
    glow_color, shadow_color, glass_base = "#ff66aa", "#992255", "rgba(37, 22, 31, 0.45)"

if "ttt_played" not in st.session_state: st.session_state.ttt_played = 0
if "ttt_wins" not in st.session_state: st.session_state.ttt_wins = 0
if "ttt_losses" not in st.session_state: st.session_state.ttt_losses = 0
if "ttt_ties" not in st.session_state: st.session_state.ttt_ties = 0
if "ttt_board" not in st.session_state: st.session_state.ttt_board = [" " for _ in range(9)]
if "ttt_score_locked" not in st.session_state: st.session_state.ttt_score_locked = False

css_style = f"""
<style>
.stApp, [data-testid='stAppViewContainer'], .stAppHeader, [data-testid='stHeader'] {{
    background-image: linear-gradient(rgba(15, 10, 14, 0.50), rgba(15, 10, 14, 0.70)), url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important; background-position: center center !important; background-attachment: fixed !important;
}}
html, body, p, span, label, div, h1, h2, h3 {{ font-family: 'Courier New', Courier, monospace !important; font-weight: bold !important; }}
[data-testid='stSidebar'], [data-testid='stSidebarUserContent'] {{ background-color: rgba(30, 15, 23, 0.25) !important; backdrop-filter: blur(16px) !important; border-right: 3px solid {glow_color} !important; }}
[data-testid="stSidebarNav"] ul {{ background-color: rgba(37, 22, 31, 0.70) !important; border-radius: 8px !important; border: 1px solid rgba(255, 102, 170, 0.2) !important; padding: 10px !important; }}
[data-testid="stSidebarNav"] span {{ color: #ffffff !important; }}

.main .block-container {{ padding-top: 60px !important; }}
.stMainBlockContainer {{
    background-color: {glass_base} !important; backdrop-filter: blur(16px) !important; -webkit-backdrop-filter: blur(16px) !important;
    border: 2px solid {glow_color}44 !important; border-radius: 24px !important; box-shadow: 0px 8px 32px rgba(0,0,0,0.2) !important; padding: 35px !important;
}}

.ttt-container {{ display: flex; justify-content: center; margin: 15px 0; }}
.ttt-table {{ border-collapse: collapse; border: 3px solid {glow_color}aa !important; border-radius: 12px !important; overflow: hidden; }}
.ttt-cell {{ width: 68px !important; height: 68px !important; text-align: center; border: 2px solid {glow_color}33 !important; padding: 0 !important; margin: 0 !important; }}
.ttt-btn {{
    width: 100% !important; height: 100% !important; background-color: rgba(30, 15, 23, 0.65) !important; backdrop-filter: blur(10px) !important;
    color: {glow_color} !important; border: none !important; font-size: 1.6rem !important; font-weight: 900 !important; cursor: pointer; transition: all 0.15s;
}}
.ttt-btn:hover:not(:disabled) {{ background-color: {glow_color}22 !important; }}
div.stButton > button[type="primary"] {{
    background: {glow_color} !important; color: #1a0c12 !important; border: 3px solid #1a0c12 !important; font-size: 1.1rem !important; height: 45px !important; border-radius: 8px !important; box-shadow: 0px 5px 0px {shadow_color} !important;
}}
div[data-testid='stMetricValue'] {{ font-weight: 900 !important; color: {glow_color} !important; text-shadow: 2px 2px 0px #1a0c12 !important; font-size: 1.5rem !important; }}

div.stAppViewContainer > div:first-child, [data-testid="collapsedControl"], [data-testid="stHeader"], .stAppHeader {{
    display: none !important; visibility: hidden !important; opacity: 0 !important; height: 0px !important; width: 0px !important;
}}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

st.markdown(f"<div style='background-color: rgba(45, 20, 32, 0.40); backdrop-filter: blur(10px); padding: 25px; border-radius: 16px; text-align: center; border: 1px solid {glow_color}44; box-shadow: 0px 4px 15px rgba(0,0,0,0.2); margin-bottom: 35px;'><h1 style='color: {glow_color}; margin: 0; font-family: \"Courier New\", monospace; font-size: 2.1rem; letter-spacing: 2px; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>❌ NEURAL MATRIX GRID ⭕</h1></div>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("---")
    st.markdown("### 🎨 CABINET INTERFACE")
    sel_glow = st.selectbox("NEON REVOLVER COLOR:", ["🌸 Cyber Cherry Blossom", "🧪 Toxic Lime Green", "🔥 Synthwave Laser Orange"], index=["🌸 Cyber Cherry Blossom", "🧪 Toxic Lime Green", "🔥 Synthwave Laser Orange"].index(st.session_state.theme_glow))
    sel_bg = st.selectbox("BACKGROUND ARTWORK:", ["Pagoda Waterfall (Default)", "Retro Arcade Cabinet Room"], index=["Pagoda Waterfall (Default)", "Retro Arcade Cabinet Room"].index(st.session_state.theme_bg_file))
    if sel_glow != st.session_state.theme_glow or sel_bg != st.session_state.theme_bg_file:
        st.session_state.theme_glow, st.session_state.theme_bg_file = sel_glow, sel_bg; st.rerun()

for r in range(3):
    for c in range(3):
        key = f"ttt_hit_{r}_{c}"
        if key in st.query_params:
            idx = r * 3 + c
            if st.session_state.ttt_board[idx] == " ": st.session_state.ttt_board[idx] = "X"

board = st.session_state.ttt_board

def evaluate_game_state(b):
    for v in [,,,,,,,]:
        if b[v] == b[v] == b[v] and b[v] != " ": return b[v]
    if " " not in b: return "TIE"
    return None

current_match_status = evaluate_game_state(board)

if not current_match_status and board.count("X") > board.count("O"):
    moved = False
    for v in [,,,,,,,]:
        tk = [board[v], board[v], board[v]]
        if tk.count("O") == 2 and tk.count(" ") == 1: board[v[tk.index(" ")]] = "O"; moved = True; break
    if not moved:
        for v in [,,,,,,,]:
            tk = [board[v], board[v], board[v]]
            if tk.count("X") == 2 and tk.count(" ") == 1: board[v[tk.index(" ")]] = "O"; moved = True; break
    if not moved and board == " ": board = "O"; moved = True
    if not moved:
        ops = [i for i, cell in enumerate(board) if cell == " "]
        if ops: board[random.choice(ops)] = "O"
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
    st.query_params.clear(); st.rerun()

footer_html = f"<div style='text-align: center; padding: 10px; margin-top: 20px;'><p style='color: {glow_color}; font-family: \"Courier New\", monospace; font-size: 1rem; margin: 0; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</p></div>"
st.markdown("---"); st.markdown(footer_html, unsafe_allow_html=True)
