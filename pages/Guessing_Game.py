import streamlit as st
import random

PAGE_TITLE = "🎯 Guessing Game"

def _difficulty_to_params(diff_str):
    if "Novice" in diff_str:
        return (1, 20), 8
    if "Easy" in diff_str:
        return (1, 50), 6
    if "Normal" in diff_str:
        return (1, 100), 5
    if "Hard" in diff_str:
        return (1, 200), 4
    return (1, 500), 3  # Expert

def _init_state(range_vals, default_lives):
    if "games" not in st.session_state:
        st.session_state.games = {}
    game = st.session_state.games.setdefault("guessing", {})
    
    if game.get("range") != list(range_vals) or game.get("default_lives") != int(default_lives):
        game["range"] = list(range_vals)
        game["default_lives"] = int(default_lives)
        game["target"] = random.randint(*range_vals)
        game["lives"] = int(default_lives)
        game["message"] = ""
        game["last_guess"] = None
        
    game.setdefault("stats", {"played": 0, "wins": 0, "losses": 0, "total_guesses": 0})
    return game

def reset_round(game):
    game["target"] = random.randint(*game["range"])
    game["lives"] = int(game.get("default_lives", 8))
    game["last_guess"] = None
    game["message"] = ""

def submit_guess(game, guess: int):
    game["last_guess"] = guess
    game["stats"]["total_guesses"] += 1
    
    gs = st.session_state.get("global_stats", {"played":0,"wins":0,"losses":0,"total_guesses":0})
    gs["total_guesses"] += 1
    
    if guess == game["target"]:
        game["message"] = f"🎉 CORRECT! Target signature locked at {game['target']}."
        game["stats"]["wins"] += 1
        game["stats"]["played"] += 1
        gs["played"] += 1; gs["wins"] += 1
        st.session_state["global_stats"] = gs
        reset_round(game)
    else:
        game["lives"] -= 1
        if game["lives"] <= 0:
            game["message"] = f"💥 CORE CRASH! Shield fully depleted. Target was {game['target']}."
            game["stats"]["losses"] += 1
            game["stats"]["played"] += 1
            gs["played"] += 1; gs["losses"] += 1
            st.session_state["global_stats"] = gs
            reset_round(game)
        else:
            hint = "HIGHER" if guess < game["target"] else "LOWER"
            game["message"] = f"⚡ CALIBRATION ERROR: Aim {hint}. System Integrity: {game['lives']} lives remaining."
            st.session_state["global_stats"] = gs

def app():
    # Injection of specific inner-module card theme enhancements
    st.markdown(
        """
        <style>
        .terminal-header {
            text-align: center;
            color: #ff66aa;
            text-shadow: 0 0 10px rgba(255,102,170,0.6);
            font-size: 32px;
            letter-spacing: 2px;
            margin-bottom: 20px;
        }
        .status-box {
            background: rgba(37, 22, 31, 0.6);
            border-left: 4px solid #ff66aa;
            padding: 15px;
            border-radius: 6px;
            margin: 15px 0;
        }
        .stat-grid-box {
            background: rgba(20, 10, 15, 0.5);
            border: 1px solid rgba(255,102,170,0.2);
            border-radius: 8px;
            padding: 15px;
            text-align: center;
            box-shadow: inset 0 0 8px rgba(255,102,170,0.05);
        }
        .stat-val {
            font-size: 24px;
            font-weight: bold;
            color: #ff66aa;
        }
        div[data-testid="stForm"] {
            background: rgba(26, 12, 18, 0.4) !important;
            border: 1px solid rgba(255, 102, 170, 0.25) !important;
            border-radius: 12px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='frosted'>", unsafe_allow_html=True)
    st.markdown("<h1 class='terminal-header'>🎯 TARGET RADAR SCANNER</h1>", unsafe_allow_html=True)

    # ─── CONFIGURATION ZONE ───
    diff = st.selectbox(
        "⚙️ CORE SYSTEM DIFFICULTY CONFIGURATION",
        [
            "Novice (1–20, 8 lives)",
            "Easy (1–50, 6 lives)",
            "Normal (1–100, 5 lives)",
            "Hard (1–200, 4 lives)",
            "Expert (1–500, 3 lives)"
        ],
        index=0,
        key="game_internal_difficulty"
    )
    
    rng, lives = _difficulty_to_params(diff)
    game = _init_state(rng, lives)
    
    # Visual status bar block layout
    st.markdown(
        f"""
        <div class='status-box'>
            <b>📡 RADAR THRESHOLD:</b> {game['range'][0]} — {game['range'][1]} <br>
            <b>🛡️ SHIELD INTEGRITY:</b> {game['lives']} / {game['default_lives']} MATRIX UNITS
        </div>
        """, 
        unsafe_allow_html=True
    )

    # ─── ACTION CANVAS (THE FORM) ───
    with st.form("guess_form", clear_on_submit=False):
        col1, col2 = st.columns([3, 1])
        with col1:
            guess = st.number_input(
                "Input Coordinate Matrix Guess:",
                min_value=int(game["range"][0]),
                max_value=int(game["range"][1]),
                value=int(game["range"][0]),
                step=1,
                key="input_guess",
                label_visibility="collapsed"
            )
        with col2:
            submit = st.form_submit_button("⭐ DISPATCH SCAN")
            
        if submit:
            submit_guess(game, int(guess))
            st.rerun()

    # Dynamic Alert Feedback Layout
    if game["message"]:
        if "CORRECT" in game["message"]:
            st.success(game["message"])
        elif "CORE CRASH" in game["message"]:
            st.error(game["message"])
        else:
            st.warning(game["message"])

    st.markdown("<br><hr style='border-color: rgba(255,102,170,0.25);'>", unsafe_allow_html=True)
    
    # ─── VISUAL DATA HUB GRID ───
    st.markdown("<h3 style='color:#ffffff; font-size:16px; margin-bottom:15px;'>📊 LOCAL SECTOR PERFORMANCE</h3>", unsafe_allow_html=True)
    stats = game["stats"]
    
    # Custom HTML metrics grid layout to look clean and styled
    grid_col1, grid_col2, grid_col3, grid_col4 = st.columns(4)
    with grid_col1:
        st.markdown(f"<div class='stat-grid-box'><small>MATCHES</small><div class='stat-val'>{stats['played']}</div></div>", unsafe_allow_html=True)
    with grid_col2:
        st.markdown(f"<div class='stat-grid-box'><small>SCANS</small><div class='stat-val'>{stats['total_guesses']}</div></div>", unsafe_allow_html=True)
    with grid_col3:
        st.markdown(f"<div class='stat-grid-box'><small>WINS</small><div class='stat-val'>{stats['wins']}</div></div>", unsafe_allow_html=True)
    with grid_col4:
        st.markdown(f"<div class='stat-grid-box'><small>LOSSES</small><div class='stat-val'>{stats['losses']}</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Action control panel bar
    if st.button("🔄 REBOOT LOCAL AREA ROUND"):
        reset_round(game)
        st.toast("Core match restarted. New target matrix generated.")
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
