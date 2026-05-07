import os  # Librería para trabajar con el sistema de archivos (carpetas, rutas, etc.)
import shutil  # Librería para mover archivos
import tkinter as tk  # Librería para crear la interfaz gráfica
from tkinter import filedialog, messagebox  # Herramientas para seleccionar carpetas y mostrar mensajes
import customtkinter as ctk #Herramienta permite diseñar la interfaz grafica de forma sencilla
import webbrowser #Libreria permite acceder a la web directamente desde un enlace


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
def URL_python():
    webbrowser.open("https://www.python.org/downloads/")
#Función para redirigir a la pagina de descarga de Python 



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

      # Recorremos uno a uno todos los elementos que hay dentro de la carpeta origen
    for nombre_archivo in os.listdir(ruta_origen):

        # Construimos la ruta completa del elemento (carpeta + nombre)
        ruta_archivo = os.path.join(ruta_origen, nombre_archivo)

        if not os.path.isfile(ruta_archivo):
            continue
        #evita todas las carpetas de la carpeta de origen

        _, extension = os.path.splitext(nombre_archivo)
        #Separa el nombre de la extensión de los archivos y se queda solo con el nombre
        
        #convertimos la extensión a minúsculas para que ".PNG" y ".png" se tratem igual
        extension = extension.lower()

        # Si el archivo no tiene extensión (por ejemplo un fichero sin tipo), lo saltamos
        if not extension:
            continue
        
        #Todas las extensiones no pertenecientes a el diccionario se guardan en la carpeta otros
        nombre_carpeta = extensiones_map.get(extension, "Otros")

        #Crea la ruta de destino de los archivos 
        carpeta_destino = os.path.join(ruta_destino, nombre_carpeta)
        
        #Crea carpetas evitando errores
        os.makedirs(carpeta_destino, exist_ok=True)
        
        #Ruta de destino tras ser movido el archivo, es decir, la ruta final
        destino = os.path.join(carpeta_destino, nombre_archivo)
        
        #Si la ruta de destino no existe la crea        
        if not os.path.exists(destino):
            shutil.move(ruta_archivo, destino)
    
    #Muestra mensaje 
    messagebox.showinfo("Listo", "Archivos organizados correctamente")

# ---------------- INTERFAZ GRÁFICA ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
ventana = ctk.CTk()  
# Crea la ventana principals
titulo = ctk.CTkLabel(
    ventana,
    text="ORGANIZADOR DE ARCHIVOS",
    font=("times new roman", 24, "bold")
    )
titulo.pack(pady=(10,0))

titulo = ctk.CTkLabel(
    ventana,
    text="Organiza de forma manual o automatica tus archivos",
    font=("times new roman", 12, "bold")
    )
titulo.pack(pady=(0,0))


inicio = ctk.CTkTabview(ventana,
)
tab_principal = inicio.add("Programa manual")
tab_menu = inicio.add("Manual usuario")
inicio.pack(expand=True, fill="both")

btn_descarga = ctk.CTkButton(tab_menu,
            text="Instalar Python",
            command=URL_python,
            fg_color="red",
            height= 10 
) 
btn_descarga.pack(pady=(5,20))

linea = ctk.CTkFrame(ventana,
            fg_color="grey",
            height=(2),
            width=(900)
)
linea.pack()

frame_botones = ctk.CTkFrame(tab_principal,fg_color="transparent")
frame_botones.pack(pady=(15,5))
#frame para alinear los botones dentro de la ventana

frame_textos = tk.Frame(tab_principal, bg=ventana.cget("bg"))
frame_textos.pack()
#frame para alinear los textos en la ventana 
ventana.title("Organizador de Archivos")  
# Título de la ventana

ventana.geometry("700x550")  
# Tamaño de la ventana


# Botón para seleccionar carpeta origen
btn_origen = ctk.CTkButton(
            frame_botones, 
            text="Seleccionar carpeta ORIGEN", 
            command=seleccionar_origen,
    )
btn_origen.pack(side="left", padx=40)

# Texto que muestra la ruta origen seleccionada
label_origen = tk.Label(frame_textos, 
            text="No seleccionada", 
            bg=ventana.cget("bg"),
            fg="white",
                        )
label_origen.pack(side="left", padx=65)

# Botón para seleccionar carpeta destino
btn_destino = ctk.CTkButton(frame_botones, 
                            text="Seleccionar carpeta DESTINO", 
                            command=seleccionar_destino
                            )
btn_destino.pack(side="left", padx=30)

#flecha = tk.Label(ventana,
#            text="➜",
#            bg=ventana.cget("bg"),
#            font=("arial",20)
#) 
#flecha.place(x=335, y=222)
    
# Texto que muestra la ruta destino seleccionada
label_destino = tk.Label(frame_textos, 
            text="No seleccionada",
            bg=ventana.cget("bg"),
            fg="white", 
            )
label_destino.pack(side="left", padx=65)


# Botón para ejecutar el proceso
btn_ejecutar = ctk.CTkButton(tab_principal, 
            text="Ejecutar organización", 
            command=ejecutar_proceso,
            width=70,
            height=35,
            font= ("Arial", 15, "bold")
            )
btn_ejecutar.pack(pady=20)




ventana.mainloop()  
# Mantiene la ventana abierta (bucle principal de la interfaz)