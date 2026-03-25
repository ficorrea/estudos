import hashlib
import json
import streamlit as st

USER_DATA_FILE = "./users.json"

def hash_password(password):
    """Cria hash da senha usando SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Carrega os usuários do arquivo JSON"""
    try:
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    """Salva os usuários no arquivo JSON"""
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def check_authenticated():
    """Verifica se o usuário está autenticado"""
    return 'authenticated' in st.session_state and st.session_state.authenticated