import streamlit as st 

#Incio de pagina
with st.container():
    st.subheader("Bienvenidos, Somos SOFTIA 🙋‍♀️")
    st.title("Creamos soluciones para acelerar su negocio")
    st.write(
        "Somos unos apacionados de las tecnologias y la innovacion, especializados en el sector de la digitalizacion y automatizacion de negocios. Nos gusta crear soluciones para resolver problemas y mejoras de proceso"
    )
    st.write("[Saber más ⋙] https://emojidb.org/peaple-emojis")
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
        st.write("[Más sobre nosotros ⋙] https://emojidb.org/peaple-emojis")
    #with d_columna:
    #    st.empty
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
        st.write("[Más sobre nosotros ⋙] https://emojidb.org/peaple-emojis")

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
                 