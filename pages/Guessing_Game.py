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
    
    # Check if the player altered settings inside the gameplay canvas
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
        game["message"] = f"🎉 Correct! The number was {game['target']}."
        game["stats"]["wins"] += 1
        game["stats"]["played"] += 1
        gs["played"] += 1; gs["wins"] += 1
        st.session_state["global_stats"] = gs
        reset_round(game)
    else:
        game["lives"] -= 1
        if game["lives"] <= 0:
            game["message"] = f"💥 Out of lives. The number was {game['target']}."
            game["stats"]["losses"] += 1
            game["stats"]["played"] += 1
            gs["played"] += 1; gs["losses"] += 1
            st.session_state["global_stats"] = gs
            reset_round(game)
        else:
            hint = "higher" if guess < game["target"] else "lower"
            game["message"] = f"Try {hint}. Lives left: {game['lives']}"
            st.session_state["global_stats"] = gs

def app():
    st.markdown("<div class='frosted'>", unsafe_allow_html=True)
    st.markdown("<h1 class='hub-title'>🎯 RADAR SCANNER MODULE</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # ─── SECTION 1: DIFFICULTY SELECTOR INSIDE THE GAME SCREEN ───
    diff = st.selectbox(
        "⚡ CONFIGURE ENGINE DIFFICULTY",
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
    
    st.write(f"**Target Threshold Range:** {game['range'][0]} to {game['range'][1]}")
    st.write(f"**Core Integrity status:** {game['lives']} / {game['default_lives']} Units Remaining")
    st.markdown("---")

    # ─── SECTION 2: GAMEPLAY INPUT FIELD ───
    with st.form("guess_form", clear_on_submit=False):
        col1, col2 = st.columns([3, 1])
        with col1:
            guess = st.number_input(
                "Input Coordinate Matrix Guess:",
                min_value=int(game["range"][0]),
                max_value=int(game["range"][1]),
                value=int(game["range"][0]),
                step=1,
                key="input_guess"
            )
        with col2:
            st.write("<br>", unsafe_allow_html=True)
            submit = st.form_submit_button("⭐ EXECUTE SCAN")
            
        if submit:
            submit_guess(game, int(guess))
            st.rerun()

    if game["message"]:
        if "Correct" in game["message"]:
            st.success(game["message"])
        elif "Out of lives" in game["message"]:
            st.error(game["message"])
        else:
            st.info(game["message"])

    st.markdown("---")
    
    # ─── SECTION 3: METRICS SCOREBOARD INSIDE THE GAME SCREEN ───
    st.markdown("<h3 style='color:#ff66aa; text-align:center; font-size:18px;'>📊 MODULE SCOREBOARD</h3>", unsafe_allow_html=True)
    stats = game["stats"]
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="MATCHES PLAYED", value=stats['played'])
        st.metric(label="TOTAL SCANS", value=stats['total_guesses'])
    with col_b:
        st.metric(label="WINS CONFIRMED", value=stats['wins'])
        st.metric(label="CRASH LOSSES", value=stats['losses'])

    st.write("")
    if st.button("🎮 RESTART SYSTEM ROUND"):
        reset_round(game)
        st.toast("Core match restarted. New target matrix generated.")
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
