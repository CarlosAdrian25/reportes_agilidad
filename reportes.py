import streamlit as st
import pandas as pd
import numpy as np

def mostrar_pagina_visualizacion():
    st.title("REPORTES")
    st.header("Visualización de Datos")
    dic={"mundo":["kamicase"],"Era":[" 2020"]}
    sd=pd.DataFrame(dic)
    print(sd)