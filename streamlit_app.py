import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Hola neurona", page_icon="🧠")

# Imagen cabecera
st.image("./images/image.png", use_container_width=True)

# Título de la página
st.title("Hola neurona 🧠")

# Tabs
tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas con bias (sesgo)"])

with tab1:
    st.markdown("## Una entrada")
    
    col1, col2 = st.columns(2)
    with col1:
      w_tab1 = st.number_input("Peso") 
  
    with col2:
      x_tab1 = st.number_input("Entrada")
      
    y_tab1 = w_tab1 * x_tab1
      
    st.write("La salida de la neurona es", round(y_tab1, 2))
    
with tab2:
    st.markdown("## Dos entradas")
    
    
    col3, col4 = st.columns(2)
    with col3:
      w0_tab2 = st.slider("Peso 1", 1.0, 10.0)
      x0_tab2 = st.number_input("Entrada 1")
      
    with col4:
      w1_tab2 = st.slider("Peso 2", 1.0, 10.0)
      x1_tab2 = st.number_input("Estrada 2")
      
    st.write("La salida de la neurona es", round(w0_tab2 * x0_tab2 + w1_tab2 * x1_tab2, 2))
    
with tab3:
    st.markdown("## Tres entradas con bias (sesgo)")
    
