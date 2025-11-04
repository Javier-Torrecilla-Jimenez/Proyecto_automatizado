
#Ruta de origen de los archivos
$origen = "C:\Users\torre\Downloads"

#Ruta destino archivos con extension .pdf
$destino_pdf = "C:\Users\torre\Downloads\Pruebas\PDF"

Move-Item -path C:\Users\torre\Downloads\*.pdf -Destination $destino_pdf -Force


