import streamlit as st
import pandas as pd
import os

def archivo():
    # Espacio para que el contenido no esté oculto detrás del título
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Subida del archivo CSV con una clave única
    uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"], key="file_uploader")

    if uploaded_file is not None:
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

        if st.button("Guardar archivo", key="save_button"):
            # Crear la carpeta 'data' si no existe
            if not os.path.exists('data'):
                os.makedirs('data')

            # Guardar el archivo en la carpeta 'data'
            with open(os.path.join('data', uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.success("El archivo se subió con éxito a la carpeta 'data'.")

    else:
        st.write("Por favor, sube un archivo CSV para proceder con el análisis.")




