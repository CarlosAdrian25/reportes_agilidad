import streamlit as st 
from reportes import mostrar_pagina_visualizacion
from archivos import archivo

# Menú lateral
st.sidebar.title("MENU DE REPORTES ESTADISTICOS")
menu_opciones=st.sidebar.selectbox("Selecciona una opción", ["Carga de Datos", "Visualización de Datos", "Análisis", "Ayuda"])
if menu_opciones=='Carga de Datos':
    archivo()
elif menu_opciones=="Visualización de Datos":
    mostrar_pagina_visualizacion()
elif menu_opciones=="An'alisis":
    st.header("Análisis")
elif menu_opciones=="Ayuda":
    st.header("Ayuda")




