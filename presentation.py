import streamlit as st

# st.set_page_config(page_title="Bienvenue", page_icon="🌸", layout="wide")

# === Titre lớn ===
st.markdown("<h1 style='text-align: center; color: #6C3483;'>Bienvenue sur mon portfolio professionnel</h1>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; font-size:18px;'>
Je suis <strong>Hoang Ngoc Lam LE</strong>, étudiante vietnamienne venue en France pour poursuivre mes études supérieures. Je suis passionnée par la data, l'intelligence artificielle et la visualisation de données.  
Actuellement admise en école d'ingénieur dans le domaine de la science des données, après mon BUT 2 Science des Données, je suis à la 
recherche d'une <strong>alternance de 3 ans</strong> en tant que <strong>Data Analyst, Data Scientist ou Data Engineer</strong>.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# === Ecole ===
st.subheader("🎓 Écoles d'ingénieur où j'ai été admise")

st.markdown("""
J'ai été acceptée dans plusieurs écoles d'ingénieur en alternance pour la rentrée 2025. Ces formations me permettront de développer davantage mes compétences en **data science**, **intelligence artificielle**, et **systèmes d'information**, tout en les appliquant en entreprise.

À ce jour, je n'ai pas encore arrêté mon choix définitif.  
Chaque formation est en parfaite cohérence avec mon objectif professionnel : devenir **Data Scientist** ou **Ingénieure en Intelligence Artificielle**.
""")


import streamlit as st

ecole = {
    "nom": "ESILV",
    "domaine": "Ingénieur Majeure Data & Intelligence Artificielle",
    "rythme": "3 semaines entreprise / 2 semaines école",
    "commentaire": "Une formation axée sur les technologies avancées de la data et de l'IA, adaptée aux projets complexes en entreprise.",
    "url": "https://www.esilv.fr/"
}

st.markdown(f"""
    <div style='border: 1px solid #d3d3d3; border-radius: 10px; padding: 15px; margin-top: 10px;'>
        <h4 style='color: #2E86C1; margin-bottom: 5px; text-align: center;'>{ecole['nom']}</h4>
        <p><strong>Diplôme :</strong> {ecole['domaine']}<br>
        <strong>Rythme d'alternance :</strong> {ecole['rythme']}</p>
        <p style='font-size: 14px; color: #555;'>{ecole['commentaire']}</p>
        <a href="{ecole['url']}" target="_blank">
            <button style='padding: 8px 16px; background-color: #2E86C1; color: white; border: none; border-radius: 5px; cursor: pointer; width : 100%'>
                En savoir plus
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# === Expérience professionnelle ===

st.subheader("📌 Expérience professionnelle")

st.markdown(
    """
<div style='text-align: center;'>

### 🧪 <strong>Stagiaire en Structuration et Développement de Base de Données</strong>  
📍 <em>INRAE - Unité FRISE, Antony (Île-de-France)</em>  
📅 <em>Avril - Août 2025</em><br><br>    



</div>

<div style='text-align: justify;'>

🔹 Stage réalisé dans le cadre de ma 2ᵉ année de BUT Science des Données à l'IUT de Lille.  
🔹 Immersion professionnelle de 4 mois centrée sur la structuration de bases de données et l'intégration de solutions d'<strong>intelligence artificielle</strong>.

**Missions réalisées :**
- Préparation, nettoyage et conversion de plusieurs millions de lignes de données avec <strong>Python</strong>  
- Conception d'une base de données relationnelle et d'une application web locale avec <strong>Streamlit</strong>  
- Développement d'un <a href="https://www.pinecone.io/learn/large-language-models/" target="_blank"><strong>LLM</strong></a> personnalisé via <strong>PandasAI</strong>  
- Intégration d'une <a href="https://platform.openai.com/docs/api-reference" target="_blank"><strong>API OpenAI</strong></a> pour enrichir l'interaction avec les données

</div>
""", unsafe_allow_html=True
)

st.markdown("---")


# === Compétences en mode "grille avec popup" ===
st.subheader("🧠 Mes compétences techniques")

competences = [
    {
        "nom": "Python",
        "img": "https://img.icons8.com/color/96/000000/python.png",
        "description": "Manipulation des données avec PySpark, Pandas et NumPy, et visualisation avec Matplotlib et Seaborn",
        "link": "https://www.python.org/"
    },
    {
        "nom": "SQL, NoSQL",
        "img": "https://img.icons8.com/color/96/000000/sql.png",
        "description": "Requêtes T-SQL et PL/SQL, procédures stockées, fonctions, curseurs pour l'automatisation et le contrôle.",
        "link": "https://fr.wikipedia.org/wiki/Structured_Query_Language"
    },
    {
        "nom": "R",
        "img": "https://img.icons8.com/ios-filled/100/276DC3/r-project.png",
        "description": "Développement d’applications interactives (Shiny), analyse statistique, manipulation de données avec dplyr, visualisation avec ggplot2.",
        "link": "https://www.r-project.org/"
    },
    {
    "nom": "LLMs, RAG & NLP",
    "img": "https://img.icons8.com/ios-filled/100/000000/ai.png",
    "description": "Création de systèmes de question/réponse sur documents internes grâce à RAG et LLM (Transformers, LangChain), traitement du langage naturel.",
    "link": "https://python.langchain.com/"
    },
    {
        "nom": "Power BI",
        "img": "https://img.icons8.com/color/96/000000/power-bi.png",
        "description": "Création de tableaux de bord interactifs, visualisation d'indicateurs clés (KPI).",
        "link": "https://powerbi.microsoft.com/"
    },
    {
        "nom": "Qlik Sense",
        "img": "https://img.icons8.com/external-tal-revivo-color-tal-revivo/96/external-qlik-a-business-analytics-platform-that-delivers-real-time-insights-logo-color-tal-revivo.png",
        "description": "Visualisation de données, génération de rapports et tableaux de bord interactifs.",
        "link": "https://www.qlik.com/fr-fr/products/qlik-sense"
    },
    {
        "nom": "TensorFlow",
        "img": "https://img.icons8.com/color/96/000000/tensorflow.png",
        "description": "Framework pour la classification, la régression et le deep learning.",
        "link": "https://www.tensorflow.org/"
    },
    {
        "nom": "Scikit-learn",
        "img": "https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg",
        "description": "Librairie Python pour la modélisation prédictive, classification, régression et clustering.",
        "link": "https://scikit-learn.org/"
    },
    {
        "nom": "ODI / SSIS",
        "img": "https://img.icons8.com/color/96/000000/data-in-both-directions.png",
        "description": "Conception ETL, création de flux de données pour l'intégration et la transformation.",
        "link": "https://learn.microsoft.com/fr-fr/sql/integration-services/"
    },
    {
        "nom": "Streamlit",
        "img": "https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png",
        "description": "Création d'applications web simples pour explorer et visualiser les données.",
        "link": "https://streamlit.io/"
    },
    {
        "nom": "Web Technologie (HTML/CSS/JS/PHP/Bootstrap)",
        "img": "https://img.icons8.com/color/96/000000/code.png",
        "description": "Développement d'applications web dynamiques et interactives.",
        "link": "https://developer.mozilla.org/fr/"
    },
    {
    "nom": "Git",
    "img": "https://img.icons8.com/ios-filled/100/000000/git.png",
    "description": "Contrôle de version distribué, collaboration sur GitHub et GitLab, gestion efficace du code source.",
    "link": "https://git-scm.com/"
    },
    {
    "nom": "SAS",
    "img": "https://img.icons8.com/ios-filled/100/00599C/sas.png",
    "description": "Analyse statistique avancée, manipulation et exploration de données, reporting et modélisation prédictive.",
    "link": "https://www.sas.com/"
    }
]

cols = st.columns(3)

for i, comp in enumerate(competences):
    with cols[i % 3]:
        st.image(comp["img"], width=70)
        st.markdown(f"### {comp['nom']}")
        with st.expander("📘 En savoir plus"):
            st.write(comp["description"])
            st.markdown(f"[🔗 En savoir plus sur {comp['nom']}]({comp['link']})")

st.markdown("---")

# === projets ===
projects = [
    {
        "title": "Credit risk scoring",
        "date": "Dec 2024 - Jan 2025",
        "desc": """
            Arbres de Décision et Apprentissage par Ensemble :
            - Prédire le risque de défaut avec des modèles basés sur des arbres  
            - Arbres de décision et algorithme d'apprentissage des arbres de décision  
            - Forêt aléatoire : combiner plusieurs arbres en un seul modèle  
            - Gradient boosting : une autre méthode pour combiner des arbres de décision
        """,
        "skills": "Decision Trees · Random Forest · Gradient Boosting · Machine Learning · Python · Jupyter",
        "link": "https://github.com/lamlhn/credit-scoring"
    },
    {
        "title": "Intégration d'un Data Warehouse",
        "date": "Sep 2024 - Jan 2025",
        "desc": """
            - Mise en place d'un data warehouse en utilisant Oracle SQL Developer et Oracle Data Integrator (ODI) 
            pour extraire, transformer et charger (ETL) des données de différentes sources. 
            - Développement en SQL pour la gestion des bases de données, l'optimisation des processus d'intégration 
            et la construction de modèles de données DSA (Data Store Area) et ODS (Operational Data Store).   
            - Conception d'une architecture de data warehouse en étoile, permettant d'automatiser le flux de données 
            et d'améliorer l'efficacité des analyses.
        """,
        "skills": "Extract, Transform, Load (ETL) · Oracle SQL Developer · Oracle Data Integrator (ODI)· Data Modeling · SQL",
        "link": ""
    },
    {
        "title": "Churn Prediction",
        "date": "Nov 2024",
        "desc": """
            - Prédire les clients susceptibles de se désabonner avec la régression logistique
            - Réaliser une analyse exploratoire des données pour identifier les caractéristiques importantes
            - Encoder les variables catégorielles pour les utiliser dans les modèles d'apprentissage automatique
            - Utiliser la régression logistique pour la classification
        """,
        "skills": "Machine Learning · Classification · Logistic Regression · Python",
        "link": "https://github.com/lamlhn/churn-prediction"
    },
    {
        "title": "Prédiction des Prix des Voitures",
        "date": "Oct 2024",
        "desc": """
            - Nettoyage et exploration des données (traitement des valeurs manquantes, visualisations).
            - Division des données (entraînement, validation, test).
            - Entraînement d'un modèle de régression linéaire.
            - Amélioration des performances grâce à l'ingénierie des caractéristiques (âge, marques, carburant).
        """,
        "skills": "Linear Regression · Python · Pandas · Scikit-learn · Seaborn · Matplotlib · Predictive Modeling",
        "link": ""
    },
    {
        "title": "Pac-Man - Jeu vidéo",
        "date": "Mar 2024 - Jun 2024",
        "desc": """
            - Développement du jeu en C# avec une base de données SQL pour la gestion des scores.
            - Implémentation des algorithmes es mouvements des fantômes et application de la programmation orientée objet.
            - Utilisation de GitHub pour la collaboration, WinForms pour la création de l'interface utilisateur et Figma pour la conception.
            - Réalisation de tests unitaires pour assurer la qualité du code.
        """,
        "skills": "C# · WinForms · SQL · GitHub · Visual Studio · Game Dev",
        "link": ""
    },
    {
        "title": "Calculateur de Masque Réseau",
        "date": "Apr 2024 - May 2024",
        "desc": """
            - Application en C# pour calculer les informations IPv4  
            - Tests unitaires, design interface Windows Forms
        """,
        "skills": "C# · WinForms · IP Addressing · Unit Testing · GitHub",
        "link": "https://github.com/lamlhn/sae_reseaux"
    },
    {
        "title": "BeKr - Site Web",
        "date": "Sep 2023 - Jan 2024",
        "desc": """
            - Développement d'un site web avec HTML, CSS, et JavaScript, en utilisant le framework Bootstrap.
            - Conception d'interface avec Figma.
            - Optimisation du site pour une compatibilité multi-plateformes et une navigation fluide sur mobiles, tablettes et ordinateurs.
        """,
        "skills": "HTML · CSS · JavaScript · Bootstrap · Figma · Visual Studio Code",
        "link": ""
    }
]

st.subheader("📁 Projets personnels")

# Hiển thị 2 project đầu tiên
for i in range(2):
    p = projects[i]
    st.subheader(p["title"])
    st.caption(p["date"])
    st.write(p["desc"])
    st.markdown(f"**Skills**: {p['skills']}")
    if p["link"]:
        st.markdown(f"[🔗 GitHub]({p['link']})")
        st.write("")

# Tạo checkbox để hiển thị thêm
if st.button("Voir plus"):
    for p in projects[2:]:
        st.subheader(p["title"])
        st.caption(p["date"])
        st.write(p["desc"])
        st.markdown(f"**Skills**: {p['skills']}")
        if p["link"]:
            st.markdown(f"[🔗 GitHub]({p['link']})")
            st.write("")

st.markdown("---")

# === Footer ou suite ===
st.markdown("""
<div style='text-align: center; font-size:16px;'>
    💬 N'hésitez pas à me contacter pour toute opportunité d'alternance !<br><br>
    📞 07 48 15 66 21 &nbsp;&nbsp;|&nbsp;&nbsp; <a href="mailto:lammin231@gmail.com">📧 lammin231@gmail.com </a> &nbsp;&nbsp;|&nbsp;&nbsp; 📍 Cachan (94230)
</div>
""", unsafe_allow_html=True)
