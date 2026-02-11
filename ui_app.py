import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000/generate-sql"

st.set_page_config(page_title="Smart Data Querying", layout="wide")
st.title("🧠 Smart Data Querying")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Ask a question about your data...")

if user_input:
    # Show user message
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    # Call FastAPI
    response = requests.post(API_URL, json={
        "user_prompt": user_input
    }).json()

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": response
    })

# Render chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        with st.chat_message("user"):
            st.write(chat["content"])

    else:
        with st.chat_message("assistant"):
            st.markdown("### 🧠 Summary")
            st.write(chat["content"]["summary"])

            with st.expander("🧾 Generated SQL"):
                st.code(chat["content"]["generated_sql"], language="sql")

            st.markdown("### 📊 Result")
            df = pd.DataFrame(chat["content"]["result"])
            st.dataframe(df, use_container_width=True)
