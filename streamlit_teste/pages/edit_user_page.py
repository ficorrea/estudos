import streamlit as st
from utils.db_functions import (
    get_user, 
    update_user_type, 
    get_all_users,
    act_deact_user)

hide_pages_menu = """
    <style>
        /* Esconde o menu de navegação que lista as páginas da pasta pages */
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_pages_menu, unsafe_allow_html=True)

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

def clicked():
    st.session_state.button_clicked = True

def list_users():
    st.subheader("Usuários")
    users_df = get_all_users()
    st.dataframe(users_df)

def update_type_user():
    """Página de update"""
    st.title("📝 Editar Conta")
    username = st.text_input("Selecione o usuário desejado:")
    if username:
        if st.button('Submit', on_click=clicked) or st.session_state.button_clicked:
            user_up = get_user(username)
            st.badge(f"Usuário: {user_up[0]}")
            st.badge(f"Email: {user_up[1]}")
            user_type = st.text_input("Type User: *", value=user_up[2])

            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("Atualizar", type="primary", use_container_width=True):
                    try:
                        update_user_type(username=user_up[0], user_type=user_type)
                        st.success('Atualização executada com sucesso!!!')
                    except Exception as e:
                        st.error(f'Falha na atualização {e}')
            with col_btn2:
                sb_cancel = st.button("Cancelar", use_container_width=True)
                if sb_cancel:
                    st.rerun()
    else:
        pass
    

def user_status():
    st.subheader("Status do Usuário")
    users_df = get_all_users()
    user_to_change_status = st.selectbox(
        "Selecione o usuário",
        users_df['username'].tolist()
    )
    status = int(1 - users_df[users_df.username == user_to_change_status]['is_active'].values[0])
    if st.button("Submit"):
        act_deact_user(user_to_change_status, status)
        if status == 1:
            st.warning(f"Usuário {user_to_change_status} ativado!!!")
        else: 
            st.warning(f"Usuário {user_to_change_status} desativado!!!")