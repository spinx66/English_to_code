import streamlit as st

def render_header():
    st.markdown("<h1 class='title'>🧠 CodeMorph</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Transform your thoughts into real code — no syntax stress.</p>", unsafe_allow_html=True)
    st.markdown("---")

def render_input_section():
    st.markdown("### 💬 Describe your logic")
    return st.text_area("Your English input here:", key="input_text", height=150, label_visibility="collapsed")

def render_language_selector():
    return st.selectbox("Language", ["JavaScript", "Python"], key="lang_select")

def render_transform_button():
    return st.button("⚡ Transform Code")

def render_output_placeholder():
    st.markdown("### 🧾 Output Code")
    st.empty()

def render_structured_output(response_json, language):
    st.markdown("### 🧠 Explanation")
    st.markdown(response_json["explanation"])
    
    st.markdown("### 🧾 Code")
    st.code(response_json["code"], language=language.lower())
    
    st.markdown("### 🔍 Summary")
    st.markdown(response_json["summary"])
