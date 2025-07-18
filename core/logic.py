import requests
import streamlit as st

# Access the Groq API key from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

def english_to_code(user_input: str, lang: str = "JavaScript") -> str:
    if not user_input:
        return "❗ No input provided."

    prompt = f"""You are an AI that converts plain English into clean, minimal {lang} code.

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
                "model": "mixtral-8x7b-32768",
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
