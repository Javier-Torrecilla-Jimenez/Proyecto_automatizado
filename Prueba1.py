import os

ruta_origen = "C:\\users\\torre\\Downloads"
ruta_destino = "D:\\Pruebas3"
    if not os.path.exists(os.path.join(ruta_origen, extension)): #Si no existe la carpeta de la extension en la ruta de origen
            os.makedirs(os.path.join(ruta_destino, extension), exist_ok=True) #Crea las carpetas en la ruta de destino
        #con el exist_ok indicamos que lo ignore si la carpeta ya existe anteriormente
        with open("ValorVariable.txt", "w") as archivo:
            archivo.write("0")
            print("hola")
 