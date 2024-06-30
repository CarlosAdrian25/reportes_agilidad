import streamlit as st 
from reportes import mostrar_pagina_visualizacion
from archivos import archivo
from analisis import analisis
from Ayuda import ayuda
from streamlit_option_menu import option_menu

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] > div:first-child {
        background-color: #1a1a2e;
    }
    .menu_icon {
        color: #ffd700;  /* Color dorado */
        font-size: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    titulo=st.markdown("<center><h1 style='color: #ffd590;'>🗳 PANEL DE CONTROL</h1></center>", unsafe_allow_html=True)
    selected = option_menu(
        "",
        ["ANALISIS", "SUBIR ARCHIVO", "REPORTES (EXPORTACION)"],
        icons=["wrench", "cloud", "lightbulb"],
        menu_icon="cast",
        default_index=1,
        styles={
            "container": {"padding": "5px", "background-color": "#1a1a2e","color":"white"},
            "icon": {"color": "#ffd700", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "color": "#eaeaea", "--hover-color": "#0f3460"},
            "nav-link-selected": {"background-color": "#16213e"},
        }
    )

# Mostrar contenido basado en la selección
if selected == "ANALISIS":
    st.write("Esta es la página de inicio")
elif selected == "SUBIR ARCHIVO":
    archivo()
elif selected == "REPORTES (EXPORTACION)":
    st.write("Esta es la página de acerca de")






