import sqlite3
import streamlit as st
from utils.db_functions import get_db_connection, hash_password

hide_pages_menu = """
    <style>
        /* Esconde o menu de navegação que lista as páginas da pasta pages */
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_pages_menu, unsafe_allow_html=True)

def register_user(username, password, email):
    """Registra um novo usuário"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        hashed_password = hash_password(password)
        user_type = "default"
        cursor.execute('''
            INSERT INTO users (username, password, email, user_type)
            VALUES (?, ?, ?, ?)
        ''', (username, hashed_password, email, user_type))
        conn.commit()
        return True, "Usuário registrado com sucesso!"
    except sqlite3.IntegrityError as e:
        if "username" in str(e):
            return False, "Nome de usuário já existe!"
        elif "email" in str(e):
            return False, "Email já está cadastrado!"
        else:
            return False, "Erro ao registrar usuário!"
    finally:
        conn.close()

def register_page():
    """Página de registro"""
    st.title("📝 Criar Nova Conta")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Preencha seus dados")
        
        with st.form("register_form"):
            new_username = st.text_input("Usuário")
            new_email = st.text_input("Email")
            new_password = st.text_input("Senha", type="password")
            confirm_password = st.text_input("Confirmar Senha", type="password")

            submit = st.form_submit_button("Registrar")
            
            if submit:
                if new_username and new_email and new_password and confirm_password:
                    if new_password == confirm_password:
                        if len(new_password) >= 6:
                            success, message = register_user(new_username, new_password, new_email)
                            if success:
                                st.success(message)
                                st.info("Faça login com suas novas credenciais.")
                                st.session_state['page'] = 'login'
                                st.rerun()
                            else:
                                st.error(message)
                        else:
                            st.warning("A senha deve ter pelo menos 6 caracteres!")
                    else:
                        st.warning("As senhas não coincidem!")
                else:
                    st.warning("Preencha todos os campos!")
        
        if st.button("Voltar para Login"):
            st.session_state['page'] = 'login'
            st.rerun()
