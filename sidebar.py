import streamlit as st

def render_sidebar():
    """Renders the standard system metrics and configuration selectors."""
    with st.sidebar:
        # ─── SECTION 1: SYSTEM CORE HEADER ──────────────────────────────
        st.markdown("<h2 style='color:#ff66aa; font-size:22px; font-weight:900;'>🎛️ CORE MATRIX</h2>", unsafe_allow_html=True)
        st.markdown("---")
        
        # ─── SECTION 2: APPLICATION NAVIGATION TABS ─────────────────────
        st.markdown("<h3 style='color:#ffffff; font-size:16px;'>📂 SYSTEM NAVIGATION</h3>", unsafe_allow_html=True)
        page_titles = st.session_state.get("page_titles", ["🌸 MAIN HUB"])
        choice = st.radio("Deploy Module Link:", page_titles, index=0, key="nav_choice", label_visibility="collapsed")
        st.markdown("---")
        
        # ─── SECTION 3: PARAMETER ADJUSTMENT INPUTS ─────────────────────
        st.markdown("<h3 style='color:#ffffff; font-size:16px;'>⚙️ ENGINE PARAMETERS</h3>", unsafe_allow_html=True)
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
        st.markdown("---")
        
        # ─── SECTION 4: REAL-TIME ANALYTICS DASHBOARD ───────────────────
        st.markdown("<h3 style='color:#ff66aa; font-size:16px;'>📊 TOTAL REALM ANALYTICS</h3>", unsafe_allow_html=True)
        gs = st.session_state.get("global_stats", {"played": 0, "wins": 0, "losses": 0, "total_guesses": 0})
        
        # Using columns to create a balanced horizontal data layout inside the sidebar
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="MATCHES", value=gs['played'])
            st.metric(label="WINS", value=gs['wins'])
        with col2:
            st.metric(label="GUESSES", value=gs['total_guesses'])
            st.metric(label="LOSSES", value=gs['losses'])
            
        st.markdown("---")
        st.markdown("<div style='font-size:11px; text-align:center; color:#ff66aa;'>[ HUB READY // ONLINE ]</div>", unsafe_allow_html=True)
        
    return choice
