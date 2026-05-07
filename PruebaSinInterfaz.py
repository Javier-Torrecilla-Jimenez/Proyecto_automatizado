import os
import shutil

        
  #-----Log Ruta Destino-----
func = os.getcwd()+"\\"+".log.txt"
#Ruta del archivo con el que vamos a iterar
func1 = func.replace(' ', '').replace('\\', '\\\\')     
#Ruta del archivo modificada para que python la comprenda de manera correcta
    
if not os.path.exists(func1):
#Si la ruta no existe
    with open(f"{func1}", "w") as archivo:
    # Abre el archivo en modo escritura, con el que iteramos
        archivo.write("0")
        #Escribe el valor string 0
  #-----Log Ruta Origen-----

ori = os.getcwd()+"\\"+".log2.txt"
#Ruta del archivo con el que vamos a iterar
ori1 = ori.replace(' ', '').replace('\\', '\\\\')     
#Ruta del archivo modificada para que python la comprenda de manera correcta

if not os.path.exists(ori1):
#Si la ruta no existe
    with open(f"{ori1}", "w") as archivo:
    # Abre el archivo en modo escritura, con el que iteramos
        archivo.write("0")
        #Escribe el valor string 0

  #---Petición y almacenamiento de la ruta de Destino---
with open(f"{func1}", "r") as archivo:
#Abre el archivo en modo lectura, con el que iteramos
    for valor in archivo:
    #Bucle para el valor dentor de archivo    
        if valor == "0":
        #Si el valor es igual a 0    
            Ruta = input(f"Introduce carpeta destino almacenara archivos ¡IMPORTANTE! Si no existe se crea. Ruta escrita en este formato --> C:\\users\\torre\\Downloads: ") 
            #Pide al usuario que introduzca la ruta de destino de los archivos en su equipo
            ruta_destino2 = Ruta.replace(' ', '').replace('\\', '\\\\')
            with open(f".RutaDest.txt", "w") as archivo:
                archivo.write(ruta_destino2)
            #Ruta del archivo modificada para que python la comprenda de manera correcta
            with open(f"{func1}", "w") as archivo:
            #Abre el archivo en modo escritura
                archivo.write("1")
                #Escribe el valor 1
        else:
            pass     
        #Condicion para cuando el if anterior sea diferente a 0 siga ejecuta el codigo. 
with open(f".RutaDest.txt", "r") as archivo:
    #abre en modo lectura el archivo que hemos creado para almacenar la ruta de origen
    ruta_destino = archivo.readline()

  #---Petición y almacenamiento de la ruta de Origen---

with open(f"{ori1}", "r") as archivo:
    for valor in archivo:
        if valor == "0":
            Ruta_origen = input(f"Introduce la ruta de donde se debe coger los archivos. Ruta escrita en este formato --> C:\\users\\torre\\Downloads): ") 
            #Pide al usuario que introduzca la ruta de origen de los archivos en su equipo
            Ruta_origen2 = Ruta_origen.replace(' ', '').replace('\\', '\\\\')
            with open(f".RutaOri.txt", "w") as archivo:
                archivo.write(Ruta_origen2)
            with open(f"{ori1}", "w") as archivo:
                archivo.write("1")
        else:
            pass     
        #Condicion para cuando el if anterior sea diferente a 0 siga ejecuta el codigo. 
with open(f".RutaOri.txt", "r") as archivo:
    #abre en modo lectura el archivo que hemos creado para almacenar la ruta de origen
    Rut_origenFin = archivo.readline()

#Diccionario almacena todas las extensiones de los archivos que se van a mover
carpetas_destino = {
   
}
for nombre_archivo2 in os.listdir(Rut_origenFin): #un bucle lista los elementos de la ruta de origen y les da el valor de la variable nombre_archivo
    nombre2, extension2 = os.path.splitext(nombre_archivo2) #separa el nombre de la extension de los elementos de la variable y le da a la variable extension el valor de las extensiones de los archivos
    carpetas_destino[extension2]= extension2

for extension in carpetas_destino: #para los valores dentro de carpetas destino se los da a la variable extension
    if not os.path.exists(os.path.join(Rut_origenFin, extension)): #Si no existe la carpeta de la extension en la ruta de origen
        os.makedirs(os.path.join(ruta_destino, extension), exist_ok=True) #Crea las carpetas en la ruta de destino
    #con el exist_ok indicamos que lo ignore si la carpeta ya existe anteriormente

for nombre_archivo in os.listdir(Rut_origenFin): #un bucle lista los elementos de la ruta de origen y les da el valor de la variable nombre_archivo
    nombre, extension = os.path.splitext(nombre_archivo) #separa el nombre de la extension de los elementos de la variable y le da a la variable extension el valor de las extensiones de los archivos
    # Si el archivo tiene una extensión que queremos organizar
    if extension in carpetas_destino:
            # Construye las rutas de origen y destino
            ruta_origen_archivo = os.path.join(Rut_origenFin, nombre_archivo)
            ruta_destino_archivo = os.path.join(ruta_destino, carpetas_destino[extension], nombre_archivo)
            
            # Mueve el archivo a la carpeta de destino
            shutil.move(ruta_origen_archivo, ruta_destino_archivo)



