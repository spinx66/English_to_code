import requests
import streamlit as st

# Groq API Key from Streamlit Secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

def english_to_code(user_input: str, lang: str = "JavaScript") -> str:
    if not user_input:
        return "❗ No input provided."

    prompt = f"""You are a coding assistant. Convert the user's casual English instruction into clean, correct {lang} code.

User: {user_input}
Code:"""

    try:
        response = requests.post(
            url="https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-8b-8192",  # ✅ Works well and is available
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            },
            timeout=15
        )

        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"⚠️ Error: {e}"
