import streamlit as st
from datetime import datetime
from utils.users import load_users

def dashboard():
    """Dashboard principal após login"""
    st.title(f"👋 Bem-vindo, {st.session_state.username}!")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Status", "Online")
    
    with col2:
        users = load_users()
        user_data = users.get(st.session_state.username, {})
        if user_data.get('last_login'):
            last_login = datetime.fromisoformat(user_data['last_login'])
            st.metric("Último Login", last_login.strftime("%d/%m/%Y %H:%M"))
    
    with col3:
        st.metric("Conta Criada", 
                 datetime.fromisoformat(user_data.get('created_at', datetime.now().isoformat())).strftime("%d/%m/%Y"))
    
    st.markdown("---")
    
    # Área de conteúdo principal
    st.subheader("📊 Seu Dashboard")
    
    tab1, tab2, tab3 = st.tabs(["📈 Estatísticas", "⚙️ Configurações", "👤 Perfil"])
    
    with tab1:
        st.write("### Suas Estatísticas")
        st.write("Aqui você pode visualizar suas estatísticas de uso...")
        # Adicione gráficos ou estatísticas aqui
        
    with tab2:
        st.write("### Configurações da Conta")
        st.write("Configure suas preferências...")
        
        # Exemplo: Alterar senha
        with st.expander("Alterar Senha"):
            current_pass = st.text_input("Senha Atual", type="password")
            new_pass = st.text_input("Nova Senha", type="password")
            confirm_new_pass = st.text_input("Confirmar Nova Senha", type="password")
            
            if st.button("Atualizar Senha"):
                if new_pass == confirm_new_pass:
                    st.success("Senha atualizada com sucesso!")
                else:
                    st.error("As senhas não coincidem!")
    
    with tab3:
        st.write("### Seu Perfil")
        users = load_users()
        user_data = users.get(st.session_state.username, {})
        
        st.write(f"**Usuário:** {st.session_state.username}")
        st.write(f"**E-mail:** {user_data.get('email', 'Não informado')}")
        st.write(f"**Conta criada em:** {datetime.fromisoformat(user_data.get('created_at')).strftime('%d/%m/%Y às %H:%M')}")
    
    # Logout button na sidebar
    with st.sidebar:
        st.markdown("---")
        if st.button("🚪 Sair", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.username = None
            st.session_state.page = "login"
            st.rerun()