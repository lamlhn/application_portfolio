import streamlit as st
import numpy as np
import joblib

def breast_cancer():
    st.subheader("Breast Cancer Prediction")
    st.text("This app uses a trained machine learning model to predict whether a breast tumor is benign or malignant based on key clinical features. Users input diagnostic measurements, and the app provides an instant prediction along with the probability score, helping support early detection and informed decisions.")
    model = joblib.load("breast_cancer_model.pkl")
    scaler = joblib.load("scaler.pkl")

    def choix_number(var):
        return st.slider(f"{var} (1-10)",1, 10, 5)

    var_list = ["Clum thickness", "Uniformity cell size", "Uniformity cell shape", "Marginal adhesion", "Single epithelial cell size", "Bare cuclei", "Bland chromatin", "Normal nucleoli", "Mitoses"]

    cols = st.columns(3)
    inputs = []
    for i, var in enumerate(var_list):
        col = cols[i % 3]
        with col:
            value = choix_number(var)
            inputs.append(value)


    if st.button("Predire", type="primary", use_container_width=True):
        input_data = np.array([inputs])

        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)[0]
        prob = model.predict_proba(input_scaled)[0][1]

        if prediction == 1:
            st.error(f"Diagnosis: Malignant (Confidence: {prob:.2%})")
        else:
            st.success(f"Diagnosis: Benign (Confidence: {(1 - prob):.2%})")
