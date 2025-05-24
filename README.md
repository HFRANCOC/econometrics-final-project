# Scraper de Comentarios de YouTube – Proyecto Final Econometría II

Este proyecto forma parte del trabajo final del curso *Econometría II*. Consiste en construir un pipeline reproducible para recolectar comentarios de videos de YouTube utilizando la API de YouTube Data v3.

## 🎯 Objetivo

Recolectar comentarios de usuarios de un video específico de YouTube para analizarlos mediante técnicas de texto o aplicaciones econométricas.

## 📁 Estructura del Proyecto

econometrics-final-project/
├── README.md
├── .gitignore
├── .env # NOT included in GitHub
├── requirements.txt # or environment.yml
├── code/
│ └── scrape_comments.py
└── data/
└── dataset.csv # Final dataset with comments

## ⚙️ Instrucciones de Configuración

1. **Clonar el repositorio**

bash
git clone https://github.com/tu-usuario/econometrics-final-project.git
cd econometrics-final-project

2. **Clonar el repositorio**

Con venv:

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

3. **Agrega tu clave de API**

Crea un archivo .env en la raíz del proyecto con el siguiente contenido:

API_KEY =tu_api_key_aquí

🚀 Ejecutar el Scraper
Desde la carpeta raíz:
python code/scrape_comments.py

El script descargará comentarios del siguiente video:

https://www.youtube.com/watch?v=9FcaUhySrbA

Los guardará automáticamente en data/dataset.csv.

📊 Información del Dataset
El archivo CSV generado contiene las siguientes columnas:

comment_id: ID único del comentario

text: contenido del comentario

video_id: ID del video de YouTube

video_title: título del video fuente

El dataset contiene más de 500 comentarios.

📝 Notas
La clave de API se gestiona de forma segura usando dotenv y no se sube a GitHub.

El código cumple con el estándar de estilo PEP-8.

El proyecto está organizado de forma clara y reproducible.