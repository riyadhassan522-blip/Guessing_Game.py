# app.py
import streamlit as st
import base64
import importlib
import pkgutil

st.set_page_config(page_title="Lord's Arcade Realm", page_icon="🌸", layout="centered")

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
            pages[title] = name
        except Exception:
            continue
    return pages

# Styling and background
bg_b64 = get_base64_image("themes/bg.jpg")
bg_css = (
    f"background-image: linear-gradient(rgba(26,12,18,0.45), rgba(26,12,18,0.65)), url('data:image/jpeg;base64,{bg_b64}');"
    if bg_b64 else "background-color: #110b11;"
)

st.markdown(
    f"""
    <style>
    [data-testid='stAppViewContainer'] {{
        {bg_css}
        background-size: cover !important;
        background-position: center center !important;
    }}
    .frosted {{
        background: rgba(30,15,23,0.28);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,102,170,0.18);
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
    }}
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
    [data-testid='stSidebar'] {{
        background: linear-gradient(rgba(20,10,15,0.35), rgba(20,10,15,0.25));
        backdrop-filter: blur(14px);
        border-right: 3px solid #ff66aa !important;
    }}
    h1,h2,h3,p,label,.stMarkdown,.stMetric,input,button {{
        font-family: 'Courier New', monospace !important;
        color: #ffffff !important;
    }}
    .main .block-container {{ padding-top: 36px !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar navigation and controls
pages = discover_pages("pages")
page_titles = ["🌸 MAIN HUB"] + sorted(pages.keys())

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
    choice = st.radio("Navigate", page_titles, index=0)
    st.markdown("---")
    st.markdown("### DASHBOARD STATS")
    gs = st.session_state.get("global_stats", {"played": 0, "wins": 0, "losses": 0, "total_guesses": 0})
    st.write(f"PLAYED MATCH… {gs['played']}")
    st.write(f"TOTAL GUESSES… {gs['total_guesses']}")
    st.write(f"WINS RECORDED… {gs['wins']}")
    st.write(f"CRASH LOSSES… {gs['losses']}")

# Expose selected difficulty for pages
st.session_state.selected_difficulty = st.session_state.get("hub_difficulty", "Novice (1–20, 8 lives)")

# Main hub content
if choice == "🌸 MAIN HUB":
    st.markdown("<div class='frosted'>", unsafe_allow_html=True)
    st.markdown("<h1 class='hub-title'>🌸 LORD'S ARCADE REALM 🌸</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hub-sub'>[ SYSTEM CORE MODULES // CHIEF ENGINEER: LORDDARKNESS393 ]</p>", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("STATUS // PLATFORM IDLE")
    st.write("Initialize the left matrix panel to deploy your first gameplay module round!")
    st.markdown("---")
    st.markdown("<div style='text-align:center; color:#ff66aa; font-weight:900;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Load selected page from pages package
else:
    module_path = pages.get(choice)
    if module_path:
        try:
            mod = importlib.import_module(module_path)
            if hasattr(mod, "app"):
                mod.app()
            else:
                st.error("Page module found but no app() function defined.")
        except Exception as e:
            st.error("This page failed to load. Check the page module for errors.")
            st.exception(e)
    else:
        st.error("Selected page not found. Ensure the page file exists in pages/ and defines PAGE_TITLE and app().")
