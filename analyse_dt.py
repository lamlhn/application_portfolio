import streamlit as st
import pandas as pd


st.title("📊 Analyse de données à partir d'un fichier CSV")

# === Chargement du fichier ===
uploaded_file = st.file_uploader("📁 Déposez un fichier CSV ici", type=["csv"])

# Fichier par défaut si aucun n'est fourni
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
    if not uploaded_file:
        st.markdown("### 📊 Coût des études internationales")

        st.markdown("""
        Ce fichier présente les **coûts principaux pour les étudiants internationaux**, standardisés en **USD** pour faciliter la comparaison.  
        Il inclut : pays, ville, université, programme, niveau d'études, durée, **frais de scolarité**, **coût de la vie**, **loyer**, **visa**, **assurance**, et **taux de change**.

        ---

        ### 📌 Colonnes clés

        - **Country** : Pays de l'université  
        - **City** : Ville  
        - **University** : Nom de l'université  
        - **Program** : Intitulé du programme  
        - **Level** : Niveau (Licence, Master, PhD…)  
        - **Duration_Years** : Durée (années)  
        - **Tuition_USD** : Frais de scolarité (USD)  
        - **Living_Cost_Index** : Indice coût de vie (base NYC = 100)  
        - **Rent_USD** : Loyer mensuel moyen (USD)  
        - **Visa_Fee_USD** : Frais de visa (USD)  
        - **Insurance_USD** : Assurance annuelle (USD)  
        - **Exchange_Rate** : Taux de change (local/USD)
        """)


# === Génération dynamique des filtres ===
st.subheader("🎛️ Filtres interactifs")

colonnes = df.columns.tolist()
colonnes_selectionnees = st.multiselect("Choisissez les colonnes à filtrer :", colonnes)

# Création des widgets de filtre selon type
filtres = {}
for col in colonnes_selectionnees:
    if pd.api.types.is_numeric_dtype(df[col]):
        min_val, max_val = float(df[col].min()), float(df[col].max())
        filtres[col] = st.slider(f"Filtrer {col} :", min_val, max_val, (min_val, max_val))
    else:
        valeurs = df[col].dropna().unique().tolist()
        filtres[col] = st.multiselect(f"Filtrer {col} :", valeurs, default=valeurs)

# === Bouton pour lancer l'analyse ===
if st.button("🔍 Analyser"):
    df_filtré = df.copy()
    for col, valeur in filtres.items():
        if isinstance(valeur, tuple):  # slider
            df_filtré = df_filtré[df_filtré[col].between(valeur[0], valeur[1])]
        else:  # multiselect
            df_filtré = df_filtré[df_filtré[col].isin(valeur)]
    st.success(f"✅ {len(df_filtré)} lignes correspondantes.")
    st.dataframe(df_filtré)

    # Export CSV
    st.download_button(
        label="📥 Télécharger le résultat au format CSV",
        data=df_filtré.to_csv(index=False).encode('utf-8'),
        file_name="résultat_filtré.csv",
        mime="text/csv"
    )
