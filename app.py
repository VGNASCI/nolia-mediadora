import streamlit as st

st.set_page_config(
    page_title="Nólia Mediadora",
    page_icon="🤝",
    layout="wide"
)

def main():
    st.title("🤝 Nólia - Assistente de Comunicação")
    st.subheader("Conectando surdos e ouvintes angolanos")
    
    st.write("""
    Bem-vindo ao protótipo da Nólia! 
    Esta é uma ferramenta de mediação entre a comunidade surda e ouvinte.
    """)
    
    # Modos de operação
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🕊️ Modo Amigo", use_container_width=True):
            st.session_state.modo = "amigo"
            st.success("Modo Amigo ativado - Conversa livre")
    
    with col2:
        if st.button("🤝 Modo Mediação", use_container_width=True):
            st.session_state.modo = "mediacao"
            st.success("Modo Mediação ativado - Turnos controlados")
    
    # Status atual
    if 'modo' not in st.session_state:
        st.session_state.modo = "amigo"
    
    st.info(f"**Modo atual:** {st.session_state.modo.upper()}")

if __name__ == "__main__":
    main()
