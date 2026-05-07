# 🧠 Proyecto de Clasificación: Piedra, Papel o Tijera

Bienvenido al repositorio de este proyecto de Machine Learning. Este proyecto demuestra el ciclo de vida completo de un modelo de Deep Learning, desde su entrenamiento hasta su despliegue en producción con una arquitectura separada para mejor escalabilidad y presentación.

## 🏗️ Arquitectura del Proyecto

El despliegue está dividido en dos partes principales:

1. **Front-End Informativo (GitHub Pages):** Un archivo estático `index.html` sirve como *Landing Page*. Documenta la teoría del proyecto, los objetivos, el equipo de desarrollo y provee un punto de entrada atractivo.
2. **Aplicación de Predicción (Streamlit Cloud):** El archivo `app.py` contiene exclusivamente la lógica de inferencia, encargada de recibir las imágenes de los usuarios (por subida o cámara web) y pasarlas por el modelo de Keras para predecir si es Piedra, Papel o Tijera.

## ⚙️ Funcionalidades de la App (Streamlit)

- **Predicción con Imágenes:** Permite al usuario subir una imagen (jpg, jpeg, png) para que el modelo realice la predicción.
- **Predicción en Tiempo Real (Webcam):** Permite utilizar la cámara web del dispositivo para capturar una imagen al instante y clasificarla.
- **Resultados en Tiempo Real:** Barra de progreso y métrica de confianza (Accuracy) para la inferencia.

## 🛠️ Tecnologías Utilizadas

- **HTML5 / CSS3:** Para la Landing Page.
- **Python 3.9+** y **Streamlit**: Para el despliegue del modelo predictivo.
- **TensorFlow / Keras**: Carga del modelo `.h5` e inferencia en batch.
- **Pillow (PIL) y NumPy**: Procesamiento y transformación de imágenes al formato (224x224).

## 🚀 Instalación y Ejecución Local

### Probar la Landing Page
Simplemente abre el archivo `index.html` en cualquier navegador web. No requiere servidor.

### Probar la Aplicación Streamlit Localmente
1. **Crear un entorno virtual** (recomendado):
   ```bash
   python -m venv venv
   # Activar en Windows
   venv\Scripts\activate
   # Activar en Mac/Linux
   source venv/bin/activate
   ```
2. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecutar la aplicación**:
   ```bash
   streamlit run app.py
   ```

## 🌐 Pasos para Despliegue Público

1. **GitHub Pages (Landing Page):**
   - Sube este repositorio a tu cuenta de GitHub.
   - Ve a `Settings` > `Pages` y selecciona desplegar desde la rama principal (`main`).
   - GitHub te proveerá un enlace público (ej. `https://tu-usuario.github.io/tu-repo/`).

2. **Streamlit Community Cloud (App de Predicción):**
   - Inicia sesión en [Streamlit Cloud](https://streamlit.io/cloud).
   - Crea una nueva aplicación apuntando a este mismo repositorio de GitHub y selecciona el archivo `app.py`.
   - Una vez desplegado, copia la URL pública que te dé Streamlit.

3. **¡Conecta ambas piezas!**
   - Abre el archivo `index.html` en tu editor de código.
   - Busca el enlace temporal `<a href="#" id="app-link" class="cta-button">` y reemplaza el `#` por la URL de tu aplicación en Streamlit.
   - Sube los cambios (push) a GitHub para actualizar la Landing Page.
