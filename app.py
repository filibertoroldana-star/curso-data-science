import os
import json
import streamlit as st

st.set_page_config(page_title="Resultados del Curso de Data Science", layout="wide")

st.title("?? Visor de Resultados por Carpeta y Ejercicio")
st.markdown("Esta aplicación lee tus notebooks de Jupyter y muestra los ejercicios y resultados organizados.")

root_dir = "."

folders = [f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, f)) and not f.startswith((".", "_"))]
folders.sort()

selected_folder = st.sidebar.selectbox("Selecciona una Carpeta", folders)

if selected_folder:
    folder_path = os.path.join(root_dir, selected_folder)
    files = [f for f in os.listdir(folder_path) if f.endswith(".ipynb")]
    files.sort()
    
    st.header(f"?? Carpeta: {selected_folder}")
    
    selected_file = st.selectbox("Selecciona un Ejercicio (Notebook)", files)
    
    if selected_file:
        file_path = os.path.join(folder_path, selected_file)
        st.subheader(f"?? Ejercicio: {selected_file}")
        
        try:
            # Leer el archivo reemplazando cualquier byte inválido para que nunca falle
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                nb = json.load(f)
                
            for i, cell in enumerate(nb.get("cells", [])):
                if cell["cell_type"] == "code":
                    st.markdown(f"**Código (Celda {i+1}):**")
                    code_text = "".join(cell.get("source", []))
                    st.code(code_text, language="python")
                    
                    outputs = cell.get("outputs", [])
                    if outputs:
                        st.markdown("**Resultado:**")
                        for output in outputs:
                            if "text" in output:
                                st.text("".join(output["text"]))
                            elif "data" in output and "text/plain" in output["data"]:
                                st.text("".join(output["data"]["text/plain"]))
                            elif "data" in output and "text/html" in output["data"]:
                                st.markdown("".join(output["data"]["text/html"]), unsafe_allow_html=True)
                    st.divider()
        except Exception as e:
            st.error(f"Error al leer el archivo: {e}")

