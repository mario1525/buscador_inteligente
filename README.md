markdown

# Proyecto de Web Scraping con Django y Scrapy

Este repositorio contiene un proyecto que combina Django y Scrapy para realizar tareas de web scraping y mostrar los datos extraídos en una aplicación web Django.

## Descripción del Proyecto

El proyecto consta de dos partes principales:

1. **Web Scraping con Scrapy**: Utilizamos Scrapy, un framework de scraping web de Python, para extraer datos de sitios web específicos. El programa Scrapy está diseñado para extraer información de manera automatizada y estructurada.

2. **Aplicación Web Django**: Utilizamos Django, un framework web de Python, para construir una aplicación web que mostrará los datos extraídos por Scrapy. La aplicación web permite interactuar con los datos de forma dinámica y proporciona una interfaz fácil de usar.

## Instalación y Configuración

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

1. Clona este repositorio en tu máquina local:

git clone https://github.com/mario1525/buscador_inteligente.git

markdown


2. Instala las dependencias necesarias para Django y Scrapy. Puedes usar `pip` para instalar los paquetes necesarios:

pip install -r requirements.txt

csharp


3. Aplica las migraciones de Django para configurar la base de datos:

python manage.py migrate

markdown


## Uso

- Para ejecutar el programa Scrapy y realizar el scraping web, puedes usar el comando:

scrapy crawl mi_spider -o datos.json

css


- Para ejecutar el servidor de desarrollo de Django y acceder a la aplicación web, utiliza el comando:

python manage.py runserver

yaml


## Contribuir

Si quieres contribuir a este proyecto, ¡eres bienvenido! Siéntete libre de abrir un problema o enviar una solicitud de extracción con tus mejoras.

## Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE).

---
Hecho con ❤️ por [mario1525, robert, sergio](https://github.com/mario1525)
