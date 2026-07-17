import streamlit as st

def render_sidebar():
    """Compiles and renders the primary arcade dashboard interface."""
    with st.sidebar:
        st.markdown("### 🖥️ SYSTEM SETTINGS")
        
        # Difficulty selection engine
        st.selectbox(
            "Select Difficulty",
            [
                "Novice (1–20, 8 lives)",
                "Easy (1–50, 6 lives)",
                "Normal (1–100, 5 lives)",
                "Hard (1–200, 4 lives)",
                "Expert (1–500, 3 lives)"
            ],
            index=0,
            key="hub_difficulty"
        )
        
        # Pull global page data from routing array
        page_titles = st.session_state.get("page_titles", ["🌸 MAIN HUB"])
        choice = st.radio("Navigate", page_titles, index=0, key="nav_choice")
        
        st.markdown("---")
        st.markdown("### DASHBOARD STATS")
        gs = st.session_state.get("global_stats", {"played": 0, "wins": 0, "losses": 0, "total_guesses": 0})
        st.write(f"PLAYED MATCH… {gs['played']}")
        st.write(f"TOTAL GUESSES… {gs['total_guesses']}")
        st.write(f"WINS RECORDED… {gs['wins']}")
        st.write(f"CRASH LOSSES… {gs['losses']}")
        
    return choice
