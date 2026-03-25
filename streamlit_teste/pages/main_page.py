import streamlit as st

from datetime import datetime

from pages import (
    marketing_page, 
    profile_page, 
    dashboard_page,
    admin_page,
    config_page)

def main_app():
    """Página principal após o login"""
    st.sidebar.title(f"👤 Bem-vindo, {st.session_state['username']}!")
    
    if st.session_state['user_type'] == 'admin':
        menu = st.sidebar.selectbox(
            "Navegação",
            ["Dashboard", "Perfil", "Marketing", "Usuários", "Configurações"]
        )
    
    elif st.session_state['user_type'] == 'mkt':
        menu = st.sidebar.selectbox(
            "Navegação",
            ["Dashboard", "Perfil", 'Marketing']
        )
    
    elif st.session_state['user_type'] == 'default':
        menu = st.sidebar.selectbox(
            "Navegação",
            ["Dashboard", "Perfil"]
        )
    
    if menu == "Dashboard":
        dashboard_page.dashboard_page()
    
    elif menu == "Perfil":
        profile_page.profile_page()
    
    elif menu == "Usuários":
        admin_page.admin_page()

    elif menu == "Marketing":
        marketing_page.marketing_page()

    elif menu ==  "Configurações":
        config_page.config_page()
    
    # Botão de logout na sidebar
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Sair"):
        for key in ['authenticated', 'user_id', 'username', 'user_email', 'page']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()