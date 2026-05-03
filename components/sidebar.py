import streamlit as st

def show_sidebar():

    st.sidebar.title("📊 FinanSim")

    # 🔥 valor por defecto
    if "menu" not in st.session_state:
        st.session_state["menu"] = "Dashboard"

    option = st.sidebar.radio(
        "Navegación",
        [
            "Dashboard",
            "Conversión de Tasas",
            "Interés",
            "Créditos"
        ],
        index=[
            "Dashboard",
            "Conversión de Tasas",
            "Interés",
            "Créditos"
        ].index(st.session_state["menu"])
    )

    # 🔥 sincroniza estado
    st.session_state["menu"] = option

    return option