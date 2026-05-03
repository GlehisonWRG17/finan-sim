import streamlit as st

def show():

    # 🔥 TÍTULO
    st.markdown("""
    <div class="hero">
        <h1>💰 FinanSim Pro</h1>
        <p class="subtitle">Simulador Financiero Inteligente</p>
    </div>
    """, unsafe_allow_html=True)

    # 🔥 INFO (SEPARADO)
    st.markdown("""
    <div class="info">
        <p class="main">Ingeniería Económica</p>
        <p>Ing. Telemetica • Grupo 301</p>
        <p>Universidad Distrital Francisco José de Caldas</p>
        <p>Facultad Tecnológica</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # 🔥 TARJETAS NAVEGABLES
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📈 Tasas", use_container_width=True):
            st.session_state["menu"] = "Conversión de Tasas"
            st.rerun()

    with col2:
        if st.button("💳 Créditos", use_container_width=True):
            st.session_state["menu"] = "Créditos"
            st.rerun()

    with col3:
        if st.button("💵 Interés", use_container_width=True):
            st.session_state["menu"] = "Interés"
            st.rerun()

    st.markdown("---")

    # 🔥 EQUIPO
    st.markdown("""
    <div class="team">
        <h3>👨‍💻 Equipo</h3>
        <p>Zharik Tatiana Rojas Cruz – 20261678045</p>
        <p>Jose Luis Vargas Alvarez -  20261678007</p>
        <p>Cristian Arley Oviedo Galindo - 20261678042 </p>
        <p>Glehison Wuhilder Rojas Guatavita – 20261678047</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # 🔥 ACTIVIDAD
    st.markdown("""
    <div class="dev">
        🚧 Dashboard de usuario en desarrollo
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # 🔥 FOOTER
    st.markdown("""
    <div class="footer">
        © 2026 Glehison Rojas — FinanSim Pro
    </div>
    """, unsafe_allow_html=True)