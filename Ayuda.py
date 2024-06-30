import streamlit as st

def ayuda():
    st.title("Bienvenido Al area de Soporte")
    st.markdown("----")
    st.markdown("## hola al area de soporte")
    st.error("la alta demanda crea lucides en el area de desarrollo")
    array=[" ","ayuda a evo","mantenimiento","error al subir"]
    opcion=st.selectbox("INDIQUE SU ERROR",array)
    if opcion != "ayuda a evo" and opcion !="mantenimiento" and opcion!="error al subir":
        st.markdown("<div style='background-color:#FF0000; padding:10px; border-radius:5px'><span style='color:#FFFFFF'>Eres un huevito</span></div>", unsafe_allow_html=True)
    elif opcion=="ayuda a evo":
        st.error("Te gusta evo")
    elif opcion=="error al subir":
        st.error("primero debes saber estan topando los parametros para la subida de archivos")
    elif opcion=="mantenimiento":
        st.error("parametro de error")