import streamlit as st
from pages.edit_user_page import *
from utils.db_functions import get_all_users

hide_pages_menu = """
    <style>
        /* Esconde o menu de navegação que lista as páginas da pasta pages */
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_pages_menu, unsafe_allow_html=True)

def admin_page():
    st.title("👥 Gerenciar Usuários")

    adm_menu = st.selectbox("Administração", ["Listar", "Status", "Editar"])

    if adm_menu == "Listar":
        list_users()
    
    if adm_menu == "Status":
        user_status()
    
    if adm_menu == "Editar":
        update_type_user()