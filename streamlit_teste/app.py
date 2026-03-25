import streamlit as st
from pages.login_page import login_page
from pages.register_page import register_page
from pages.main_page import main_app

hide_pages_menu = """
    <style>
        /* Esconde o menu de navegação que lista as páginas da pasta pages */
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_pages_menu, unsafe_allow_html=True)

# Configuração da página
st.set_page_config(
    page_title="Sisteminha Teste",
    page_icon="🔒",
    layout="wide"
)

# Inicialização da sessão
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

# Roteamento das páginas
if st.session_state['authenticated']:
    main_app()
else:
    if st.session_state['page'] == 'login':
        login_page()
    else:
        register_page()