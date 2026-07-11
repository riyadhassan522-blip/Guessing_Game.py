import streamlit as st
import random
import time
import base64

st.set_page_config(
    page_title="Mainframe Tic-Tac-Toe", 
    page_icon="❌", 
    layout="centered"
)

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file: return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError: return ""

bg_base64 = get_base64_image("themes/bg.jpg")

# =========================================================================
# UNIFIED COMPONENT STYLE ENGINE (Matches Guessing Game 100%)
# =========================================================================
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
.stMainBlockContainer {{
    background-color: rgba(35, 16, 25, 0.75) !important; backdrop-filter: blur(12px) !important;
    border: 4px solid #1a0c12 !important; border-radius: 12px !important; box-shadow: 8px 8px 0px #1a0c12 !important; padding: 35px !important; margin-top: 50px !important;
}}

/* 🎯 THE CHUNKY 3x3 ARENA GRID LAYOUT SYSTEM */
div.stButton > button:first-child {{
    background: #ff66aa !important; color: #1a0c12 !important; border: 3px solid #1a0c12 !important; font-weight: 900 !important;
    font-size: 1.8rem !important; height: 80px !important; text-transform: uppercase !important; border-radius: 8px !important;
    box-shadow: 0px 6px 0px #992255 !important; transition: all 0.1s ease-in-out !important; width: 100% !important; margin-bottom: 15px !important;
}}
div.stButton > button:first-child:active {{ transform: translateY(4px) !important; box-shadow: 0px 2px 0px #992255 !important; }}
button[aria-label="Collapse sidebar"], button[aria-label="Expand sidebar"] {{ display: none !important; }}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

st.markdown("<div style='background-color: rgba(45, 20, 32, 0.40); backdrop-filter: blur(10px); padding: 25px; border-radius: 12px; text-align: center; border: 1px solid rgba(255, 102, 170, 0.25); box-shadow: 0px 4px 15px rgba(255, 102, 170, 0.1); margin-bottom: 35px;'><h1 style='color: #ff66aa; margin: 0; font-family: \"Courier New\", monospace; font-size: 2.1rem; letter-spacing: 2px; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>❌ NEURAL MATRIX GRID ⭕</h1></div>", unsafe_allow_html=True)

# Initialize Isolated Board Array State Memory
if "ttt_board" not in st.session_state:
    st.session_state.ttt_board = [" " for _ in range(9)]

st.markdown("##### 📝 TARGET VECTOR SECTORS:")
st.markdown(" ")

# 🦾 INTERACTIVE 3x3 ARENA RENDER LOOP
board = st.session_state.ttt_board
for row_idx in range(3):
    grid_cols = st.columns(3)
    for col_idx in range(3):
        idx = row_idx * 3 + col_idx
        with grid_cols[col_idx]:
            # Shows current cell occupant ('X', 'O', or blank space)
            display_text = board[idx] if board[idx] != " " else "·"
            if st.button(display_text, key=f"cell_{idx}", use_container_width=True):
                if board[idx] == " ":
                    board[idx] = "X"
                    st.toast(f"Vector signature locked at space index: {idx+1}")
                    st.rerun()

if st.button("🔄 RE-INITIALIZE GAME FIELD MATRIX", use_container_width=True, type="primary"):
    st.session_state.ttt_board = [" " for _ in range(9)]
    st.rerun()

st.markdown("---")
footer_html = "<div style='text-align: center; padding: 10px;'><p style='color: #ff66aa; font-family: \"Courier New\", monospace; font-size: 1rem; margin: 0; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</p></div>"
st.markdown(footer_html, unsafe_allow_html=True)
