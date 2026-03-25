import streamlit as st
import requests

st.title("CHATBOT")

API_KEY = "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"

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask something")

if st.button("Send") and user_input:
    st.session_state.chat.append(("You", user_input))

    try:
        with st.spinner("Thinking... 🤔"):

            url = "https://openrouter.ai/api/v1/chat/completions"

            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                
            }

            data = {
                "model": "meta-llama/llama-3-8b-instruct",  # ✅ good free model
                "messages": [
                    {"role": "user", "content": user_input}
                ]
            }

            response = requests.post(url, headers=headers, json=data)

            if response.status_code != 200:
                reply = f"⚠️ Error {response.status_code}"
            else:
                res = response.json()
                reply = res["choices"][0]["message"]["content"]

    except Exception as e:
        reply = f"⚠️ Error: {e}"

    st.session_state.chat.append(("Bot", reply))

for sender, msg in st.session_state.chat:
    st.write(f"{sender}: {msg}")
