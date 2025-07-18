import streamlit as st
from components import ui
from core.logic import english_to_code
import os

# Load custom CSS
with open(os.path.join("components", "style.css")) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# UI
ui.render_header()
user_input = ui.render_input_section()
language = ui.render_language_selector()

# Action
if ui.render_transform_button():
    if user_input.strip():
        with st.spinner("✨ Morphing your logic into code..."):
            result = english_to_code(user_input, language)

            st.markdown("### 🧠 Explanation")
            st.markdown(f"```markdown\n{result['explanation']}\n```")

            st.markdown("### 🧾 Code")
            st.code(result["code"], language=language.lower())

            st.markdown("### 🔍 Summary")
            st.markdown(f"```markdown\n{result['summary']}\n```")
    else:
        st.warning("⚠️ Please enter something to transform.")
