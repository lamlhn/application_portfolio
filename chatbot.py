import streamlit as st
from openai import OpenAI
import os

st.markdown("<h1 style='text-align: center; color: #6C3483;'>Votre Assistant IA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Posez-moi vos questions sur les études internationales, les coûts ou les programmes !</p>", unsafe_allow_html=True)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Posez votre question")

if prompt:
    st.session_state.message.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})