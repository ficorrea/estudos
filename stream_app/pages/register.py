
import streamlit as st
from datetime import datetime
from utils.users import hash_password, save_users, load_users

def register_user(username, password, email=None):
    """Registra um novo usuário"""
    users = load_users()
    
    if username in users:
        return False, "Usuário já existe!"
    
    if len(password) < 6:
        return False, "Senha deve ter pelo menos 6 caracteres!"
    
    # Cria hash da senha
    hashed_password = hash_password(password)
    
    # Adiciona o novo usuário
    users[username] = {
        'password_hash': hashed_password,
        'email': email,
        'created_at': datetime.now().isoformat(),
        'last_login': None
    }
    
    save_users(users)
    return True, "Usuário registrado com sucesso!"

def register_page():
    """Página de registro"""
    st.title("📝 Registro de Usuário")
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.subheader("Criar Nova Conta")
        
        with st.form("register_form"):
            username = st.text_input("Usuário*", placeholder="Escolha um nome de usuário")
            email = st.text_input("E-mail", placeholder="seu@email.com (opcional)")
            password = st.text_input("Senha*", type="password", placeholder="Mínimo 6 caracteres")
            confirm_password = st.text_input("Confirmar Senha*", type="password", placeholder="Digite novamente")
            
            col1, col2 = st.columns(2)
            with col1:
                submit = st.form_submit_button("Registrar")
            with col2:
                cancel = st.form_submit_button("Cancelar")
            
            if cancel:
                st.session_state.page = "login"
                st.rerun()
            
            if submit:
                if not username or not password:
                    st.error("Campos marcados com * são obrigatórios!")
                elif password != confirm_password:
                    st.error("As senhas não coincidem!")
                else:
                    success, message = register_user(username, password, email)
                    if success:
                        st.success(message)
                        st.session_state.page = "login"
                        st.rerun()
                    else:
                        st.error(message)