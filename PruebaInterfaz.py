import customtkinter as ctk

# ---------------- CONFIGURACIÓN VISUAL ----------------
ctk.set_appearance_mode("dark")  # "light" o "dark"
ctk.set_default_color_theme("blue")


# ---------------- VENTANA PRINCIPAL ----------------
ventana = ctk.CTk()
ventana.title("UI de Prueba - Organizador de Archivos")
ventana.geometry("520x350")

# ---------------- TÍTULO ----------------
titulo = ctk.CTkLabel(
    ventana,
    text="INTERFAZ DE PRUEBA",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=20)

# ---------------- BOTÓN ORIGEN ----------------
btn_origen = ctk.CTkButton(
    ventana,
    text="Seleccionar carpeta ORIGEN",
    command=lambda: print("ORIGEN (sin función)")
)
btn_origen.pack(pady=10)

label_origen = ctk.CTkLabel(
    ventana,
    text="Ruta origen no seleccionada"
)
label_origen.pack()

# ---------------- BOTÓN DESTINO ----------------
btn_destino = ctk.CTkButton(
    ventana,
    text="Seleccionar carpeta DESTINO",
    command=lambda: print("DESTINO (sin función)")
)
btn_destino.pack(pady=10)

label_destino = ctk.CTkLabel(
    ventana,
    text="Ruta destino no seleccionada"
)
label_destino.pack()

# ---------------- BOTÓN AÑADIR EXTENSIÓN ----------------
btn_ext = ctk.CTkButton(
    ventana,
    text="Añadir extensión",
    command=lambda: print("EDITOR EXTENSIONES (sin función)"),
    )
btn_ext.pack(pady=10)

# ---------------- BOTÓN EJECUTAR ----------------
btn_ejecutar = ctk.CTkButton(
    ventana,
    text="Ejecutar organización",
    fg_color="green",
    hover_color="darkgreen",
    command=lambda: print("EJECUTAR (sin función)")
)
btn_ejecutar.pack(pady=20)

# ---------------- LOOP ----------------
ventana.mainloop()