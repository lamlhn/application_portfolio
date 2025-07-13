import streamlit as st

st.header("Smart Predict with LAM — your data, your insights, your future")

option = st.selectbox(
    "What condition would you like to analyze today?",
    ("Breast cancer", "House price"),
)

if option == "Breast cancer":
    from breast_cancer_app import breast_cancer
    breast_cancer()