from components import ui
from core.logic import english_to_code
import os
import streamlit as st
import re

# Load custom CSS
with open(os.path.join("components", "style.css")) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# UI
ui.render_header()
user_input = ui.render_input_section()
language = ui.render_language_selector()

if ui.render_transform_button():
    if user_input.strip():
        with st.spinner("✨ Morphing your logic into code..."):
            raw_output = english_to_code(user_input, language)

            # Extract Explanation, Code, Summary using regex
            explanation = re.search(r"🧠 Explanation\n(.+?)\n\n", raw_output, re.DOTALL)
            code = re.search(r"🧾 Code\n(.+?)\n\n", raw_output, re.DOTALL)
            summary = re.search(r"🔍 Summary\n(.+)", raw_output, re.DOTALL)

            if explanation:
                st.markdown("### 🧠 Explanation")
                st.markdown(explanation.group(1).strip())

            if code:
                st.markdown("### 🧾 Code")
                st.code(code.group(1).strip(), language=language.lower())

            if summary:
                st.markdown("### 🔍 Summary")
                st.markdown(summary.group(1).strip())
    else:
        st.warning("⚠️ Please enter something to transform.")
