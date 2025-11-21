#Ruta de origen de los archivos
$origen = "C:\Users\torre\Downloads"

#Ruta de origen de los archivos
$origen = "C:\Users\torre\Downloads"

#Ruta destino archivos con extension .pdf
$destinopdf = "D:\Pruebas2\PDF\"
$destinoTXT = "D:\Pruebas2\TXT\"


if (!(Test-Path $destinopdf)) {
    New-Item -Path $destinopdf -ItemType "Directory" -force No 
  
}
copy-Item -path C:\Users\torre\Downloads\*.pdf -Destination $destinopdf 
        
