
#Ruta de origen de los archivos
$origen = "C:\Users\Admin_Javier\Downloads"

#Ruta destino archivos con extensión .pdf
$destino_pdf = "C:\Users\Admin_Javier\Downloads\Prueba\.pdf"

Move-Item -Path "C:\Users\Admin_Javier\Downloads\*.pdf" -Destination "C:\Users\Admin_Javier\Downloads\Prueba\.pdf" -Force

