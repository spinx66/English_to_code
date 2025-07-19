import requests
import streamlit as st

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

def english_to_code(user_input: str, lang: str = "JavaScript") -> dict:
    if not user_input:
        return {
            "explanation": "❗ No input provided.",
            "code": "",
            "summary": ""
        }

    prompt = f"""
You are an expert coding assistant. You can code in any language possible, Convert the following instruction into a clean {lang} script. Respond ONLY in this JSON format:
{{
  "explanation": "<brief explanation of the logic>",
  "code": "<final working {lang} code>",
  "summary": "<summarize the expected behavior and output>"
}}

Instruction: {user_input}
"""

    try:
        response = requests.post(
            url="https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-8b-8192",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3
            },
            timeout=15
        )
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"].strip()

        # Attempt to parse the returned content as a JSON-like dictionary
        return eval(content)  # You can replace with `json.loads` if AI output is strict JSON

    except Exception as e:
        return {
            "explanation": "",
            "code": "",
            "summary": f"⚠️ Error: {e}"
        }
