import streamlit as st
import pandas as pd
import numpy as np


def mostrar_pagina_visualizacion():

    st.title("REPORTES")

    st.header("Visualización de Datos")

    dic = {"mundo": ["kamicase"], "Era": ["2020"]}

    sr = pd.DataFrame(dic)

    st.write(sr)

    st.write(sr.count())

    hola = sr.count()

    # creacion de data view de grados de texto

    st.metric(label="Ventas", value=hola[0], delta=f"{5} %")

    col1,col2,col3=st.columns(3)
    col1.metric("Ventas", hola[0])
    col2.metric("Secciones",hola[0])
    col3.metric("Promedio", hola[0], delta=f"{5} %")