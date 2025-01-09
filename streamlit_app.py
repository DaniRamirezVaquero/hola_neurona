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
      w_tab1 = st.slider("Peso", 0, 10, 5)
  
    with col2:
      x_tab1 = st.number_input("Entrada")
      
    y_tab1 = w_tab1 * x_tab1
      
    st.write("La salida de la neurona es", y_tab1)
    
with tab2:
    st.markdown("## Dos entradas")
    
with tab3:
    st.markdown("## Tres entradas con bias (sesgo)")
    
