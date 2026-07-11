import streamlit as st
import random
import copy
import time
import base64

st.set_page_config(
    page_title="Mainframe Sudoku Core", 
    page_icon="🧩", 
    layout="centered"
)

# Native asset loader assigned strictly to this sub-page instance
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""

bg_base64 = get_base64_image("themes/bg.jpg")

# =========================================================================
# ISOLATED BACKTRACKING MATHEMATICAL RESOLUTION ENGINE
# =========================================================================
def is_valid_move(board, row, col, num):
    if num in board[row]: return False
    if num in [board[i][col] for i in range(9)]: return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num: return False
    return True

def solve_sudoku_matrix(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku_matrix(board): return True
                        board[row][col] = 0
                return False
    return True

def generate_base_puzzle(cells_to_remove=35):
    board = [[0 for _ in range(9)] for _ in range(9)]
    for box in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3): board[box + i][box + j] = nums.pop()
    solve_sudoku_matrix(board)
    solution = copy.deepcopy(board)
    attempts = cells_to_remove
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            attempts -= 1
    return board, solution

def trigger_arcade_synth():
    st.markdown("""<audio autoplay style="display:none;"><source src="data:audio/wav;base64,UklGRigAAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQQAAAAAf39/fw==" type="audio/wav"></audio>""", unsafe_allow_html=True)

