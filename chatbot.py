import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
import os
import torch

# Titre et intro
st.markdown("<h1 style='text-align: center; color: #6C3483;'>Votre Assistant IA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Posez-moi vos questions sur les études internationales, les coûts ou les programmes !</p>", unsafe_allow_html=True)

# Load model & tokenizer
token = st.secrets("HUGGINGFACEHUB_API_TOKEN")
# login(token=token)
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it", token=token)
device = "mps" if torch.backends.mps.is_available() else "cpu"
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it", torch_dtype=torch.float16, token=token)
model = model.to(device)


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
        inputs = tokenizer(prompt + tokenizer.eos_token, return_tensors="pt").to(model.device)

        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            do_sample=True,
            top_p=0.9,
            temperature=0.7
        )

        # Lấy phần mới sinh ra
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Cắt prompt đầu ra nếu cần (để chỉ lấy phần trả lời)
        reply_text = generated_text[len(prompt):].strip()

        st.markdown(reply_text)
    st.session_state.messages.append({"role": "assistant", "content": reply_text})
