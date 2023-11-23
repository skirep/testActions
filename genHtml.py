import os
import datetime

def generar_pagina_html(directorio):
    # Obtener la lista de archivos PNG
    archivos_png = [archivo for archivo in os.listdir(directorio) if archivo.lower().endswith('.png')]

    # Crear el contenido HTML
    contenido_html = "<html>\n<body>\n<h1>Archivos PNG en el directorio</h1>\n<table border='1'>\n<tr>\n<th>Nombre del Archivo</th>\n<th>Fecha de Creación</th>\n<th>Link</th>\n</tr>\n"

    # Agregar una fila por cada archivo PNG
    for archivo_png in archivos_png:
        # Generar la ruta completa del archivo
        ruta_completa = os.path.join(directorio, archivo_png)

        # Obtener la fecha de creación del archivo
        fecha_creacion = obtener_fecha_creacion(ruta_completa)

        # Agregar una fila a la tabla HTML con el nombre del archivo, fecha de creación y enlace
        contenido_html += f'<tr>\n<td>{archivo_png}</td>\n<td>{fecha_creacion}</td>\n<td><a href="{ruta_completa}" target="_blank">Link</a></td>\n</tr>\n'

    # Cerrar las etiquetas HTML
    contenido_html += "</table>\n</body>\n</html>"

    # Guardar el contenido en un archivo HTML
    with open("index.html", "w") as archivo_html:
        archivo_html.write(contenido_html)

def obtener_fecha_creacion(ruta_archivo):
    # Obtener la fecha de creación del archivo
    fecha_creacion_timestamp = os.path.getctime(ruta_archivo)
    fecha_creacion = datetime.datetime.fromtimestamp(fecha_creacion_timestamp)
    return fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")

# Especifica el directorio que deseas analizar
directorio_actual = "."  # Puedes cambiar esto al directorio que desees

# Generar la página HTML con la tabla y enlaces
generar_pagina_html(directorio_actual)

print("Página HTML generada exitosamente.")
