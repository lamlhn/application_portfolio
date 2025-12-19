import streamlit as st

st.header("Smart Predict with LAM — your data, your insights, your future")

# option = st.selectbox(
#     "What condition would you like to analyze today?",
#     ("SAE Datamining"),
# )

# if option == "Breast cancer":
#     from breast_cancer_app import breast_cancer
#     breast_cancer()
@st.cache_data
def load_default_data():
    return pd.read_csv("dataset_default.csv")  # ← Đổi sang file của bạn

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Fichier importé avec succès.")
else:
    df = load_default_data()
    st.info("ℹ️ Aucun fichier chargé. Utilisation du fichier CSV par défaut.")

# === Affichage rapide des données ===
st.dataframe(df.head())
with st.expander("🧾 Aperçu de l'information de données"):
    if uploaded_file:
        df.head()
