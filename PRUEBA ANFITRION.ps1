#Ruta de origen de los archivos
$origen = "C:\Users\torre\Downloads"

#Ruta destino archivos con extension .pdf
$destinopdf = "D:\Pruebas2\PDF\"
#con con el ! indicamos que solo se meta a la función del if si el test-path nos devuelve como respuesta false (no existe)
if (!(Test-Path $destinopdf)) { 
    new-item -ItemType Directory -Path $destinopdf -Force    #Fuerza a el sistema a crear la carpeta de la ruta $destino_pdf
}

copy-Item -path C:\Users\torre\Downloads\*.pdf -Destination $destinopdf 
