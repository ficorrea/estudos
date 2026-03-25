import streamlit as st

hide_pages_menu = """
    <style>
        /* Esconde o menu de navegação que lista as páginas da pasta pages */
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_pages_menu, unsafe_allow_html=True)

def profile_page():
    st.title("👤 Meu Perfil")
        
    st.markdown(f"""
    **Informações do Usuário:**
    - **ID:** {st.session_state['user_id']}
    - **Usuário:** {st.session_state['username']}
    - **Email:** {st.session_state['user_email']}
    """)