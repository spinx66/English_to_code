import streamlit as st
from components import ui
import os

# Load CSS
with open(os.path.join("components", "style.css")) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# UI Flow
ui.render_header()
user_input = ui.render_input_section()
language = ui.render_language_selector()
if ui.render_transform_button():
    st.info("⚙️ Code transformation will appear here soon.")
ui.render_output_placeholder()
