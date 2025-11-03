
#Ruta de origen de los archivos
$origen = "C:\Users\torre\Downloads"

#Ruta destino archivos con extensión .pdf
$destino_pdf = "D:\pruebas\.pdf"

Move-Item -Path "C:\Users\torre\Downloads\*.pdf" -Destination "D:\pruebas\.pdf" -Force


