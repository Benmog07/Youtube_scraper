# Scraper de Comentarios de YouTube

Este proyecto es un scraping de datos en Python que extrae comentarios recientes de videos de YouTube utilizando la API de YouTube Data. Fue desarrollado como parte de un proyecto final del Taller de Econometría II de la Maestría en Economía Aplicada del ITAM.

## Propósito

El objetivo del proyecto es recolectar hasta 40 de los comentarios más recientes de uno o más videos de YouTube (hasta 3 URLs) y guardar los resultados en un archivo CSV para su análisis posterior.

## Estructura del Repositorio

```
api/
├── README.md
├── .gitignore
├── requirements.txt
│
├── code/
│   └── youtube_scraper.py
│
├── data/
    └── final_dataset.csv
```

## Requisitos

Este proyecto utiliza las siguientes librerías:

- google-api-python-client
- python-dotenv

Para instalar las dependencias, ejecuta:

```
pip install -r requirements.txt
```

## Llave de API

Para ejecutar el scraper necesitas una llave de la API de YouTube Data válida.  
Crea un archivo `.env` en la carpeta raíz del proyecto con el siguiente contenido:

```
YOUTUBE_API_KEY=tu_clave_aquí
```

No compartas ni subas tu archivo `.env`. Este archivo está ignorado mediante `.gitignore`.

## Cómo usar

1. Activa tu entorno virtual.  
2. Navega a la carpeta raíz del proyecto.  
3. Ejecuta el script y proporciona entre 1 y 3 URLs de videos de YouTube cuando se te solicite:

```
python code/youtube_scraper.py
```

El script hará lo siguiente:

- Cargará la llave de API desde el archivo `.env`.
- Usará la API de YouTube para extraer los 40 comentarios más recientes de cada video.
- Guardará los resultados combinados en `data/final_dataset.csv`.

## Salida

El archivo final `final_dataset.csv` contendrá las siguientes columnas:

- video_id  
- video_url  
- comment_text  
- author_name  
- published_at  
- like_count

## Estilo y buenas prácticas

El código sigue las convenciones de estilo PEP-8 y no expone datos sensibles ni secretos.

## Licencia

