import streamlit as st
import random
import base64
import time

st.set_page_config(page_title="Number Scanner Radar", page_icon="🎯", layout="centered")

if "gg_played" not in st.session_state:
    st.session_state.gg_played = 0
    st.session_state.gg_wins = 0
    st.session_state.gg_losses = 0
    st.session_state.gg_total_guesses = 0
    st.session_state.gg_best_score = None
    st.session_state.gg_active = False
    st.session_state.gg_current_difficulty = None

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file: return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError: return ""

bg_base64 = get_base64_image("themes/bg.jpg")

def trigger_arcade_synth():
    st.markdown("""<audio autoplay style="display:none;"><source src="data:audio/wav;base64,UklGRigAAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQQAAAAAf39/fw==" type="audio/wav"></audio>""", unsafe_allow_html=True)

css_style = f"""
<style>
.stApp, [data-testid='stAppViewContainer'], .stAppHeader, [data-testid='stHeader'] {{
    background-image: linear-gradient(rgba(26, 12, 18, 0.45), rgba(26, 12, 18, 0.65)), url("data:image/jpeg;base64,{bg_base64}") !important;
    background-size: cover !important; background-position: center center !important; background-attachment: fixed !important;
}}

/* SAFE ARCHITECTURAL TYPOGRAPHY: Forces your clean arcade monospace layout without corrupting Streamlit's icon engines */
h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stMetric, input, button, .stForm {{
    font-family: 'Courier New', Courier, monospace !important;
    font-weight: bold !important;
}}

/* THE GLORIOUS FROSTED GLASS SIDEBAR AREA (Fully visible and functioning) */
[data-testid='stSidebar'], [data-testid='stSidebarUserContent'], section[data-testid='stSidebar'] > div:first-child {{ 
    background-color: rgba(30, 15, 23, 0.25) !important; 
    backdrop-filter: blur(16px) !important; 
    -webkit-backdrop-filter: blur(16px) !important;
    border-right: 3px solid #ff66aa !important; 
    display: block !important;
    visibility: visible !important;
}}
[data-testid="stSidebarNav"] {{
    display: block !important;
    visibility: visible !important;
}}
[data-testid="stSidebarNav"] ul {{ background-color: rgba(37, 22, 31, 0.70) !important; border-radius: 8px !important; border: 1px solid rgba(255, 102, 170, 0.4) !important; padding: 10px !important; }}
[data-testid="stSidebarNav"] span {{ color: #ffffff !important; }}

/* FLOATING COUNTER CARDS COMPONENT HOUSING */
div[data-testid='stForm'], .stMainBlockContainer div[data-testid='stVerticalBlock'] > div[style*="border"] {{
    background-color: rgba(37, 22, 31, 0.45) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 2px solid rgba(255, 102, 170, 0.4) !important;
    border-radius: 24px !important;
    padding: 30px !important;
    box-shadow: 0px 8px 32px rgba(255, 102, 170, 0.15) !important;
    margin-bottom: 25px !important;
}}
.stMainBlockContainer {{ background: transparent !important; padding: 0 !important; max-width: 100% !important; }}

.main .block-container {{
    padding-top: 50px !important;
}}

div.stButton > button:first-child {{
    background: #ff66aa !important; color: #1a0c12 !important; border: 3px solid #1a0c12 !important; font-weight: 900 !important;
    font-size: 1.1rem !important; text-transform: uppercase !important; letter-spacing: 2px !important; border-radius: 8px !important;
    box-shadow: 0px 6px 0px #992255 !important; transition: all 0.1s ease-in-out !important; width: 100% !important;
}}
div.stButton > button:first-child:active {{ transform: translateY(4px) !important; box-shadow: 0px 2px 0px #992255 !important; }}
div[data-testid="stTextInput"] [data-baseweb="input"] {{ background-color: rgba(37, 22, 31, 0.90) !important; border: 2px solid rgba(255, 102, 170, 0.5) !important; border-radius: 8px !important; }}
div[data-testid="stTextInput"] input {{ background-color: transparent !important; color: #ff66aa !important; font-size: 1.1rem !important; }}
div[data-testid="stTextInput"] [data-baseweb="input"] + div {{ display: none !important; }}
div[data-testid='stMetricValue'] {{ font-weight: 900 !important; color: #ff66aa !important; text-shadow: 2px 2px 0px #1a0c12 !important; font-size: 1.6rem !important; }}

/* 🚨 THE TRUE TEXT ELIMINATOR: Hard-deletes the broken top header toggle buttons completely from the page node structure */
[data-testid="stHeader"], .stAppHeader, [data-testid="collapsedControl"] {{
    display: none !important;
    visibility: hidden !important;
    height: 0px !important;
    opacity: 0 !important;
}}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

st.markdown("<div style='background-color: rgba(45, 20, 32, 0.40); backdrop-filter: blur(10px); padding: 25px; border-radius: 16px; text-align: center; border: 1px solid rgba(255, 102, 170, 0.25); box-shadow: 0px 4px 15px rgba(255, 102, 170, 0.1); margin-bottom: 35px;'><h1 style='color: #ff66aa; margin: 0; font-family: \"Courier New\", monospace; font-size: 2.3rem; letter-spacing: 2px; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>🌸 RADAR NUMBER SCANNER 🌸</h1></div>", unsafe_allow_html=True)
with st.sidebar:
    st.markdown("### ⚙️ SYSTEM SETTINGS")
    difficulty = st.selectbox("Select Rank Boundary:", ["1. Novice (1-20, 8 lives)", "2. Easy (1-50, 10 lives)", "3. Medium (1-100, 7 lives)", "4. Hard (1-200, 5 lives)", "5. Expert (1-500, 3 lives)"])
    if "1." in difficulty: max_lives, max_range = 8, 20
    elif "2." in difficulty: max_lives, max_range = 10, 50
    elif "3." in difficulty: max_lives, max_range = 7, 100
    elif "4." in difficulty: max_lives, max_range = 5, 200
    else: max_lives, max_range = 3, 500

    if st.button("🚀 DEPLOY CORE MATCH", use_container_width=True, type="primary"):
        with st.spinner("🔄 SYNCING MAINFRAME..."): time.sleep(1.2); trigger_arcade_synth()
        st.session_state.gg_secret_number = random.randint(1, max_range)
        st.session_state.gg_lives_left = max_lives
        st.session_state.gg_round_attempts = 0
        st.session_state.gg_active = True
        st.session_state.gg_current_difficulty = difficulty
        st.session_state.gg_feedback = "🎯 SYSTEM ENGINE LOADED. DISPATCH YOUR FIRST GUESS ANALYSIS."
        st.session_state.gg_feedback_type = "info"

    st.markdown("---")
    st.markdown("### 📊 DASHBOARD STATS")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="PLAYED MATCHES", value=st.session_state.gg_played)
        st.metric(label="WINS RECORDED 🏆", value=st.session_state.gg_wins)
    with col2:
        st.metric(label="TOTAL GUESSES", value=st.session_state.gg_total_guesses)
        st.metric(label="CRASH LOSSES 💀", value=st.session_state.gg_losses)
    st.markdown("---")
    best_display = f"{st.session_state.gg_best_score} attempts" if st.session_state.gg_best_score else "No wins recorded"
    st.markdown(f"<p style='color: #ff66aa; font-family: monospace; font-size: 0.85rem; font-weight: bold; margin-top: 15px;'>🏆 BEST RECORD: <span style='color: #ffffff;'>{best_display}</span></p>", unsafe_allow_html=True)

if st.session_state.gg_active:
    with st.container(border=True):
        st.markdown(f"##### 🌸 Core Integrity: **{st.session_state.gg_lives_left} / {max_lives} Lives Remaining**")
        st.progress(float(min(1.0, max(0, st.session_state.gg_lives_left) / max_lives)))
    st.markdown(" ")
    with st.form(key="guess_form", clear_on_submit=True):
        guess_input = st.text_input(f"Target Scan Range [1 to {max_range}]:", value="", placeholder="Type your number analysis here and click submit...")
        submit_guess = st.form_submit_button("💥 SUBMIT SCAN RADAR", use_container_width=True)

    if submit_guess and guess_input.strip().isdigit():
        guess = int(guess_input.strip())
        trigger_arcade_synth()
        st.session_state.gg_round_attempts += 1
        st.session_state.gg_total_guesses += 1
        warm_threshold = max(3, max_range // 15)
        secret = st.session_state.gg_secret_number

        if guess < secret:
            st.session_state.gg_lives_left -= 1
            msg = f"📉 {guess} is Too Low!"
            if secret - guess <= warm_threshold: msg += " 👉 Radar signature getting warm!!"
            st.session_state.gg_feedback, st.session_state.gg_feedback_type = msg, "warning"
        elif guess > secret:
            st.session_state.gg_lives_left -= 1
            msg = f"📈 {guess} is Too High!"
            if guess - secret <= warm_threshold: msg += " 👉 Radar signature getting warm!!"
            st.session_state.gg_feedback, st.session_state.gg_feedback_type = msg, "warning"
        else:
            st.session_state.gg_feedback = f"🎉 MAINFRAME ACCESS SECURED! Encryption cracked in {st.session_state.gg_round_attempts} attempts!"
            st.session_state.gg_feedback_type = "success"
            st.session_state.gg_wins += 1; st.session_state.gg_played += 1
            if st.session_state.gg_best_score is None or st.session_state.gg_round_attempts < st.session_state.gg_best_score:
                st.session_state.gg_best_score = st.session_state.gg_round_attempts
                st.toast("🌸 NEW MAINFRAME CORE SPEED-RECORD SET! 🌸")
            st.session_state.gg_active = False

        if st.session_state.gg_lives_left <= 0 and st.session_state.gg_active:
            st.session_state.gg_feedback = f"💀 PROTOCOL ABORTED! System crashed. Core signature code was: {secret}."
            st.session_state.gg_feedback_type = "error"
            st.session_state.gg_losses += 1; st.session_state.gg_played += 1
            st.session_state.gg_active = False
    elif submit_guess:
        st.session_state.gg_feedback, st.session_state.gg_feedback_type = "⚠️ INVALID TRANSMISSION! Input raw numbers sequence inside scanner channel.", "error"

    if "gg_feedback" in st.session_state:
        if st.session_state.gg_feedback_type == "success": st.success(st.session_state.gg_feedback)
        elif st.session_state.gg_feedback_type == "warning": st.warning(st.session_state.gg_feedback)
        elif st.session_state.gg_feedback_type == "error": st.error(st.session_state.gg_feedback)
        else: st.info(st.session_state.gg_feedback)
else:
    st.markdown("<div style='text-align: center; padding: 40px 20px; background-color: rgba(45, 20, 32, 0.40); backdrop-filter: blur(10px); border: 4px dashed #ff66aa; box-shadow: 0px 4px 15px rgba(255, 102, 170, 0.15);'><p style='font-size: 1.3rem; color: #ff66aa; font-weight: 900; letter-spacing: 1px; text-shadow: 1px 1px 0px #1a0c12;'>STATUS // PLATFORM IDLE</p><p style='font-size: 0.95rem; color: #ffffff; font-weight: bold; margin-top: 10px;'>Initialize the left matrix panel to deploy your first gameplay module round!</p></div>", unsafe_allow_html=True)

footer_html = "<div style='text-align: center; padding: 10px; margin-top: 30px;'><p style='color: #614653; font-family: \"Courier New\", monospace; font-size: 0.85rem; margin: 0; font-weight: bold;'>© 2026 DARKNESS GAMING LABS | ALL RIGHTS RESERVED</p></div>"
st.markdown("---"); st.markdown(footer_html, unsafe_allow_html=True)
