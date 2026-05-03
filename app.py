import streamlit as st
from components.sidebar import show_sidebar
from views import dashboard

# Configuración
st.set_page_config(
    page_title="FinanSim Pro",
    layout="wide"
)

# Cargar CSS
def load_css():
    with open("assets/styles.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Sidebar
option_sidebar = show_sidebar()

# 🔥 prioriza navegación desde botones
if "nav" in st.session_state:
    option = st.session_state["nav"]
else:
    option = option_sidebar
    
    
  # 🔥 limpiar navegación después de usarla
if "nav" in st.session_state:
    nav_temp = st.session_state["nav"]
    del st.session_state["nav"]
    option = nav_temp  

# Navegación
if option == "Dashboard":
    dashboard.show()

elif option == "Conversión de Tasas":

    import streamlit as st
    from modules import tasas

    st.title("📈 Conversión de Tasas")

    tipo = st.selectbox(
        "Tipo de conversión",
        [
            "Nominal a Efectiva",
            "Efectiva a Nominal",
            "Cambio de periodo"
        ]
    )

    st.markdown("---")

    if tipo == "Nominal a Efectiva":
        i = st.number_input("Tasa nominal (%)", value=10.0)
        i = tasas.decimal(i)
        m = st.number_input("Número de periodos (m)", value=12)

        if st.button("Calcular"):
            resultado = tasas.nominal_a_efectiva(i, m)
            st.success(f"Tasa efectiva: {resultado*100:.2f}%")

    elif tipo == "Efectiva a Nominal":
        i = st.number_input("Tasa efectiva (%)", value=10.0) / 100
        m = st.number_input("Número de periodos (m)", value=12)

        if st.button("Calcular"):
            resultado = tasas.efectiva_a_nominal(i, m)
            st.success(f"Tasa nominal: {resultado*100:.2f}%")

    elif tipo == "Cambio de periodo":
        i = st.number_input("Tasa efectiva (%)", value=10.0) / 100
        n1 = st.number_input("Periodo origen", value=1)
        n2 = st.number_input("Periodo destino", value=12)

        if st.button("Calcular"):
            resultado = tasas.convertir_efectiva(i, n1, n2)
            st.success(f"Tasa equivalente: {resultado*100:.2f}%")

elif option == "Interés":

    from modules import interes

    st.title("💵 Simulador de Interés")

    tipo = st.selectbox(
        "Tipo de cálculo",
        [
            "Interés Simple",
            "Interés Compuesto",
            "Valor Presente"
        ]
    )

    st.markdown("---")

    P = st.number_input("Capital inicial", value=1000000.0)
    tasa = st.number_input("Tasa (%)", value=10.0)
    n = st.number_input("Número de periodos", value=5)

    i = tasa / 100

    if st.button("Calcular"):

        if tipo == "Interés Simple":
            interes_val = interes.interes_simple(P, i, n)
            monto = interes.monto_simple(P, i, n)

        elif tipo == "Interés Compuesto":
            interes_val = interes.interes_compuesto(P, i, n)
            monto = interes.monto_compuesto(P, i, n)

        elif tipo == "Valor Presente":
            monto = interes.valor_presente(P, i, n)
            interes_val = 0

        st.markdown("### 📊 Resultados")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("💰 Monto final", f"${monto:,.2f}")

        with col2:
            st.metric("📈 Interés generado", f"${interes_val:,.2f}")

elif option == "Créditos":

    from modules import creditos
    import plotly.express as px

    st.title("🏦 Simulador de Créditos")

    st.markdown("### Datos del crédito")

    col1, col2 = st.columns(2)

    with col1:
        P_input = st.text_input("Monto del crédito", value="10,000,000")

        try:
            P = float(P_input.replace(",", ""))
        except:
            P = 0

        tasa = st.number_input("Tasa (%)", value=12.0)

    with col2:
        n = st.number_input("Número de periodos", value=12)
        tipo = st.selectbox("Sistema", ["Francés"])

    st.markdown("---")

    if st.button("Calcular crédito"):

        i = tasa / 100

        cuota = creditos.cuota_frances(P, i, n)

        st.success(f"Cuota mensual: ${cuota:,.2f}")

        df = creditos.tabla_amortizacion(P, i, n)

        # 🔥 TABLA FORMATEADA
        df_mostrar = df.copy()
        for col in ["Cuota", "Interés", "Capital", "Saldo"]:
            df_mostrar[col] = df_mostrar[col].apply(lambda x: f"${x:,.2f}")

        st.markdown("### Tabla de amortización")
        st.dataframe(df_mostrar)

        # 🔥 GRÁFICAS
        st.markdown("### 📊 Gráficas del crédito")

        fig1 = px.line(
            df,
            x="Periodo",
            y="Saldo",
            title="Evolución del saldo"
        )
        fig1.update_layout(template="plotly_dark")
        st.plotly_chart(fig1, use_container_width=True)

        df_plot = df.melt(
            id_vars="Periodo",
            value_vars=["Interés", "Capital"],
            var_name="Tipo",
            value_name="Valor"
        )

        fig2 = px.bar(
            df_plot,
            x="Periodo",
            y="Valor",
            color="Tipo",
            barmode="stack",
            title="Interés vs Capital"
        )
        fig2.update_layout(template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)
        
        st.markdown("### 📊 Análisis del crédito")

        total_pagado = df["Cuota"].sum()
        total_interes = df["Interés"].sum()
        total_capital = df["Capital"].sum()

        porcentaje_interes = (total_interes / total_pagado) * 100
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("💰 Total pagado", f"${total_pagado:,.2f}")

        with col2:
            st.metric("📈 Total intereses", f"${total_interes:,.2f}")

        with col3:
            st.metric("📊 % Interés", f"{porcentaje_interes:.2f}%")
            
        if porcentaje_interes > 50:
            st.warning("⚠️ Estás pagando más en intereses que en capital.")
        else:
            st.success("✅ Buen equilibrio entre capital e intereses.")