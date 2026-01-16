import os
import shutil

        



ruta_origen = "C:\\users\\javier\\Downloads"
Ruta = input(f"Introduce carpeta destino almacenara archivos ¡IMPORTANTE! (Se creara la ruta si no existe): ") 
ruta_destino = Ruta.replace(' ', '').replace('\\', '\\\\') 
print(ruta_destino)
if not os.path.exists(ruta_destino):
    with open("D:\\Pruebas2\\ValorVariable.txt", "w") as archivo:
        archivo.write("0")
        print("hola")
if os.path.exist(ruta_destino):
     with open("D:\\Pruebas2\\ValorVariable.txt", "w") as archivo:
          archivo.write("1")

with open("D:\\Pruebas2\\ValorVariable.txt", "r") as a:
     Valor = a.readline()
if Valor == 1:
     
else:
     print()

carpetas_destino = {
   
}
for nombre_archivo2 in os.listdir(ruta_origen): #un bucle lista los elementos de la ruta de origen y les da el valor de la variable nombre_archivo
    nombre2, extension2 = os.path.splitext(nombre_archivo2) #separa el nombre de la extension de los elementos de la variable y le da a la variable extension el valor de las extensiones de los archivos
    carpetas_destino[extension2]= extension2

for extension in carpetas_destino: #para los valores dentro de carpetas destino se los da a la variable extension
    if not os.path.exists(os.path.join(ruta_origen, extension)): #Si no existe la carpeta de la extension en la ruta de origen
        os.makedirs(os.path.join(ruta_destino, extension), exist_ok=True) #Crea las carpetas en la ruta de destino
    #con el exist_ok indicamos que lo ignore si la carpeta ya existe anteriormente

for nombre_archivo in os.listdir(ruta_origen): #un bucle lista los elementos de la ruta de origen y les da el valor de la variable nombre_archivo
    nombre, extension = os.path.splitext(nombre_archivo) #separa el nombre de la extension de los elementos de la variable y le da a la variable extension el valor de las extensiones de los archivos
    # Si el archivo tiene una extensión que queremos organizar
    if extension in carpetas_destino:
            # Construye las rutas de origen y destino
            ruta_origen_archivo = os.path.join(ruta_origen, nombre_archivo)
            ruta_destino_archivo = os.path.join(ruta_destino, carpetas_destino[extension], nombre_archivo)
            
            # Mueve el archivo a la carpeta de destino
            shutil.move(ruta_origen_archivo, ruta_destino_archivo)




