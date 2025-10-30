
#Ruta de origen de los archivos
$origen = "C:\Users\jtorrecjim\Downloads"

#Ruta destino archivos con extensión .pdf
$destino_pdf = "C:\Users\jtorrecjim\Downloads\Prueba\.pdf"

Move-Item -Path "C:\Users\jtorrecjim\Downloads\*.pdf" -Destination "C:\Users\jtorrecjim\Downloads\Prueba\.pdf" -Force

