import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Titre et intro
st.markdown("<h1 style='text-align: center; color: #6C3483;'>Votre Assistant IA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Posez-moi vos questions sur les études internationales, les coûts ou les programmes !</p>", unsafe_allow_html=True)

# Load model & tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Init session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des messages existants
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Saisie utilisateur
prompt = st.chat_input("Posez votre question")

if prompt:
    # Affichage message user
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Génération réponse bot
    with st.chat_message("assistant"):
        user_input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')

        # On peut ajouter historique plus tard si tu veux
        bot_input_ids = user_input_ids

        output_ids = model.generate(
            bot_input_ids,
            max_length=1000,
            pad_token_id=tokenizer.eos_token_id
        )

        reply_ids = output_ids[:, bot_input_ids.shape[-1]:][0]
        reply_text = tokenizer.decode(reply_ids, skip_special_tokens=True)

        st.markdown(reply_text)
    st.session_state.messages.append({"role": "assistant", "content": reply_text})
