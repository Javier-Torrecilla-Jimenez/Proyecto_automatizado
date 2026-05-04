import os  # Librería para trabajar con el sistema de archivos (carpetas, rutas, etc.)
import shutil  # Librería para mover archivos
import tkinter as tk  # Librería para crear la interfaz gráfica
from tkinter import filedialog, messagebox  # Herramientas para seleccionar carpetas y mostrar mensajes

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

# ---------------- FUNCIONES ----------------

def seleccionar_origen():
    global ruta_origen
    ruta_origen = filedialog.askdirectory()
    label_origen.config(text=ruta_origen)

def seleccionar_destino():
    global ruta_destino
    ruta_destino = filedialog.askdirectory()
    label_destino.config(text=ruta_destino)

def abrir_editor_extensiones():
    # Crea una ventana secundaria para añadir extensiones
    ventana_ext = tk.Toplevel(ventana)
    ventana_ext.title("Añadir extensión")
    ventana_ext.geometry("300x200")

    tk.Label(ventana_ext, text="Extensión (ej: .avi)").pack(pady=5)
    entry_ext = tk.Entry(ventana_ext)
    entry_ext.pack()

    tk.Label(ventana_ext, text="Nombre carpeta").pack(pady=5)
    entry_nombre = tk.Entry(ventana_ext)
    entry_nombre.pack()

    def guardar_extension():
        ext = entry_ext.get().strip().lower()
        nombre = entry_nombre.get().strip()

        # Validaciones básicas
        if not ext or not nombre:
            messagebox.showerror("Error", "Rellena todos los campos")
            return

        if not ext.startswith("."):
            messagebox.showerror("Error", "La extensión debe empezar por punto (.)")
            return

        # Añadir al diccionario en tiempo real
        extensiones_map[ext] = nombre

        messagebox.showinfo("OK", f"Añadido: {ext} → {nombre}")
        ventana_ext.destroy()

    tk.Button(ventana_ext, text="Guardar", command=guardar_extension).pack(pady=15)

def ejecutar_proceso():
    if not ruta_origen or not ruta_destino:
        messagebox.showwarning("Error", "Selecciona ambas rutas")
        return

    carpetas_destino = {}

    # Detectar extensiones
    for nombre_archivo in os.listdir(ruta_origen):
        _, extension = os.path.splitext(nombre_archivo)
        if extension:
            carpetas_destino[extension] = extension

    # Crear carpetas
    for extension in carpetas_destino:
        os.makedirs(os.path.join(ruta_destino, extension), exist_ok=True)

    # Mover archivos
    for nombre_archivo in os.listdir(ruta_origen):
        nombre, extension = os.path.splitext(nombre_archivo)

        if extension in carpetas_destino:
            origen = os.path.join(ruta_origen, nombre_archivo)
            destino = os.path.join(ruta_destino, extension, nombre_archivo)

            if os.path.isfile(origen):
                shutil.move(origen, destino)

    # Renombrar carpetas
    for nombre in os.listdir(ruta_destino):
        ruta_completa = os.path.join(ruta_destino, nombre)

        if os.path.isdir(ruta_completa):
            nombre_lower = nombre.lower()

            if nombre_lower in extensiones_map:
                nuevo_nombre = extensiones_map[nombre_lower]
                nueva_ruta = os.path.join(ruta_destino, nuevo_nombre)

                contador = 1
                while os.path.exists(nueva_ruta):
                    nueva_ruta = os.path.join(ruta_destino, f"{nuevo_nombre}_{contador}")
                    contador += 1

                os.rename(ruta_completa, nueva_ruta)

    messagebox.showinfo("Listo", "Archivos organizados correctamente")

# ---------------- INTERFAZ ----------------

ventana = tk.Tk()
ventana.title("Organizador de Archivos")
ventana.geometry("500x320")

btn_origen = tk.Button(ventana, text="Seleccionar carpeta ORIGEN", command=seleccionar_origen)
btn_origen.pack(pady=10)

label_origen = tk.Label(ventana, text="No seleccionada", wraplength=450)
label_origen.pack()

btn_destino = tk.Button(ventana, text="Seleccionar carpeta DESTINO", command=seleccionar_destino)
btn_destino.pack(pady=10)

label_destino = tk.Label(ventana, text="No seleccionada", wraplength=450)
label_destino.pack()

btn_ext = tk.Button(ventana, text="Añadir extensión", command=abrir_editor_extensiones)
btn_ext.pack(pady=10)

btn_ejecutar = tk.Button(ventana, text="Ejecutar organización", command=ejecutar_proceso)
btn_ejecutar.pack(pady=20)

ventana.mainloop()