# =========================================================================
# SUDOKU CORE EXCLUSIVE GRAPHICS WRAPPER (Zero Global Leakage)
# =========================================================================
css_style = f"""
<style>
.stApp, [data-testid='stAppViewContainer'], .stAppHeader, [data-testid='stHeader'] {{
    background-image: linear-gradient(rgba(18, 8, 15, 0.60), rgba(18, 8, 15, 0.75)), 
                url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important;
    background-position: center center !important;
    background-attachment: fixed !important;
}}
html, body, p, span, label, div, h1, h3, select {{
    font-family: 'Courier New', Courier, monospace !important;
    font-weight: bold !important;
}}
/* SOLID HIGH-CONTRAST PANEL: Isolates the 9x9 board so it's fully visible and solid */
div[data-testid='stForm'], .stMainBlockContainer {{
    background-color: rgba(30, 14, 24, 0.94) !important;
    backdrop-filter: blur(20px) !important;
    border: 3px solid #ff66aa !important;
    border-radius: 16px !important;
    box-shadow: 0px 0px 25px rgba(255, 102, 170, 0.25) !important;
    padding: 30px !important;
    max-width: 100% !important;
}}
/* TARGETED SUDOKU CELL HOOKS */
div[data-testid="stNumberInput"] input {{
    background-color: #1a0b14 !important;
    color: #ff66aa !important;
    border: 2px solid rgba(255, 102, 170, 0.4) !important;
    text-align: center !important;
    font-size: 1.4rem !important;
    font-weight: 900 !important;
    border-radius: 8px !important;
    height: 45px !important;
}}
div[data-testid="stNumberInput"] [data-baseweb="input"] {{
    background-color: transparent !important;
    border: none !important;
}}
div[data-testid="stNumberInput"] [data-baseweb="input"] + div,
div[data-testid="stNumberInput"] button {{
    display: none !important;
}}
/* Sidebar Navigation Overrides */
[data-testid='stSidebar'], [data-testid='stSidebarUserContent'] {{
    background-color: rgba(30, 15, 23, 0.25) !important;
    backdrop-filter: blur(16px) !important;
    border-right: 3px solid #ff66aa !important;
}}
[data-testid="stSidebarNav"] ul {{
    background-color: rgba(37, 22, 31, 0.60) !important;
    border-radius: 8px !important;
    border: 1px solid rgba(255, 102, 170, 0.2) !important;
    padding: 12px !important;
}}
[data-testid="stSidebarNav"] span {{ color: #ffffff !important; }}
button[aria-label="Collapse sidebar"], button[aria-label="Expand sidebar"] {{ display: none !important; }}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)
# =========================================================================
# APPLICATION ENVIRONMENT MEMORY MANAGEMENT
# =========================================================================
if "sdk_puzzle" not in st.session_state:
    base_board, solved_map = generate_base_puzzle(cells_to_remove=30)
    st.session_state.sdk_puzzle = base_board
    st.session_state.sdk_solution = solved_map
    st.session_state.sdk_locked_mask = [[base_board[r][c] != 0 for c in range(9)] for r in range(9)]
    st.session_state.sdk_user_matrix = copy.deepcopy(base_board)

# =========================================================================
# SYSTEM BRANDING BANNER
# =========================================================================
st.markdown(
    "<div style='background-color: rgba(45, 20, 32, 0.40); backdrop-filter: blur(10px); padding: 20px; border-radius: 12px; text-align: center; border: 1px solid rgba(255, 102, 170, 0.25); box-shadow: 0px 4px 15px rgba(255, 102, 170, 0.1); margin-bottom: 25px;'>\n"
    "    <h1 style='color: #ff66aa; margin: 0; font-family: \"Courier New\", monospace; font-size: 2rem; letter-spacing: 2px; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>\n"
    "        🧩 SYSTEM SUDOKU DECK 🧩\n"
    "    </h1>\n"
    "    <p style='color: #ffffff; margin: 6px 0 0 0; font-size: 0.9rem; font-family: \"Courier New\", monospace; font-weight: bold;'>\n"
    "        [ RUNTIME SECTOR: HARD CONSTRAINT SOLVER ]\n"
    "    </p>\n"
    "</div>",
    unsafe_allow_html=True
)

# =========================================================================
# ARCADE CONFIGURATION CONTROLS
# =========================================================================
st.markdown("### ⚙️ DEPLOYMENT ENGINE")
difficulty_rank = st.selectbox(
    "Select Target Matrix Complexity:",
    ["1. Novice Core (30 blanks)", "2. Skilled Terminal (40 blanks)", "3. Master Matrix (52 blanks)"]
)

if st.button("🚀 EXECUTE GENERATOR SYNC", use_container_width=True, type="primary"):
    if "1." in difficulty_rank: blanks = 30
    elif "2." in difficulty_rank: blanks = 40
    else: blanks = 52
    
    with st.spinner("🔄 DRILLING MATRIX HOLES..."):
        base_board, solved_map = generate_base_puzzle(cells_to_remove=blanks)
        st.session_state.sdk_puzzle = base_board
        st.session_state.sdk_solution = solved_map
        st.session_state.sdk_locked_mask = [[base_board[r][c] != 0 for c in range(9)] for r in range(9)]
        st.session_state.sdk_user_matrix = copy.deepcopy(base_board)
    st.rerun()

st.markdown("---")
st.markdown("##### 📝 TARGET COMPLIANCE LAYER:")

# =========================================================================
# 9x9 COMPACT INTERACTIVE ARENA ENGINE
# =========================================================================
for r in range(9):
    grid_cols = st.columns(9)
    for c in range(9):
        with grid_cols[c]:
            is_locked = st.session_state.sdk_locked_mask[r][c]
            
            if is_locked:
                st.markdown(
                    f"<div style='text-align:center; line-height:42px; background-color:rgba(255,102,170,0.25); "
                    f"border:2px solid #ff66aa; border-radius:8px; height:45px; font-weight:900; color:#ffffff; "
                    f"font-size:1.3rem; text-shadow:0px 0px 8px #ff66aa;'>{st.session_state.sdk_puzzle[r][c]}</div>", 
                    unsafe_allow_html=True
                )
            else:
                val = st.session_state.sdk_user_matrix[r][c]
                user_move = st.number_input(
                    label=f"cell_{r}_{c}",
                    min_value=0,
                    max_value=9,
                    step=1,
                    value=int(val) if val != 0 else 0,
                    key=f"cell_{r}_{c}",
                    label_visibility="collapsed"
                )
                st.session_state.sdk_user_matrix[r][c] = user_move

st.markdown(" ")

# =========================================================================
# EVALUATION MECHANICS
# =========================================================================
col_check, col_solve = st.columns(2)

with col_check:
    if st.button("💥 ANALYZE GRID CORES", use_container_width=True):
        trigger_arcade_synth()
        is_perfect = True
        
        for r in range(9):
            for c in range(9):
                if st.session_state.sdk_user_matrix[r][c] != st.session_state.sdk_solution[r][c]:
                    is_perfect = False
                    break
        
        if is_perfect:
            st.success("🎉 SECURITY PROTOCOL CRACKED! Sudoku encryption complete!")
        else:
            st.error("❌ INTEGRITY FAILURE! Matrix contains conflicting path coordinates.")

with col_solve:
    if st.button("👁️ AUTO-CRACK GRID", use_container_width=True):
        trigger_arcade_synth()
        st.session_state.sdk_user_matrix = copy.deepcopy(st.session_state.sdk_solution)
        st.toast("⚡ Mainframe solver dispatched. Solution injected natively!")
        st.rerun()

# 5. STUDIO PRODUCTION INSIGNIA
st.markdown("---")
footer_html = "<div style='text-align: center; padding: 10px; margin-top: 10px;'><p style='color: #614653; font-family: \"Courier New\", monospace; font-size: 0.85rem; margin: 0; font-weight: bold;'>© 2026 DARKNESS GAMING LABS | ALL RIGHTS RESERVED</p><p style='color: #ff66aa; font-family: \"Courier New\", monospace; font-size: 1rem; margin: 5px 0 0 0; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</p></div>"
st.markdown(footer_html, unsafe_allow_html=True)
