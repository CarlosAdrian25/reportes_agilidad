import streamlit as st 
import pandas as pd

# Título de la aplicación
st.markdown("""
    <style>
    .title-container {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        background-color: white;
        padding: 10px;
        z-index: 1000;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
    }
    </style>
    <div class="title-container">
        <p class="title">CARGA DE DATOS</p>
    </div>
    """, unsafe_allow_html=True)

# Espacio para que el contenido no esté oculto detrás del título
st.markdown("<br><br><br>", unsafe_allow_html=True)

# Subida del archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Lee el archivo CSV en un DataFrame de pandas
    df = pd.read_csv(uploaded_file)

    # Muestra el contenido del DataFrame
    st.write("Contenido del archivo CSV:")
    st.dataframe(df)

    # Ejemplo de análisis: Muestra las primeras filas del DataFrame
    st.write("Primeras filas del archivo CSV:")
    st.dataframe(df.head())

    # Puedes agregar más análisis y visualizaciones aquí
    st.write("Descripción estadística del archivo CSV:")
    st.write(df.describe())

# Menú lateral
st.sidebar.title("MENU DE REPORTES ESTADISTICOS")
menu_opciones=st.sidebar.selectbox("Selecciona una opción", ["Carga de Datos", "Visualización de Datos", "Análisis", "Ayuda"])
if menu_opciones=='Carga de Datos':
    st.header(" ") #nota se debe de colocar los datos en apartados
elif menu_opciones=="Visualización de Datos":
    st.markdown(" ")
    st.header("Visualización de Datos")
elif menu_opciones=="An'alisis":
    st.header("Análisis")
elif menu_opciones=="Ayuda":
    st.header("Ayuda")
    st.write(reportes.datos)
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #007880; /* Green background */
        color: white; /* White text */
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# Botón con nuevo estilo
if st.button("SUBIR ARCHIVO"):
    st.write("Archivo subido correctamente.")


