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

    # st.metric(label="Ventas", value=hola[0], delta=f"{5} %")

    col1,col2,col3=st.columns(3)
    col1.metric("Ventas", hola[0])
    col2.metric("Secciones",hola[0])
    col3.metric("Promedio", hola[0], delta=f"{5} %")

    #radio de select box

    options = st.multiselect(
    "Seleccione uno o mas productos",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"])

    st.write("You selected:", options)

    #select box de opciones 

    evo = st.selectbox(
    "Select Box",
    ("Email", "Home phone", "Mobile phone")
    )
    st.write("You selected:", evo)

    #un relector de rango.
    start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    value=("red", "blue"))
    st.write("tu seleccionaste desde", start_color, "hasta", end_color)
    
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
    #los graficos de parte de comlums se tiene que pasar por los indices de mi dataframe

    df = pd.DataFrame({
    "col1": np.random.randn(1000) / 50 + 37.76,
    "col2": np.random.randn(1000) / 50 + -122.4,
    "col3": np.random.randn(1000) * 100,
    "col4": np.random.rand(1000, 4).tolist(),
    })

    st.map(df,
      latitude='col1',
      longitude='col2',
      size='col3',
      color='col4')


    