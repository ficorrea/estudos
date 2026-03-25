import streamlit as st
from utils.db_functions import authenticate_user

hide_pages_menu = """
    <style>
        /* Esconde o menu de navegação que lista as páginas da pasta pages */
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_pages_menu, unsafe_allow_html=True)

# Funções de interface
def login_page():
    """Página de login"""
    st.title("🔐 Autenticação")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Login")
        
        with st.form("login_form"):
            username = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            submit = st.form_submit_button("Entrar")
            
            if submit:
                if username and password:
                    user = authenticate_user(username, password)
                    
                    if user:
                        st.session_state['authenticated'] = True
                        st.session_state['user_id'] = user[0]
                        st.session_state['username'] = user[1]
                        st.session_state['user_email'] = user[2]
                        st.session_state['user_type'] = user[3]
                        st.rerun()
                    else:
                        st.error("Usuário ou senha inválidos!")
                else:
                    st.warning("Preencha todos os campos!")
        
        st.markdown("---")
        st.markdown("### Novo por aqui?")
        if st.button("Criar nova conta"):
            st.session_state['page'] = 'register'
            st.rerun()