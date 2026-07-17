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
    
    # Check if the player changed difficulty setting in the sidebar
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
    
    # Sync with global stats tracker
    gs = st.session_state.get("global_stats", {"played":0,"wins":0,"losses":0,"total_guesses":0})
    gs["total_guesses"] += 1
    
    if guess == game["target"]:
        game["message"] = f"🎉 Correct! The number was {game['target']}."
        game["stats"]["wins"] += 1
        game["stats"]["played"] += 1
        gs["played"] += 1
        gs["wins"] += 1
        st.session_state["global_stats"] = gs
        reset_round(game)
    else:
        game["lives"] -= 1
        if game["lives"] <= 0:
            game["message"] = f"💥 Out of lives. The number was {game['target']}."
            game["stats"]["losses"] += 1
            game["stats"]["played"] += 1
            gs["played"] += 1
            gs["losses"] += 1
            st.session_state["global_stats"] = gs
            reset_round(game)
        else:
            hint = "higher" if guess < game["target"] else "lower"
            game["message"] = f"Try {hint}. Lives left: {game['lives']}"
            st.session_state["global_stats"] = gs

def app():
    # Read chosen values from sidebar dropdown
    diff = st.session_state.get("selected_difficulty", "Novice (1–20, 8 lives)")
    rng, lives = _difficulty_to_params(diff)

    game = _init_state(rng, lives)

    st.markdown("<div class='frosted'>", unsafe_allow_html=True)
    st.header("🎯 RADAR SCANNER")
    st.write(f"**Difficulty Setting:** {diff}")
    st.write(f"**Core Integrity:** {game['lives']} / {game['default_lives']} Lives Remaining")
    st.markdown("---")

    with st.form("guess_form", clear_on_submit=False):
        col1, col2 = st.columns([3, 1])
        with col1:
            guess = st.number_input(
                f"Enter Scan Matrix ({game['range'][0]}–{game['range'][1]}):",
                min_value=int(game["range"][0]),
                max_value=int(game["range"][1]),
                value=int(game["range"][0]),
                step=1,
                key="input_guess"
            )
        with col2:
            st.write("<br>", unsafe_allow_html=True) # visual spacer
            submit = st.form_submit_button("⭐ SUBMIT SCAN")
            
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
    
    # Local Module Stats Panel (Moved safely inside main content screen)
    st.subheader("📊 CURRENT MODULE PERFORMANCE")
    c1, c2, c3, c4 = st.columns(4)
    stats = game["stats"]
    c1.metric("Played", stats['played'])
    c2.metric("Guesses", stats['total_guesses'])
    c3.metric("Wins", stats['wins'])
    c4.metric("Losses", stats['losses'])

    st.write("")
    if st.button("🎮 RESTART CURRENT ROUND"):
        reset_round(game)
        st.toast("Core match restarted. New target generated.")
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
