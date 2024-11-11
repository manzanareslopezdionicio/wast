import re
import streamlit as st 
import time

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern,email) is not None

def contact_form():
    with st.form("contact_form"):
        nombre = st.text_input("Nombre:", placeholder="Escriba su nombre")
        email= st.text_input("Correo Electronico:", placeholder="email@gmail.com")
        mensaje = st.text_area ("Mensaje:")
        submit_button = st.form_submit_button("Enviar", use_container_width=True)

    if submit_button:
        if not nombre:
            st.error("Por favor escriba su nombre.")
            st.stop()
        if not email:
            st.error("Por favor escriba su direccion de correo electronico")
            st.stop()    
        if not is_valid_email(email):
            st.error("Por favor su direccion de correo electronico no es correcta")
            st.stop()
        if not mensaje:
            st.error("Por favor escriba un mensaje")
            st.stop()
        if submit_button:
            st.success("Se envio satisfactoriamente")