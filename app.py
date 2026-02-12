import streamlit as st
from google import genai
from google.genai import types


client = genai.Client(api_key="AIzaSyBqQdlIbxJrr4ZvHsgO5T9egMCP6VQmMgc")

system_prompt = "You are a helpful assistant."

st.set_page_config(page_title="My Gemini Chatbot", page_icon=":robot:")
st.title("My Gemini Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything about the code in this notebook!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    
    with st.chat_message("assistant"):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "system_instruction": system_prompt,
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
            }
        )
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})