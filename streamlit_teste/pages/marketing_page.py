import streamlit as st

hide_pages_menu = """
    <style>
        /* Esconde o menu de navegação que lista as páginas da pasta pages */
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_pages_menu, unsafe_allow_html=True)

def marketing_page():
    st.write('Essa é uma página de marketing!!!')