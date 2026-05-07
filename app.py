import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Predicción: Piedra, Papel o Tijera",
    page_icon="🤖",
    layout="centered"
)

# --- Funciones Auxiliares para el Modelo ---
@st.cache_resource
def load_model_and_labels():
    """Carga el modelo de Keras y las etiquetas, cacheando el resultado para mayor eficiencia."""
    model = tf.keras.models.load_model("keras_model.h5", compile=False)
    with open("labels.txt", "r") as f:
        labels = f.readlines()
    return model, labels

def process_and_predict(image, model, labels):
    """Procesa la imagen y realiza la predicción usando el modelo."""
    # Desactivar notación científica en numpy
    np.set_printoptions(suppress=True)
    
    # Redimensionar a 224x224 (típicamente requerido por modelos exportados de Teachable Machine)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    
    # Convertir a arreglo numpy
    image_array = np.asarray(image)
    
    # Normalizar la imagen
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    
    # Expandir dimensiones para crear el batch
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    
    # Predicción
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = labels[index]
    confidence_score = prediction[0][index]
    
    return class_name.strip(), confidence_score

# --- Interfaz Principal ---
st.title("🤖 Predicción Inteligente")
st.markdown("Carga una imagen o usa tu cámara web para que la Inteligencia Artificial adivine si es Piedra, Papel o Tijera.")

# Cargar modelo de forma cacheada
with st.spinner("Cargando el motor de inteligencia artificial..."):
    model, labels = load_model_and_labels()
    
tab1, tab2 = st.tabs(["📤 Subir Imagen", "📷 Usar Cámara"])

with tab1:
    uploaded_file = st.file_uploader("Elige una imagen (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Imagen Subida", use_column_width=True)
        
        if st.button("Analizar Imagen", use_container_width=True):
            with st.spinner("Procesando..."):
                class_name, confidence = process_and_predict(image, model, labels)
                label_text = class_name[2:] if len(class_name) > 2 else class_name
                
                st.success(f"**Predicción:** {label_text}")
                st.progress(float(confidence))
                st.write(f"**Confianza:** {confidence * 100:.2f}%")
                
with tab2:
    st.info("Concede permisos de cámara a tu navegador para usar esta función.")
    camera_image = st.camera_input("Capturar foto")
    
    if camera_image is not None:
        image = Image.open(camera_image).convert("RGB")
        
        with st.spinner("Analizando captura..."):
            class_name, confidence = process_and_predict(image, model, labels)
            label_text = class_name[2:] if len(class_name) > 2 else class_name
            
            st.success(f"**Predicción:** {label_text}")
            st.progress(float(confidence))
            st.write(f"**Confianza:** {confidence * 100:.2f}%")

# Pie de página global
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'><small>Desplegado en Streamlit Cloud | Integración con modelo Keras .h5</small></p>", unsafe_allow_html=True)
