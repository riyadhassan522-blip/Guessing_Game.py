import streamlit as st
import random
import copy

st.set_page_config(
    page_title="Mainframe Sudoku Core", 
    page_icon="🧩", 
    layout="centered"
)

# =========================================================================
# CENTRAL MATHEMATICAL BACKTRACKING ENGINE
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

# =========================================================================
# APPLICATION ENVIRONMENT STATE MEMORY
# =========================================================================
if "sdk_puzzle" not in st.session_state:
    base_board, solved_map = generate_base_puzzle(cells_to_remove=35)
    st.session_state.sdk_puzzle = base_board
    st.session_state.sdk_solution = solved_map
    st.session_state.sdk_locked_mask = [[base_board[r][c] != 0 for c in range(9)] for r in range(9)]
    st.session_state.sdk_user_matrix = copy.deepcopy(base_board)

# =========================================================================
# ARCADE STYLES ENGINE: BULLETPROOF HTML GRID ARCHITECTURE
# =========================================================================
css_style = """
<style>
html, body, p, span, label, div, h1, h3, select, button {
    font-family: 'Courier New', Courier, monospace !important;
    font-weight: bold !important;
}

/* THE CORE SOLID GAMING CABINET CARD PANEL */
.stMainBlockContainer {
    background-color: rgba(30, 14, 24, 0.92) !important;
    backdrop-filter: blur(15px) !important;
    border: 4px solid #1a0c12 !important;
    border-radius: 16px !important;
    box-shadow: 8px 8px 0px #1a0c12 !important;
    padding: 30px !important;
    margin-top: 40px !important;
}

/* 🎯 THE PERFECT 9x9 BOARD FIELD PLANE GRID CONTAINER */
.sudoku-container {
    display: flex;
    justify-content: center;
    margin: 25px 0;
}

.sudoku-table {
    border-collapse: collapse;
    border: 4px solid #ff66aa !important;
    box-shadow: 0px 0px 20px rgba(255, 102, 170, 0.2);
}

.sudoku-cell {
    width: 45px;
    height: 45px;
    text-align: center;
    border: 1px solid rgba(255, 102, 170, 0.25);
    padding: 0;
    margin: 0;
}

/* Force standard 3x3 block sub-grid quadrant borders */
.sudoku-row:nth-child(3n) .sudoku-cell { border-bottom: 3px solid #ff66aa !important; }
.sudoku-cell:nth-child(3n) { border-right: 3px solid #ff66aa !important; }

/* Dynamic cell styling wrappers */
.locked-node {
    background-color: rgba(255, 102, 170, 0.15);
    color: #ffffff;
    font-size: 1.4rem;
    font-weight: 900;
    line-height: 45px;
    text-shadow: 0px 0px 6px #ff66aa;
}

.player-input-cell {
    width: 100%;
    height: 100%;
    background-color: #1a0b14 !important;
    color: #ff88bb !important;
    border: none !important;
    text-align: center !important;
    font-size: 1.3rem !important;
    font-weight: 900 !important;
    outline: none !important;
}
.player-input-cell:focus {
    background-color: #2b1121 !important;
    color: #ff66aa !important;
}

/* Retro Arcade 3D Button Configurations */
div.stButton > button:first-child {
    background: #ff66aa !important;
    color: #1a0c12 !important;
    border: 3px solid #1a0c12 !important;
    font-weight: 900 !important;
    font-size: 1.1rem !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    border-radius: 8px !important;
    box-shadow: 0px 5px 0px #992255 !important;
    transition: all 0.1s ease-in-out !important;
    width: 100% !important;
}
div.stButton > button:first-child:active {
    transform: translateY(3px) !important;
    box-shadow: 0px 2px 0px #992255 !important;
}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# =========================================================================
# SYSTEM BRANDING BANNER
# =========================================================================
st.markdown(
    "<div style='background-color: rgba(45, 20, 32, 0.70); padding: 20px; border-radius: 12px; text-align: center; border: 4px solid #1a0c12; box-shadow: 6px 6px 0px #1a0c12; margin-bottom: 25px;'>\n"
    "    <h1 style='color: #ff66aa; margin: 0; font-size: 2rem; letter-spacing: 2px; text-shadow: 2px 2px 0px #1a0c12;'>🧩 SYSTEM SUDOKU DECK 🧩</h1>\n"
    "    <p style='color: #ffffff; margin: 6px 0 0 0; font-size: 0.9rem;'>[ RUNTIME SECTOR: HARD CONSTRAINT SOLVER ]</p>\n"
    "</div>",
    unsafe_allow_html=True
)

# =========================================================================
# ARCADE CONFIGURATION CONTROLS
# =========================================================================
difficulty_rank = st.selectbox(
    "Select Target Matrix Complexity:",
    ["1. Novice Core (30 blanks)", "2. Skilled Terminal (42 blanks)", "3. Master Matrix (52 blanks)"]
)

if st.button("🚀 EXECUTE GENERATOR SYNC", use_container_width=True, type="primary"):
    blanks = 30 if "1." in difficulty_rank else (42 if "2." in difficulty_rank else "52")
    base_board, solved_map = generate_base_puzzle(cells_to_remove=int(blanks))
    st.session_state.sdk_puzzle = base_board
    st.session_state.sdk_solution = solved_map
    st.session_state.sdk_locked_mask = [[base_board[r][c] != 0 for c in range(9)] for r in range(9)]
    st.session_state.sdk_user_matrix = copy.deepcopy(base_board)
    st.rerun()

st.markdown("---")

# =========================================================================
# DYNAMIC MATRIX SYNC GENERATION LAYER
# =========================================================================
# Catch query parameters to parse cell updates before submission loops
query_params = st.query_transform()

# Process data alterations natively through query loops
for r in range(9):
    for c in range(9):
        key = f"cell_{r}_{c}"
        if key in st.context.query_params:
            try:
                user_val = int(st.context.query_params[key][0])
                if 0 <= user_val <= 9:
                    st.session_state.sdk_user_matrix[r][c] = user_val
            except:
                pass

# Renders the absolute geometric 9x9 HTML Grid Table Structure
table_html = "<div class='sudoku-container'><table class='sudoku-table'>"
for r in range(9):
    table_html += "<tr class='sudoku-row'>"
    for c in range(9):
        if st.session_state.sdk_locked_mask[r][c]:
            table_html += f"<td class='sudoku-cell locked-node'>{st.session_state.sdk_puzzle[r][c]}</td>"
        else:
            val = st.session_state.sdk_user_matrix[r][c]
            val_str = str(val) if val != 0 else ""
            # Injecting standard fields with automated web arguments to save input values natively
            table_html += f"""<td class='sudoku-cell'>
                <input type='text' maxlength='1' class='player-input-cell' value='{val_str}' 
                onchange="const url=new URL(window.location); url.searchParams.set('cell_{r}_{c}', this.value || '0'); window.history.replaceState({{}}, '', url); location.reload();">
            </td>"""
    table_html += "</tr>"
table_html += "</table></div>"

st.markdown(table_html, unsafe_allow_html=True)

# =========================================================================
# EVALUATION MECHANICS
# =========================================================================
col_check, col_solve = st.columns(2)

with col_check:
    if st.button("💥 ANALYZE GRID CORES", use_container_width=True):
        if st.session_state.sdk_user_matrix == st.session_state.sdk_solution:
            st.success("🎉 SECURITY PROTOCOL CRACKED! Sudoku encryption complete!")
        else:
            st.error("❌ INTEGRITY FAILURE! Matrix contains conflicting path coordinates.")

with col_solve:
    if st.button("👁️ AUTO-CRACK GRID", use_container_width=True):
        st.session_state.sdk_user_matrix = copy.deepcopy(st.session_state.sdk_solution)
        st.toast("⚡ Mainframe solver dispatched. Solution injected natively!")
        st.rerun()

# 5. STUDIO PRODUCTION INSIGNIA
st.markdown("---")
footer_html = "<div style='text-align: center; padding: 10px;'><p style='color: #ff66aa; font-family: \"Courier New\", monospace; font-size: 1rem; margin: 0; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</p></div>"
st.markdown(footer_html, unsafe_allow_html=True)
