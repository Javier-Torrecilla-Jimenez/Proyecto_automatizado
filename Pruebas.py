import os
import shutil
        

func = os.getcwd()+"\\"+".verificacion.txt"
print(func)
#Ruta del archivo con el que vamos a iterar
func1 = func.replace(' ', '').replace('\\', '\\\\')     

#Ruta del archivo modificada para que python la comprenda de manera correcta
ruta_origen = "C:\\users\\torre\\Downloads"
#Ruta origen de donde cogera los archivosS
existe = bool()
if not os.path.exists(func1):
    existe = False
else:
    existe = True  
print(existe)
with open(func1, "w") as write:
    if existe == False :
    #Si la ruta no existe
        # Abre el archivo en modo escritura, con el que iteramos
            write.write("0")
            #Escribe el valor string 0
    if existe:
        with open(func1, "r") as read:
            for linea in read:
                if linea == 0:
                    write.write("1")
                else:
                    pass
 
with open(f"{func1}", "r") as archivo:
#Abre el archivo en modo lectura, con el que iteramos
    for valor in archivo:
    #Bucle para el valor dentor de archivo    
        if valor == "0":
        #Si el valor es igual a 0    
            Ruta = input(f"Introduce carpeta destino almacenara archivos ¡IMPORTANTE! (Si no existe se crea. Ruta escrita en este formato --> C:\\users\\torre\\Downloads): ") 
            #Pide al usuario que introduzca la ruta de destino de los archivos en su equipo
            ruta_destino2 = Ruta.replace(' ', '').replace('\\', '\\\\')
            with open(f".log2.txt", "w") as archivo:
                archivo.write(ruta_destino2)
            #Ruta del archivo modificada para que python la comprenda de manera correcta
            with open(f"{func1}", "w") as archivo:
            #Abre el archivo en modo escritura
                archivo.write("1")
                #Escribe el valor 1
        else:
            pass     
        #Condicion para cuando el if anterior sea diferente a 0 siga ejecuta el codigo. 
print("hola")
with open(f".log2.txt", "r") as archivo:
    #abre en modo lectura el archivo que hemos creado para almacenar la ruta de destino
    ruta_destino = archivo.readline()

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




