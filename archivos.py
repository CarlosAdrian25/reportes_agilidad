import streamlit as st
import pandas as pd

def archivo():
    # Espacio para que el contenido no esté oculto detrás del título
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Subida del archivo CSV
    uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

    if uploaded_file is not None:
        if st.button("SUBIR ARCHIVO"):
            st.write("Archivo subido correctamente.")
            # Lee el archivo CSV en un DataFrame de pandas
            df = pd.read_csv(uploaded_file)

            # Muestra el contenido del DataFrame
            st.write("### Contenido del archivo CSV:")
            st.dataframe(df)

            # Ejemplo de análisis: Muestra las primeras filas del DataFrame
            st.write("### Primeras filas del archivo CSV:")
            st.dataframe(df.head())

            # Más análisis y visualizaciones
            st.write("### Descripción estadística del archivo CSV:")
            st.write(df.describe())
        else:
            st.write("Por favor, presiona el botón para subir y procesar el archivo.")
    else:
        st.write("Por favor, sube un archivo CSV para proceder con el análisis.")

