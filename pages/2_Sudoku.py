import streamlit as st
import random
import copy

st.set_page_config(
    page_title="Mainframe Sudoku Core", 
    page_icon="🧩", 
    layout="centered"
)

# =========================================================================
# CENTRAL LOGIC MATRIX: THE BACKTRACKING VALIDATION ENGINE
# =========================================================================
def is_valid_move(board, row, col, num):
    """Verifies grid compliance against Row, Column, and 3x3 Quadrant rules"""
    # Check horizontal row constraint path
    if num in board[row]:
        return False
        
    # Check vertical column constraint path
    if num in [board[i][col] for i in range(9)]:
        return False
        
    # Check 3x3 sub-grid matrix block quadrant boundary
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
                
    return True

def solve_sudoku_matrix(board):
    """Natively solves any 9x9 layout utilizing a recursive backtracking loop"""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku_matrix(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_base_puzzle(cells_to_remove=35):
    """Generates an initialized puzzle matrix matching targeted difficulty seeds"""
    # Initialize an unmapped 9x9 blank array grid
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    # Populate the primary diagonal block vectors to seed random distribution paths Safely
    for box in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                board[box + i][box + j] = nums.pop()
                
    # Complete the core array map via solver execution
    solve_sudoku_matrix(board)
    solution = copy.deepcopy(board)
    
    # Punch blank analytical sockets out of the completed field plane
    attempts = cells_to_remove
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            attempts -= 1
            
    return board, solution

# =========================================================================
# ARCADE STYLES ENGINE: CUSTOM MATRIX GRID SYSTEM
# =========================================================================
css_style = """
<style>
/* Synchronize global typography seamlessly with Lord's Monospace palette guidelines */
html, body, [class*="css"], p, span, label, h3, select {
    font-family: 'Courier New', Courier, monospace !important;
    font-weight: bold !important;
}

/* 🎯 PREMIUM ARCADE SUDOKU MATRIX INPUT STYLING */
div[data-testid="stNumberInput"] input {
    background-color: rgba(37, 22, 31, 0.90) !important;
    color: #ff66aa !important;
    border: 1px solid rgba(255, 102, 170, 0.3) !important;
    text-align: center !important;
    font-size: 1.3rem !important;
    font-weight: 900 !important;
    border-radius: 6px !important;
    padding: 0 !important;
    height: 42px !important;
}

/* Hide native form instructions underneath individual math boxes */
div[data-testid="stNumberInput"] [data-baseweb="input"] + div {
    display: none !important;
}

/* Strip native calculation buttons to ensure clean mobile device layout tracking */
div[data-testid="stNumberInput"] button {
    display: none !important;
}

/* Locked core starting numbers get high contrast white typography indicators */
.locked-cell {
    color: #ffffff !important;
    text-shadow: 0px 0px 8px #ff66aa !important;
}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# =========================================================================
# APPLICATION ENVIRONMENT MEMORY MANAGEMENT
# =========================================================================
if "sdk_puzzle" not in st.session_state:
    # Initialize basic grid arrays on primary system spin up
    base_board, solved_map = generate_base_puzzle(cells_to_remove=30)
    st.session_state.sdk_puzzle = base_board
    st.session_state.sdk_solution = solved_map
    # Keep track of original structural sockets so players can't overwrite locked nodes
    st.session_state.sdk_locked_mask = [[base_board[r][c] != 0 for c in range(9)] for r in range(9)]
    st.session_state.sdk_user_matrix = copy.deepcopy(base_board)

# =========================================================================
# SYSTEM BRANDING BANNER
# =========================================================================
st.markdown(
    "<div style='background-color: rgba(45, 20, 32, 0.40); backdrop-filter: blur(10px); padding: 20px; border-radius: 12px; text-align: center; border: 1px solid rgba(255, 102, 170, 0.25); margin-bottom: 25px;'>\n"
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
# Renders 9 core vertical column segments bounded within grid grids natively
for r in range(9):
    grid_cols = st.columns(9)
    for c in range(9):
        with grid_cols[c]:
            is_locked = st.session_state.sdk_locked_mask[r][c]
            
            if is_locked:
                # Displays the core static node values cleanly wrapped in visual markers
                st.markdown(
                    f"<div style='text-align:center; line-height:42px; background-color:rgba(255,102,170,0.15); "
                    f"border:1px solid #ff66aa; border-radius:6px; height:42px; font-weight:900; color:#ffffff; "
                    f"font-size:1.2rem; text-shadow:0px 0px 6px #ff66aa;'>{st.session_state.sdk_puzzle[r][c]}</div>", 
                    unsafe_allow_html=True
                )
            else:
                # Players manipulate open analytical fields natively using numeric slots
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
