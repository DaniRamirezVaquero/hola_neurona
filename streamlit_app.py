import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Hola neurona", page_icon="🧠")

# Imagen cabecera
st.image("./images/image.png", use_container_width=True)

# Título de la página
st.title("Hola neurona 🧠")

# Tabs
tab1, tab2, tab3 = st.tabs(
    ["Una entrada", "Dos entradas", "Tres entradas con bias (sesgo)"])

with tab1:
    st.markdown("## Una entrada")

    col1, col2 = st.columns(2)
    with col1:
        w_tab1 = st.number_input("Peso", key="w_tab1")

    with col2:
        x_tab1 = st.number_input("Entrada", key="x_tab1")

    y_tab1 = w_tab1 * x_tab1
    
    st.latex(r'y = w \cdot x')

    st.write("La salida de la neurona es", round(y_tab1, 2))

with tab2:
    st.markdown("## Dos entradas")

    col3, col4 = st.columns(2)
    with col3:
        w0_tab2 = st.slider("Peso 1", -10.0, 10.0, 0.0, key="w0_tab2")
        x0_tab2 = st.number_input("Entrada 1", key="x0_tab2")

    with col4:
        w1_tab2 = st.slider("Peso 2", -10.0, 10.0, 0.0, key="w1_tab2")
        x1_tab2 = st.number_input("Estrada 2", key="x1_tab2")

    y_tab2 = round(w0_tab2 * x0_tab2 + w1_tab2 * x1_tab2, 2)
    
    st.latex(r'y = w_0 \cdot x_0 + w_1 \cdot x_1')

    st.write("La salida de la neurona es", y_tab2)

with tab3:
    st.markdown("## Tres entradas con bias (sesgo)")

    col5, col6, col7 = st.columns(3)

    with col5:
        w0_tab3 = st.slider("Peso 1", -10.0, 10.0, 0.0, key="w0_tab3")
        x0_tab3 = st.number_input("Entrada 1", key="x0_tab3")

    with col6:
        w1_tab3 = st.slider("Peso 2", -10.0, 10.0, 0.0, key="w1_tab3")
        x1_tab3 = st.number_input("Entrada 2", key="x1_tab3")

    with col7:
        w2_tab3 = st.slider("Peso 3", -10.0, 10.0, 0.0, key="w2_tab3")
        x2_tab3 = st.number_input("Entrada 3", key="x2_tab3")

    b_tab3 = st.slider("Bias", -10.0, 10.0, 0.0, key="b_tab3")

    y_tab3 = round(w0_tab3 * x0_tab3 + w1_tab3 *
                   x1_tab3 + w2_tab3 * x2_tab3 + b_tab3, 2)
    
    st.latex(r'y = w_0 \cdot x_0 + w_1 \cdot x_1 + w_2 \cdot x_2 + b')

    st.write("La salida de la neurona es", y_tab3)
