import streamlit as st
import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from pages.dashboard import dashboard
from pages.login import login_page
from pages.register import register_page

# Configuração da página
st.set_page_config(
    page_title="Sistema de Autenticação",
    page_icon="🔐",
    layout="wide"
)

# Caminho para o arquivo de usuários
USER_DATA_FILE = "users.json"

def init_user_data():
    """Inicializa o arquivo de dados de usuários se não existir"""
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'w') as f:
            json.dump({}, f)

def main():
    """Função principal da aplicação"""
    
    # Inicializa o arquivo de dados
    init_user_data()
    
    # Inicializa o estado da sessão
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'page' not in st.session_state:
        st.session_state.page = "login"
    if 'username' not in st.session_state:
        st.session_state.username = None
    
    # Mostra a página apropriada
    if st.session_state.authenticated:
        dashboard()
    else:
        if st.session_state.page == "register":
            register_page()
        else:
            login_page()
    
    # Rodapé
    st.markdown("---")
    st.caption("Sistema de Autenticação v1.0 © 2024")

if __name__ == "__main__":
    main()