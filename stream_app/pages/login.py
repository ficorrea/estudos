import hashlib
from datetime import datetime
import streamlit as st
from utils.users import load_users, hash_password, save_users

def authenticate_user(username, password):
    """Autentica um usuário"""
    users = load_users()
    
    if username not in users:
        return False, "Usuário não encontrado!"
    
    # Verifica a senha
    hashed_password = hash_password(password)
    if users[username]['password_hash'] != hashed_password:
        return False, "Senha incorreta!"
    
    # Atualiza o último login
    users[username]['last_login'] = datetime.now().isoformat()
    save_users(users)
    
    return True, "Login bem-sucedido!"

def login_page():
    """Página de login"""
    st.title("🔐 Sistema de Autenticação")
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.subheader("Login")
        
        with st.form("login_form"):
            username = st.text_input("Usuário", placeholder="Digite seu nome de usuário")
            password = st.text_input("Senha", type="password", placeholder="Digite sua senha")
            submit = st.form_submit_button("Entrar")
            
            if submit:
                if username and password:
                    success, message = authenticate_user(username, password)
                    if success:
                        st.session_state.authenticated = True
                        st.session_state.username = username
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.warning("Preencha todos os campos!")
        
        st.markdown("---")
        st.write("Não tem uma conta?")
        if st.button("Registrar-se"):
            st.session_state.page = "register"
            st.rerun()