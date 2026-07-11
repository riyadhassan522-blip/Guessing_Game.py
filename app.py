# app.py
import streamlit as st

st.set_page_config(page_title="Lord's Arcade Realm", page_icon="🌸", layout="centered")

# --- Styling and background (keeps frosted look) ---------------------------
def _load_bg_css():
    try:
        import base64, pathlib
        p = pathlib.Path("themes/bg.jpg")
        if p.exists():
            b64 = base64.b64encode(p.read_bytes()).decode()
            bg = f"background-image: linear-gradient(rgba(26,12,18,0.45), rgba(26,12,18,0.65)), url('data:image/jpeg;base64,{b64}');"
        else:
            bg = "background-color: #110b11;"
    except Exception:
        bg = "background-color: #110b11;"

    st.markdown(
        f"""
        <style>
        [data-testid='stAppViewContainer'] {{
            {bg}
            background-size: cover !important;
            background-position: center center !important;
        }}
        .frosted {{
            background: rgba(30,15,23,0.28);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255,102,170,0.18);
            border-radius: 14px;
            padding: 18px;
        }}
        [data-testid='stSidebar'] {{
            background: linear-gradient(rgba(20,10,15,0.35), rgba(20,10,15,0.25));
            backdrop-filter: blur(14px);
            border-right: 3px solid #ff66aa !important;
        }}
        h1,h2,h3,p,label,.stMarkdown,.stMetric,input,button {{
            font-family: 'Courier New', monospace !important;
            font-weight: 700 !important;
            color: #ffffff !important;
        }}
        .main .block-container {{ padding-top: 48px !important; }}
        </style>
        """,
        unsafe_allow_html=True,
    )

_load_bg_css()

# --- Sidebar controls (hub only sets difficulty and deploy flag) ------------
with st.sidebar:
    st.markdown("### 🖥️ SYSTEM SETTINGS")
    difficulty = st.selectbox(
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
    # This flag only indicates the user wants to open the guessing game page.
    if st.button("🎮 DEPLOY CORE MATCH"):
        st.session_state.selected_difficulty = difficulty
        # optional: set a flag so pages can detect the deploy action
        st.session_state.deployed_guessing = True

    st.markdown("---")
    st.markdown("### DASHBOARD STATS")
    gs = st.session_state.get("global_stats", {"played": 0, "wins": 0, "losses": 0, "total_guesses": 0})
    st.write(f"PLAYED MATCH… {gs['played']}")
    st.write(f"TOTAL GUESSES… {gs['total_guesses']}")
    st.write(f"WINS RECORDED… {gs['wins']}")
    st.write(f"CRASH LOSSES… {gs['losses']}")

# --- Main hub UI (clean, no game UI here) ----------------------------------
st.markdown("<div class='frosted'>", unsafe_allow_html=True)
st.markdown("### 🌸 LORD'S ARCADE REALM 🌸")
st.markdown("[ SYSTEM CORE MODULES // CHIEF ENGINEER: LORDDARKNESS393 ]")
st.markdown("---")
st.subheader("STATUS // PLATFORM IDLE")
st.write("Initialize the left matrix panel to deploy your first gameplay module round!")
st.markdown("---")
st.markdown("<div style='text-align:center; color:#ff66aa; font-weight:900;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
