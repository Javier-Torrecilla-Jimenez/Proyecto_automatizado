#Ruta de origen de los archivos
$origen = "C:\Users\torre\Downloads"

#Ruta destino archivos con extension .pdf
$destinopdf = "D:\Pruebas2\PDF\"

copy-Item -path C:\Users\torre\Downloads\*.pdf -Destination $destinopdf 

