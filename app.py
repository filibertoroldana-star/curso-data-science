import streamlit as st
import pandas as pd

st.title('🚀 Mi Curso de Data Science')
st.write('Exploración de datos y proyectos interactivos en la web.')

try:
    df = pd.read_csv('02.Intro a Pandas/StudentsPerformance.csv')
    st.subheader('Visualización del Dataset (StudentsPerformance)')
    st.dataframe(df.head(10))
except Exception as e:
    st.warning('No se pudo cargar el archivo CSV de ejemplo.')
