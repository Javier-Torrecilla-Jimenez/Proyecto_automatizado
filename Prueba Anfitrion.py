import os
import shutil

ruta_origen = "C:\\users\\jtorrecjim\\Downloads"

carpetas_destino = {
    ".txt": ".txt", #Indicamos la extensión y su carpeta. 
    ".pdf": ".pdf",
    ".jpg": ".jpg",
    ".ova": ".ova",
}
for extension in carpetas_destino:
    if not os.path.exists(os.path.join(ruta_origen, extension)):
        os.makedirs(os.path.join(ruta_origen, extension))

for nombre_archivo in os.listdir(ruta_origen):
    # Obtén la extensión del archivo
    nombre, extension = os.path.splitext(nombre_archivo) 
    
    # Si el archivo tiene una extensión que queremos organizar
    if extension in carpetas_destino:
        # Construye las rutas de origen y destino
        ruta_origen_archivo = os.path.join(ruta_origen, nombre_archivo)
        ruta_destino_archivo = os.path.join(ruta_origen, carpetas_destino[extension], nombre_archivo)
        
        # Mueve el archivo a la carpeta de destino
        shutil.move(ruta_origen_archivo, ruta_destino_archivo)
        print(f"'{nombre_archivo}' movido a la carpeta '{carpetas_destino[extension]}'")
    else:
        #Si no se cumple que cree una carpete de la extension
        carpetas_destino = carpetas_destino + [nombre_archivo[extension]]
        print(carpetas_destino)

