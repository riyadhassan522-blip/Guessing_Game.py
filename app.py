# app.py
import streamlit as st
import base64
import importlib
import pkgutil
from typing import Callable, Dict

st.set_page_config(page_title="Lord's Arcade Realm", page_icon="🌸", layout="centered")

def get_base64_image(path: str):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return None

def discover_pages(package_name: str = "pages") -> Dict[str, Callable]:
    pages = {}
    try:
        package = importlib.import_module(package_name)
    except Exception:
        return pages
    prefix = package.__name__ + "."
    for finder, name, ispkg in pkgutil.iter_modules(package.__path__, prefix):
        try:
            mod = importlib.import_module(name)
            app_fn = getattr(mod, "app", None)
            if callable(app_fn):
                title = getattr(mod, "PAGE_TITLE", None) or getattr(mod, "PAGE_NAME", None) or name.split(".")[-1]
                pages[title] = app_fn
        except Exception:
            continue
    return pages

# Styling and frosted glass background
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

st.markdown(
    """
    <div class="frosted" style="text-align:center; margin-bottom:18px;">
      <h1 style="color:#ff66aa; margin:0;">🌸 LORD'S ARCADE REALM 🌸</h1>
      <p style="margin:6px 0 0 0; color:#fff;">[ SYSTEM CORE MODULES // CHIEF ENGINEER: LORDDARKNESS393 ]</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### 🖥️ DIAGNOSTIC CORE")
    st.markdown("● **STATUS:** `ONLINE` ⚡")
    st.markdown("● **ENGINES:** `01 MODULE` 💾")
    st.markdown("---")

pages = discover_pages("pages")
nav_options = ["🌸 MAIN LOBBY"] + sorted(pages.keys())
choice = st.sidebar.radio("Navigate", nav_options)

if choice == "🌸 MAIN LOBBY":
    st.markdown("<div class='frosted'>", unsafe_allow_html=True)
    st.markdown("### 🕹️ LOBBY TERMINAL HUB ONLINE")
    st.markdown("---")
    st.markdown("Your retro gaming console framework has been successfully updated and re-aligned to full cross-platform glass dictionary specs.")
    st.info("💡 TRANSMISSION PANEL: Use the left-side drawer to deploy your game channels.")
    global_stats = st.session_state.get("global_stats", {"played": 0, "wins": 0, "losses": 0, "total_guesses": 0})
    cols = st.columns(4)
    cols[0].metric("Played", global_stats["played"])
    cols[1].metric("Wins", global_stats["wins"])
    cols[2].metric("Losses", global_stats["losses"])
    cols[3].metric("Guesses", global_stats["total_guesses"])
    st.markdown("---")
    st.markdown("<div style='text-align:center; color:#ff66aa; font-weight:900;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    page_fn = pages.get(choice)
    if page_fn:
        try:
            page_fn()
        except Exception as e:
            st.error("This page failed to load. Check the page module for errors.")
            st.exception(e)
    else:
        st.error("Selected page not found. Make sure the page module defines `app()` and is inside the pages package.")
