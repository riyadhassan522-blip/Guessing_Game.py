# pages/TicTacToe.py
import streamlit as st

PAGE_TITLE = "🎲 TicTacToe"

def app():
    # minimal placeholder; expand with your UI and per-game state under st.session_state.games["tictactoe"]
    if "games" not in st.session_state:
        st.session_state.games = {}
    st.session_state.games.setdefault("tictactoe", {"stats": {"played":0,"wins":0,"losses":0}})

    st.markdown("<div class='frosted'>", unsafe_allow_html=True)
    st.header("🎲 TicTacToe")
    st.write("TicTacToe placeholder. Implement board UI and game logic here.")
    st.markdown("</div>", unsafe_allow_html=True)
