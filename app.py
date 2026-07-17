import streamlit as st
import random

# Tells app.py what to label this link in your menu list
PAGE_TITLE = "🕹️ GUESSING GAME"

def app():
    st.markdown("<div class='frosted'>", unsafe_allow_html=True)
    st.markdown("<h2 class='hub-title'>🔢 NUMBER GUESSING MODULE</h2>", unsafe_allow_html=True)
    st.write("System connected. Initializing user parameters...")
    st.markdown("---")
    
    # Reads the active difficulty setting from your sidebar selectbox
    selected_diff = st.session_state.get("hub_difficulty", "Novice (1–20, 8 lives)")
    st.info(f"Active Difficulty Engine: {selected_diff}")
    
    # ---------------------------------------------------------
    # PASTE YOUR REAL GAMEPLAY CODE / GUESS INPUTS BELOW HERE
    # ---------------------------------------------------------
    
    st.markdown("</div>", unsafe_allow_html=True)
