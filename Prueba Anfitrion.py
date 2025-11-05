import os
import shutil

ruta_origen = "C:\\users\\torre\\Downloads"
ruta_destino = "D:\\Pruebas"

carpetas_destino = {
    ".txt": ".txt", #Indicamos la extensión y su carpeta. 
    ".pdf": ".pdf",
    ".jpg": ".jpg",
    ".ova": ".ova", 
    ".pptx": ".pptx",
    ".docx": ".docx",
}

for extension in carpetas_destino: #Si la extension esta en carpetas destino
    if not os.path.exists(os.path.join(ruta_origen, extension)): #Si no existe la carpeta de la extension en la ruta de origen
        os.makedirs(os.path.join(ruta_destino, extension), exist_ok=True) #Crea las carpetas en la ruta de destino
    #con el exist_ok indicamos que lo ignore si la carpeta ya existe anteriormente

for nombre_archivo in os.listdir(ruta_origen):
    # Obtén la extensión del archivo
    nombre, extension = os.path.splitext(nombre_archivo) 
    
    # Si el archivo tiene una extensión que queremos organizar
    if extension in carpetas_destino:
        # Construye las rutas de origen y destino
        ruta_origen_archivo = os.path.join(ruta_origen, nombre_archivo)
        ruta_destino_archivo = os.path.join(ruta_destino, carpetas_destino[extension], nombre_archivo)
        
        # Mueve el archivo a la carpeta de destino
        shutil.move(ruta_origen_archivo, ruta_destino_archivo)
        print(f"'{nombre_archivo}' movido a la carpeta '{carpetas_destino[extension]}'")
    








