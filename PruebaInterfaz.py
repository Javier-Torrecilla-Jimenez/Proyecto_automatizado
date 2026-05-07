import os  # Librería para trabajar con el sistema de archivos (carpetas, rutas, etc.)
import shutil  # Librería para mover archivos
import tkinter as tk  # Librería para crear la interfaz gráfica
from tkinter import filedialog, messagebox  # Herramientas para seleccionar carpetas y mostrar mensajes
import customtkinter as ctk
# Variables globales donde guardaremos las rutas seleccionadas por el usuario
ruta_origen = ""
ruta_destino = ""

# Diccionario que relaciona extensiones con nombres más amigables
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

# Función para seleccionar la carpeta de origen (de donde se cogerán los archivos)
def seleccionar_origen():
    global ruta_origen  # Indicamos que usamos la variable global
    ruta_origen = filedialog.askdirectory()  # Abre un explorador para elegir carpeta
    label_origen.config(text=ruta_origen)  # Muestra la ruta seleccionada en la interfaz

# Función para seleccionar la carpeta de destino (donde se moverán los archivos)
def seleccionar_destino():
    global ruta_destino
    ruta_destino = filedialog.askdirectory()
    label_destino.config(text=ruta_destino)

# Función principal que ejecuta todo el proceso
def ejecutar_proceso():
    # Verifica que el usuario haya seleccionado ambas rutas
    if not ruta_origen or not ruta_destino:
        messagebox.showwarning("Error", "Selecciona ambas rutas")
        return  # Sale de la función si falta alguna ruta

    carpetas_destino = {}  
    # Diccionario donde guardaremos las extensiones detectadas

    # ---------------- DETECTAR EXTENSIONES ----------------
    for nombre_archivo in os.listdir(ruta_origen):  
        # Recorre todos los archivos de la carpeta origen

        _, extension = os.path.splitext(nombre_archivo)  
        # Separa el nombre del archivo y su extensión
        
        if extension:  
            # Si el archivo tiene extensión
            carpetas_destino[extension] = extension  
            # Guarda la extensión en el diccionario

    # ---------------- CREAR CARPETAS ----------------
    for extension in carpetas_destino:  
        # Recorre cada extensión detectada

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
                shutil.move(origen, destino)
                # Mueve el archivo

    # ---------------- RENOMBRAR CARPETAS ----------------
    for nombre in os.listdir(ruta_destino):
        # Recorre las carpetas creadas en destino

        ruta_completa = os.path.join(ruta_destino, nombre)

        if os.path.isdir(ruta_completa):
            # Verifica que sea una carpeta

            nombre_lower = nombre.lower()
            # Convierte el nombre a minúsculas

            if nombre_lower in extensiones_map:
                # Si la carpeta coincide con una extensión del diccionario

                nuevo_nombre = extensiones_map[nombre_lower]
                # Obtiene el nombre descriptivo

                nueva_ruta = os.path.join(ruta_destino, nuevo_nombre)

                contador = 1
                # Contador para evitar sobrescribir carpetas

                while os.path.exists(nueva_ruta):
                    # Si ya existe una carpeta con ese nombre
                    nueva_ruta = os.path.join(ruta_destino, f"{nuevo_nombre}_{contador}")
                    contador += 1

                os.rename(ruta_completa, nueva_ruta)
                # Renombra la carpeta

    messagebox.showinfo("Listo", "Archivos organizados correctamente")
    # Muestra mensaje final

# ---------------- INTERFAZ GRÁFICA ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
ventana = ctk.CTk()  

# Crea la ventana principal

ventana.title("Organizador de Archivos")  
# Título de la ventana

ventana.geometry("500x350")  
# Tamaño de la ventana

# Botón para seleccionar carpeta origen
btn_origen = ctk.CTkButton(
    ventana, 
    text="Seleccionar carpeta ORIGEN", 
    command=seleccionar_origen
    )
btn_origen.pack(pady=10)

# Texto que muestra la ruta origen seleccionada
label_origen = ctk.CTkLabel(ventana, 
                        text="No seleccionada", 
                        wraplength=450)
label_origen.pack()

# Botón para seleccionar carpeta destino
btn_destino = ctk.CTkButton(ventana, text="Seleccionar carpeta DESTINO", command=seleccionar_destino)
btn_destino.pack(pady=10)

# Texto que muestra la ruta destino seleccionada
label_destino = ctk.CTkLabel(ventana, text="No seleccionada", wraplength=450)
label_destino.pack()

# Botón para ejecutar el proceso
btn_ejecutar = ctk.CTkButton(ventana, text="Ejecutar organización", command=ejecutar_proceso)
btn_ejecutar.pack(pady=20)

ventana.mainloop()  
# Mantiene la ventana abierta (bucle principal de la interfaz)