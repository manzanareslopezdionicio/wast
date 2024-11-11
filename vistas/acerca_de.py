import streamlit as st 
from forms.contacto import contact_form

@st.dialog("Contacto")
def ver_form_contact():
    contact_form()
    
c1,c2 = st.columns(2, gap="small", vertical_alignment="center")

with c1:
    st.image("img/dioni.png", width=250)
with c2:
    st.title("Dionicio Manzanares Lopez")
    st.write(
        "Analista de datos senior, que ayuda a las empresas apoyando la toma de deciciones basada en datos. Como ciencia de Datos"
    )
    if st.button("Contacto"):
        ver_form_contact()

st.subheader("Experiencias y Calificaciones", anchor=False)
st.write(
    """
    - 7 años de experiencia extrayendo informacion util a partir de datos.
    
    """
)
st.subheader("Habilidades", anchor=False)
st.write(
    """
    - Programacion: Python (scikin-learn, pandas), SQL, VBA
    
    """
)