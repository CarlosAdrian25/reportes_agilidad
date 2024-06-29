import streamlit as st 
from reportes import mostrar_pagina_visualizacion
from archivos import archivo
from analisis import analisis
from Ayuda import ayuda
from streamlit_option_menu import option_menu

# Crear el menú con iconos
with st.sidebar:
    selected = option_menu(
        "MENU",
        ["ANALISIS", "SUBIR ARCHIVO", "REPORTES (EXPORTACION)"],
        icons=["wrench", "cloud", "lightbulb"],
        menu_icon="cast",
        default_index=1,
        styles={
            "container": {"padding": "5px", "background-color": "#f0f0f0"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "blue"},
        }
    )

# Mostrar contenido basado en la selección
if selected == "Home":
    st.write("Esta es la página de inicio")
elif selected == "Settings":
    st.write("Esta es la página de configuración")
elif selected == "About":
    st.write("Esta es la página de acerca de")






