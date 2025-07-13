import streamlit as st

st.set_page_config(
    page_title="Hoang Ngoc Lam LE",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': "mailto:lammin231@gmail.com",
        'Report a bug': "mailto:lammin231@gmail.com",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

accueil_page = st.Page("accueil.py", title="Accueil", icon=":material/home:")
personel_page = st.Page("presentation.py", title="Who am I", icon=":material/person:")
analyse_dt_page = st.Page("analyse_dt.py", title="Analyse Dataframe", icon=":material/dashboard:")
chatbot_page = st.Page("chatbot.py", title="Chatbot", icon=":material/support_agent:")
page_predict = st.Page("page_predict.py", title="Smart Predict", icon=":material/dashboard:")
pg = st.navigation(
    {
        "Home" : [accueil_page, personel_page], 
        "Application" :[analyse_dt_page, chatbot_page, page_predict]
    }
)

pg.run()
