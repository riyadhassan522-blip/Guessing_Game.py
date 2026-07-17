import streamlit as st

def render_sidebar():
    """Renders an ultra-clean sidebar navigation interface."""
    with st.sidebar:
        st.markdown("<h2 style='color:#ff66aa; font-size:22px; font-weight:900;'>🎛️ CORE MATRIX</h2>", unsafe_allow_html=True)
        st.markdown("---")
        
        # Pull dynamic page data from routing array
        page_titles = st.session_state.get("page_titles", ["🌸 MAIN HUB"])
        
        # Display the page router selection
        choice = st.radio("Deploy Module Link:", page_titles, index=0, key="nav_choice", label_visibility="collapsed")
        
        st.markdown("---")
        st.markdown("<div style='font-size:11px; text-align:center; color:#ff66aa;'>[ HUB READY // ONLINE ]</div>", unsafe_allow_html=True)
        
    return choice
