import streamlit as st 

home = st.Page(
    page="vestas/home.py",
    title="Inicio",
    icon=":material/home:",
   # icon="🏠",
   default=True,
)
acerca_de_page= st.Page(
    page="vistas/acerca_de.py",
    title="Acerca de",
    icon=":material/account_circle",
)
project_1 = st.Page(
    page="vistas/ventas.py",
    title="ventas",
    icon="📊",
)
project_2 = st.Page(
    page="vistas/chatbot.py",
    title="Chatbot",
    icon="🤖"
)
pg = st.navigation(
    {
        "Información:":[home, acerca_de_page],
        "Proyectos:":[project_1,project_2],
    }
)
pg.run()