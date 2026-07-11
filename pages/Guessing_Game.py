# pages/Guessing_Game.py
import streamlit as st
import random

PAGE_TITLE = "🎯 RADAR SCANNER"

LIVES_DEFAULT = 8
RANGE_DEFAULT = (1, 20)

def _init_state():
    if "games" not in st.session_state:
        st.session_state.games = {}
    game = st.session_state.games.setdefault("guessing", {})
    game.setdefault("target", random.randint(*RANGE_DEFAULT))
    game.setdefault("lives", LIVES_DEFAULT)
    game.setdefault("range", list(RANGE_DEFAULT))
    game.setdefault("stats", {"played": 0, "wins": 0, "losses": 0, "total_guesses": 0})
    game.setdefault("message", "")
    game.setdefault("last_guess", None)

def _save_game(game):
    st.session_state.games["guessing"] = game

def reset_round(game):
    game["target"] = random.randint(*game["range"])
    game["lives"] = LIVES_DEFAULT
    game["last_guess"] = None
    game["message"] = ""
    _save_game(game)

def submit_guess(game, guess: int):
    game["last_guess"] = guess
    game["stats"]["total_guesses"] += 1
    if guess == game["target"]:
        game["message"] = f"🎉 Correct! The number was {game['target']}."
        game["stats"]["wins"] += 1
        game["stats"]["played"] += 1
        reset_round(game)
    else:
        game["lives"] -= 1
        if game["lives"] <= 0:
            game["message"] = f"💥 Out of lives. The number was {game['target']}."
            game["stats"]["losses"] += 1
            game["stats"]["played"] += 1
            reset_round(game)
        else:
            hint = "higher" if guess < game["target"] else "lower"
            game["message"] = f"Try {hint}. Lives left: {game['lives']}"
    _save_game(game)

def app():
    _init_state()
    game = st.session_state.games["guessing"]

    st.markdown("<div class='frosted'>", unsafe_allow_html=True)
    st.header("🎯 RADAR SCANNER")
    st.subheader(f"Core Integrity: {game['lives']} / {LIVES_DEFAULT} Lives Remaining")

    # difficulty selector (affects range and lives)
    with st.expander("Difficulty"):
        diff = st.selectbox("Select difficulty", ["Novice", "Normal", "Hard"], index=0, key="guess_diff")
        if diff == "Novice":
            game["range"] = [1, 20]
            game["lives"] = 8
        elif diff == "Normal":
            game["range"] = [1, 50]
            game["lives"] = 6
        else:
            game["range"] = [1, 100]
            game["lives"] = 4
        _save_game(game)

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
    st.sidebar.header("SYSTEM SETTINGS")
    if st.sidebar.button("🎮 DEPLOY CORE MATCH"):
        reset_round(game)
        st.success("Core match deployed. New target generated.")

    st.sidebar.markdown("### DASHBOARD STATS (Guessing)")
    stats = game["stats"]
    st.sidebar.write(f"Played Matches: {stats['played']}")
    st.sidebar.write(f"Total Guesses: {stats['total_guesses']}")
    st.sidebar.write(f"Wins Recorded: {stats['wins']}")
    st.sidebar.write(f"Crash Losses: {stats['losses']}")

    st.markdown("</div>", unsafe_allow_html=True)
