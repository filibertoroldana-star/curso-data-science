import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title='Curso de Data Science', page_icon='📊', layout='wide')

# Diseño personalizado con CSS para estilizar la interfaz
st.markdown('''
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #1f77b4; font-family: 'Helvetica', sans-serif; }
    h2, h3 { color: #2c3e50; }
    .stDataFrame { border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    </style>
''', unsafe_allow_html=True)

# Título principal traducido y estilizado
st.title('📊 Panel Interactivo de Ciencia de Datos')
st.markdown('Bienvenido al explorador visual de tus prácticas, notebooks y datasets del curso.')

# Menú lateral en español
st.sidebar.header('⚙️ Panel de Navegación')
opcion = st.sidebar.selectbox('Selecciona una sección:', ['🏠 Resumen General', '📁 Explorador de Datasets', '📈 Estadísticas y Prácticas'])

if opcion == '🏠 Resumen General':
    st.subheader('Estado Actual del Proyecto')
    st.info('La aplicación se encuentra conectada correctamente a tu repositorio y desplegada en la nube.')
    
    # Tarjetas de métricas visuales
    col1, col2, col3 = st.columns(3)
    col1.metric('Módulos del Curso', '12', 'Activos')
    col2.metric('Entorno', 'Streamlit & Python', 'Optimizado')
    col3.metric('Estado del Servidor', 'En Línea 🟢', 'Render')

elif opcion == '📁 Explorador de Datasets':
    st.subheader('Visualización del Dataset: StudentsPerformance')
    try:
        df = pd.read_csv('02.Intro a Pandas/StudentsPerformance.csv')
        st.success('¡Archivo cargado con éxito desde el repositorio!')
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.warning('No se pudo localizar el archivo CSV de ejemplo.')

else:
    st.subheader('📈 Sección de Prácticas y Modelos')
    st.write('Aquí puedes integrar los resultados de tus notebooks de Machine Learning, regresiones y gráficas interactivas.')
