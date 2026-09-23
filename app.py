import streamlit as st
import pandas as pd
import os

st.title('🚀 Explorador Automático del Curso de Data Science')
st.write('Selecciona un módulo y visualiza los datasets y resultados de tus prácticas.')

# Buscar archivos CSV disponibles en el repositorio
csv_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.csv'):
            csv_files.append(os.path.join(root, file))

if csv_files:
    st.sidebar.header('📂 Selector de Datasets')
    selected_csv = st.sidebar.selectbox('Elige un archivo de datos:', csv_files)
    
    st.subheader(f'Visualizando: {selected_csv}')
    try:
        df = pd.read_csv(selected_csv, encoding='utf-8', on_bad_lines='skip')
        st.write(f'**Dimensiones del Dataset:** {df.shape[0]} filas y {df.shape[1]} columnas')
        st.dataframe(df.head(20))
        
        st.subheader('📈 Resumen Estadístico')
        st.write(df.describe())
    except Exception as e:
        st.error(f'No se pudo leer el archivo: {e}')
else:
    st.warning('No se encontraron archivos CSV en el repositorio.')
