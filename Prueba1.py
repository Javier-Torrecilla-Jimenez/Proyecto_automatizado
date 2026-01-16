import os

ruta_origen = "C:\\users\\torre\\Downloads"
ruta_destino = "D:\\Pruebas3"

if not os.path.exists(ruta_destino):
    with open("ValorVariable.txt", "w") as archivo:
        archivo.write("0")
        print("hola")
 