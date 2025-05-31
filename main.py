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

accueil_page = st.Page("accueil.py", title="Accueil", icon=":material/add_circle:")
personel_page = st.Page("presentation.py", title="Who am I", icon=":material/delete:")
#analyse_dt_page = st.Page("app_multi/analyse_dt.py", title="Analyse Dataframe", icon=":material/dashboard:")
#test_page = st.Page("app_multi/test.py", title="Analyse Dataframe", icon=":material/delete:")

pg = st.navigation(
    {
        "Home" : [accueil_page, personel_page], 
        #"Application" :[analyse_dt_page, test_page]
    }
)
pg.run()
