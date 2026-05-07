import os
import shutil

ruta_origen= "C:\\Users\\Javier\\downloads"
ruta_destino="C:\\Users\\Javier\\Desktop\\Pruebas3"
carpetas_destino={}
extensiones_map = {
    ".png": "Fotos",
    ".jpg": "Fotos",
    ".jpeg": "Fotos",
    ".gif": "Imagenes",
    ".bmp": "Imagenes",
    ".pdf": "PDFs",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".xls": "Excel",
    ".xlsx": "Excel",
    ".ppt": "Presentaciones",
    ".pptx": "Presentaciones",
    ".txt": "Textos",
    ".csv": "CSV",
    ".zip": "Comprimidos",
    ".rar": "Comprimidos",
    ".7z": "Comprimidos",
    ".mp3": "Audio",
    ".mp4": "Video",
    ".exe": "Ejecutables",
    ".py": "Scripts Python"
}
carpetas_destino = {}  
# Diccionario donde guardaremos las extensiones detectadas

# ---------------- DETECTAR EXTENSIONES ----------------
for nombre_archivo in os.listdir(ruta_origen):  
    # Recorre todos los archivos de la carpeta origen

    extension2 = os.path.splitext(nombre_archivo)  
    # Separa el nombre del archivo y su extensión y con la _ decimos que descarte el nombre, puesto que solo interesa la extensión. 

    if extension2:  
        # Si el archivo tiene extensión
        carpetas_destino[extension2[1]] = extension2[1]
        # Guarda la extensión en el diccionario
print(extension2)
# ---------------- CREAR CARPETAS ----------------
for extension in carpetas_destino:  
    # Recorre cada extensión detectada
    destino2 = os.path.join(ruta_destino, extensiones_map[extension2[1]], nombre_archivo)

    print(destino2)
    os.makedirs(os.path.join(ruta_destino, extension), exist_ok=True)  
    # Crea una carpeta con el nombre de la extensión en la ruta destino
    # exist_ok=True evita error si ya existe

# ---------------- MOVER ARCHIVOS ----------------
for nombre_archivo in os.listdir(ruta_origen):
    # Recorre todos los archivos nuevamente

    nombre, extension = os.path.splitext(nombre_archivo)

    if extension in carpetas_destino:
        # Si la extensión está en nuestro diccionario

        origen = os.path.join(ruta_origen, nombre_archivo)
        # Ruta completa del archivo original

        destino = os.path.join(ruta_destino, extension, nombre_archivo)
        # Ruta donde se moverá el archivo

        if os.path.isfile(origen):
            # Verifica que sea un archivo (no carpeta)
            shutil.move(origen, destino2)
            # Mueve el archivo

# ---------------- RENOMBRAR CARPETAS ----------------
for nombre in os.listdir(ruta_destino):
    # Recorre las carpetas creadas en destino y las almacena en la variable nombre

    ruta_completa = os.path.join(ruta_destino, nombre)

    if os.path.isdir(ruta_completa):
        # Verifica que sea una carpeta 

        nombre_bajo = nombre.lower()
        # Convierte el nombre a minúsculas

        if nombre_bajo in extensiones_map:
            # Si la carpeta coincide con una extensión del diccionario

            nuevo_nombre = extensiones_map[nombre_bajo]
            # Obtiene el nombre descriptivo

            nueva_ruta = os.path.join(ruta_destino, nuevo_nombre)


            os.rename(ruta_completa, nueva_ruta)
            # Renombra la carpeta

