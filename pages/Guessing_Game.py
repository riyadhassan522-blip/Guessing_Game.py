# pages/Guessing_Game.py
import streamlit as st
import random

PAGE_TITLE = "🎯 RADAR SCANNER"

def _init_state(range_vals, lives):
    if "games" not in st.session_state:
        st.session_state.games = {}
    game = st.session_state.games.setdefault("guessing", {})
    game["range"] = range_vals
    game["lives"] = lives
    game.setdefault("target", random.randint(*range_vals))
    game.setdefault("stats", {"played": 0, "wins": 0, "losses": 0, "total_guesses": 0})
    game.setdefault("message", "")
    game.setdefault("last_guess", None)

def reset_round(game):
    game["target"] = random.randint(*game["range"])
    game["lives"] = game["lives"]  # reset lives to difficulty default
    game["last_guess"] = None
    game["message"] = ""

def submit_guess(game, guess: int):
    game["last_guess"] = guess
    game["stats"]["total_guesses"] += 1
    if guess == game["target"]:
        game["message"] = f"🎉 Correct! The number was {game['target']}."
        game["stats"]["wins"] += 1
        game["stats"]["played"] += 1
        gs = st.session_state.get("global_stats", {"played":0,"wins":0,"losses":0,"total_guesses":0})
        gs["played"] += 1; gs["wins"] += 1; gs["total_guesses"] += 1
        st.session_state["global_stats"] = gs
        reset_round(game)
    else:
        game["lives"] -= 1
        if game["lives"] <= 0:
            game["message"] = f"💥 Out of lives. The number was {game['target']}."
            game["stats"]["losses"] += 1
            game["stats"]["played"] += 1
            gs = st.session_state.get("global_stats", {"played":0,"wins":0,"losses":0,"total_guesses":0})
            gs["played"] += 1; gs["losses"] += 1
            st.session_state["global_stats"] = gs
            reset_round(game)
        else:
            hint = "higher" if guess < game["target"] else "lower"
            game["message"] = f"Try {hint}. Lives left: {game['lives']}"

def app():
    # Map difficulty string to range and lives
    diff = st.session_state.get("selected_difficulty", "Novice (1–20, 8 lives)")
    if "Novice" in diff:
        rng, lives = (1,20), 8
    elif "Easy" in diff:
        rng, lives = (1,50), 6
    elif "Normal" in diff:
        rng, lives = (1,100), 5
    elif "Hard" in diff:
        rng, lives = (1,200), 4
    else:  # Expert
        rng, lives = (1,500), 3

    _init_state(rng, lives)
    game = st.session_state.games["guessing"]

    st.markdown("<div class='frosted'>", unsafe_allow_html=True)
    st.header("🎯 RADAR SCANNER")
    st.subheader(f"Core Integrity: {game['lives']} Lives Remaining")

    with st.form("guess_form"):
        col1, col2 = st.columns([3,1])
        with col1:
            guess = st.number_input(
                "Target Scan Range",
                min_value=int(game["range"][0]),
                max_value=int(game["range"][1]),
                value=int(game["range"][0]),
                step=1,
                key="input_guess"
            )
        with col2:
            submit = st.form_submit_button("⭐ SUBMIT SCAN RADAR")
        if submit:
            submit_guess(game, int(guess))

    if game["message"]:
        st.info(game["message"])

    st.markdown("---")
    st.sidebar.markdown("### DASHBOARD STATS (Guessing)")
    stats = game["stats"]
    st.sidebar.write(f"Played Matches: {stats
