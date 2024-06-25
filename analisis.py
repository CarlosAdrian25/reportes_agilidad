import streamlit as st
import matplotlib.pyplot as plt

def analisis():
    st.title("Analisis")
    labels = ['A', 'B', 'C', 'D', 'E']
    sizes = [15, 30, 45, 10, 20]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#6633cc']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    ax.axis('equal')  # Para que el gráfico sea circular
    st.pyplot(fig)