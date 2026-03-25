import streamlit as st
from datetime import datetime

hide_pages_menu = """
    <style>
        /* Esconde o menu de navegação que lista as páginas da pasta pages */
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_pages_menu, unsafe_allow_html=True)

def dashboard_page():
    st.title("📊 Dashboard")
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Usuários Ativos", "1", "+0")
    with col2:
        st.metric("Sessões", "1", "+1")
    with col3:
        st.metric("Último Acesso", datetime.now().strftime("%d/%m/%Y"))