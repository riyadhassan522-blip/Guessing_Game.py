import streamlit as st
import base64
import importlib
import pkgutil
from sidebar import render_sidebar

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
        if name.endswith(".__init__"):
            continue
        try:
            mod = importlib.import_module(name)
            title = getattr(mod, "PAGE_TITLE", None) or name.split(".")[-1].replace("_", " ").upper()
            pages[title] = name
        except Exception:
            continue
    return pages

# Initialize statistics
if "global_stats" not in st.session_state:
    st.session_state["global_stats"] = {"played": 0, "wins": 0, "losses": 0, "total_guesses": 0}

# Discover items and store them for the sidebar to see
discovered_pages = discover_pages("pages")
st.session_state["page_titles"] = ["🌸 MAIN HUB"] + sorted(discovered_pages.keys())

# Apply UI styles
bg_b64 = get_base64_image("themes/bg.jpg")
bg_css = f"background-image: linear-gradient(rgba(26,12,18,0.45), rgba(26,12,18,0.65)), url('data:image/jpeg;base64,{bg_b64}');" if bg_b64 else "background-color: #110b11;"

st.markdown(
    f"""
    <style>
    /* Main App Layout */
    [data-testid='stAppViewContainer'] {{ 
        {bg_css} 
        background-size: cover !important; 
        background-position: center center !important; 
    }}
    
    /* Center Game Canvas Container */
    .frosted {{ 
        background: rgba(30,15,23,0.28); 
        backdrop-filter: blur(12px); 
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255,102,170,0.18); 
        border-radius: 14px; 
        padding: 22px; 
        margin-bottom: 18px; 
    }}
    
    .hub-title {{ text-align: center; color: #ff66aa; font-family: 'Courier New', monospace; font-weight: 900; font-size: 28px; margin: 0; padding: 0; }}
    .hub-sub {{ text-align: center; color: #ffffff; font-family: 'Courier New', monospace; font-weight: 700; margin-top: 6px; margin-bottom: 0; }}
    
    /* THE GLASSMORPHIC SIDEBAR */
    [data-testid='stSidebar'] {{ 
        background-color: transparent !important;
        border-right: 3px solid #ff66aa !important; 
    }}
    
    [data-testid='stSidebarContent'] {{
        background: rgba(30, 15, 23, 0.35) !important; 
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        box-shadow: inset -10px 0 20px rgba(0,0,0,0.2);
    }}
    
    h1, h2, h3, p, label, .stMarkdown, .stMetric, input, button, span, div {{ 
        font-family: 'Courier New', monospace !important; 
        color: #ffffff !important; 
    }}
    
    .main .block-container {{ padding-top: 36px !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Run sidebar UI and capture choice
choice = render_sidebar()

# Create a clean, single rendering container block for the main window frame
main_canvas = st.empty()

# Run application states inside the container block to kill the double-arrow bug
with main_canvas.container():
    if choice == "🌸 MAIN HUB":
        st.markdown("<div class='frosted'>", unsafe_allow_html=True)
        st.markdown("<h1 class='hub-title'>🌸 RADAR NUMBER SCANNER 🌸</h1>", unsafe_allow_html=True)
        st.markdown("<p class='hub-sub'>[ SYSTEM CORE MODULES // CHIEF ENGINEER: LORDDARKNESS393 ]</p>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("<h3 style='color:#ff66aa; text-align:center;'>STATUS // PLATFORM IDLE</h3>", unsafe_allow_html=True)
        st.write("Initialize the left matrix panel to deploy your first gameplay module round!")
        st.markdown("---")
        st.markdown("<div style='text-align:center; color:#ff66aa; font-weight:900;'>DESIGNED & ENGINEERED BY LORDDARKNESS393</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        module_path = discovered_pages.get(choice)
        if module_path:
            try:
                # Force dynamic module reloading to clear stale visual states
                if module_path in importlib.sys.modules:
                    importlib.reload(importlib.sys.modules[module_path])
                mod = importlib.import_module(module_path)
                
                if hasattr(mod, "app"):
                    mod.app()
                else:
                    st.error("Page module found but no app() function defined.")
            except Exception as e:
                st.error("This page failed to load. Check the page module for errors.")
                st.exception(e)
