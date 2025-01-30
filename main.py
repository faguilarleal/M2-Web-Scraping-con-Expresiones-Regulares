# Web Scraping
# Autores: - Cesar Lopez #22535
#          - Francis Aguilar #22243
#          - Angela Garcia #22869

import re
import csv   
import html
from urllib.parse import urljoin
#acciones que debe de hacer el programa

#abrir un archivo html de la pagina descargada
def cargar_html(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as file:
        return file.read()

#implementar un buffer para procesar el contenido

#usar expresiones regulares para encontrar los nombres de productos y urls de imagenes
def extraer_productos(archivo_html, url_base):
    regex_nombre = r"<h2 class='woocommerce-loop-product__title'\s*>(.*?)</h2>"
    # regex_imagen = r'<img src="(.*?)" alt=".*?" />'
    regex_imagen = r'<img.*?src="(.*?)"(?: alt=".*?")?.*?>'
    nombres = re.findall(regex_nombre, archivo_html)
    imagenes = re.findall(regex_imagen, archivo_html)





    return list(zip(nombres, imagenes))

#generar un archivo exportable, como un .csv con las columnas de "nombre del producto" y "url de la imagen"
#exportar los resultados
def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Nombre del producto', 'Url de la imagen'])
        writer.writerows(productos)


#cargar el archivo
nombre_archivo= 'Trufas & Bombones _ Zurich Guatemala.html'
archivo_html = cargar_html(nombre_archivo)

#extraer los productos y las urls de imagenes
url_base = "https://zurich.com/" #esto nos va a servir, por la img que tiene la imagen
productos = extraer_productos(archivo_html, url_base)


#exportar los resultados en un csv
exportar_csv(productos, 'Trufas_bombones_Zurich_Guatemala.csv')