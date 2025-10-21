import streamlit as st 
import pandas as pd
import plotly.express as px
import datetime

st.subheader("Filtrar Datos y Captura de Datos")
st.write("El procesamiento de datos a traves Ciencia de Datos usando Streamlit de Python")

#Crear 3 columnas y filtrar por nombre del pais, minimo de hijos y expectativa de vida
c1, c2, c3 = st.columns((3))

with c1:
    par_nombrePais = st.text_input("Pais:", placeholder="Escriba nombre del Pais")

with c2:
    par_fertilidad = st.number_input("Minimo numero de Hijos:", min_value=0, max_value=100, step=1)

with c3:
    par_rangoExpectativaVida=st.slider("Rango de Expectativa de Vida:", min_value=10, max_value=100, value=(10,100))


dfDatos = pd.read_csv('http://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv')

#Seleccionar datos de la tabla
if par_nombrePais!="":
    dfDatos=dfDatos[dfDatos["country"].str.upper().str.contains(par_nombrePais.upper())]
    
if par_fertilidad>0:
    dfDatos=dfDatos[dfDatos["fertility"]>=par_fertilidad]

dfDatos=dfDatos[(dfDatos["lifeExpectancy"]>=par_rangoExpectativaVida[0]) & (dfDatos["lifeExpectancy"]<=par_rangoExpectativaVida[1])]
    
st.metric("***Registros Totales***", len(dfDatos))
st.dataframe(dfDatos, use_container_width=True)