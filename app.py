# app.py
import streamlit as st
import base64
import importlib
import pkgutil

st.set_page_config(page_title="Lord's Arcade Realm", page_icon="🌸", layout="centered")

# --- helpers ---------------------------------------------------------------
def get_base64_image(path: str):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return None

def discover_pages(package_name: str = "pages"):
    pages = {}
    try:
        package = importlib.import_module(package_name)
    except Exception:
        return pages
    prefix = package.__name__ + "."
    for finder, name, ispkg in pkgutil.iter_modules(package.__path__, prefix):
        try:
            mod = importlib.import_module(name)
            title = getattr(mod, "PAGE_TITLE", None) or name.split(".")[-1]
            pages[title] = name  # store module path string
        except Exception:
            continue
    return pages

# --- styling ---------------------------------------------------------------
bg_b64 = get_base64_image("themes/bg.jpg")
bg_css = (
    f"background-image: linear-gradient(rgba(26,12,18,0.45), rgba(26,12,18,0.65)), url('data:image/jpeg;base64,{bg_b64}');"
    if bg_b64 else "background-color: #110b11;"
)

st.markdown(
    f"""
    <style>
    /* background */
    [data-testid='stAppViewContainer'] {{
        {bg_css}
        background-size: cover !important;
        background-position: center center !important;
    }}

    /* frosted glass container */
    .frosted {{
        background: rgba(30,15,23,0.28);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,102,170,0.18);
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
    }}

    /* centered header */
    .hub-title {{
        text-align: center;
        color: #ff66aa;
        font-family: 'Courier New', monospace;
        font-weight: 900;
        font-size: 28px;
        margin: 0;
        padding: 0;
    }}
    .hub-sub {{
        text-align: center;
        color: #ffffff;
        font-family: 'Courier New', monospace;
        font-weight: 700;
        margin-top: 6px;
        margin-bottom: 0;
    }}

    /* sidebar frosted */
    [data-testid='stSidebar'] {{
        background: linear-gradient(rgba(20,10,15,0.35), rgba(20,10,15,0.25));
        backdrop-filter: blur(14px);
        border-right: 3px solid #ff66aa !important;
    }}

    /* general text */
    h1,h2,h3,p,label,.stMarkdown,.stMetric,input,button {{
        font-family: 'Courier New', monospace !important;
        color: #ffffff !important;
    }}

    .main .block-container {{ padding-top: 36px !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- sidebar navigation and controls --------------------------------------
pages = discover_pages("pages")
page_titles = ["🌸 MAIN HUB"] + sorted(pages.keys())

with st.sidebar:
    st.markdown("### 🖥️ SYSTEM SETTINGS")
    # difficulty selector stored in session so pages can read it
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
    # navigation radio (keeps hub clean until user selects a page)
    choice = st.radio("Navigate", page_titles, index=0)
    st.markdown("---")
    st.markdown("### DASHBOARD STATS")
    gs = st.session_state.get("global_stats", {"played": 0, "wins": 0, "losses": 0, "total_guesses": 0})
    st.write(f"PLAYED MATCH… {gs['played']}")
    st.write(f"TOTAL GUESSES… {gs['total_guesses']}")
    st.write(f"WINS RECORDED… {gs['wins']}")
    st.write(f"CRASH LOSSES… {gs['losses']}")

# store selected difficulty for pages to read
st.session_state.selected_difficulty = st.session_state.get("hub_difficulty", "Novice (1–20, 8 lives)")

# --- main hub
