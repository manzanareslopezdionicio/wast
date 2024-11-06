import json
import requests
import streamlit as st 
from streamlit_lottie import st_lottie

# https://lottie.host/b3c021a4-5f01-463b-9f10-bff1cf8a9321/vuKeufZXEy.json

def get(path:str):
    with open(path, "r") as p:
        return json.load(p)

#Incio de pagina
with st.container():
    st.subheader("Bienvenidos, Somos SOFTIA 🙋‍♀️")
    st.title("Creamos soluciones para acelerar su negocio")
    st.write(
        "Somos unos apacionados de las tecnologias y la innovacion, especializados en el sector de la digitalizacion y automatizacion de negocios. Nos gusta crear soluciones para resolver problemas y mejoras de proceso"
    )
    st.write("[Saber más ⋙](https://emojidb.org/peaple-emojis)")
#Sobre nosotros
with st.container():
    st.write("---")
    I_columna, d_columna = st.columns((2))
    with I_columna:
        st.subheader("Sobre nosotros 👩🏾‍🤝‍👩🏼")
        st.write(
            """ 
            Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.
            Seguramente te vamos a poder ayudar si:

            - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
            - Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido para tu negocio
            - No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos
            - Quieres mejorar la experiencia de tus clientes
            - Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo

            **Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página**
            """
        )
        st.write("[Más sobre nosotros ⋙](https://emojidb.org/peaple-emojis)")
    with d_columna:
        path = get("animacion/Ani.json")
        st_lottie(path)
        
    #Servicios
with st.container():
    st.write("---")
    st.subheader("Servicios")
    imagen_columna, texto_columba = st.columns((1,2))
    with imagen_columna:
        st.image("img/diseño.jpg")
    with texto_columba:
        st.subheader("Diseño de aplicaciones")
        st.write(
            """ 
            Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarios.
            """
        )
        st.write("[Más sobre nosotros ⋙](https://emojidb.org/peaple-emojis)")

with st.container():
    st.write("---")
    
    imagen_columna, texto_columba = st.columns((1,2))
    with imagen_columna:
        st.image("img/proceso.jpg")
    with texto_columba:
        st.subheader("Automatizacion de procesos")
        st.write(
            """ 
            Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarios.
            """
        )
        st.write("[Más sobre nosotros ⋙] https://emojidb.org/peaple-emojis")         
  
with st.container():
    st.write("---")
    
    imagen_columna, texto_columba = st.columns((1,2))
    with imagen_columna:
        st.image("img/datos.jpg")
    with texto_columba:
        st.subheader("Visualizacion de Datos")
        st.write(
            """ 
            Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarios.
            """
        )
        st.write("[Más sobre nosotros ⋙] https://emojidb.org/peaple-emojis")

#contactos
st.subheader("Contacto")

form = st.form(key="home", clear_on_submit=True)
with form:
    input_nombre = st.text_input("Nombre:", placeholder="Escriba su nombre")
    input_email = st.text_input("Correo electrónico:", placeholder="Escriba su E-mail")
    input_area = st.text_area("Comentario:")
    button_submit = form.form_submit_button("Enviar")

#footer
with st.container():
    st.write("---")
    p1, p2, p3 = st.columns((3))
    with p1:
        st.subheader("Contactos:")
        st.write("***Direccion:*** Juigalpa, Chontales-Nicaragua")
        st.write("***Telefono:*** +(505) 0000-0000")
    with p2:
        st.subheader("Servicios")
        st.write("Diseño de Aplicaciones")
        st.write("Automatización de procesos")
        st.write("Visualización de datos")
    with p3:
        st.subheader("Redes Sociales")
        st.markdown("[YOUTUBE](https://www.youtube.com/)")
        st.markdown("[Facebook](https://www.youtube.com/)")
        st.markdown("[Instagram](https://www.youtube.com/)")
