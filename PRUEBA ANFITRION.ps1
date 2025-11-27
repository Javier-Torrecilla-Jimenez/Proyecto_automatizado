#Ruta de origen de los archivos
$origen = "C:\Users\torre\Downloads"
$destino = "D:\Pruebas2\"

#Ruta destino archivos con extension .pdf
$destinopdf = "D:\Pruebas2\PDF\"
$carpetas_destino = @{
    "txt" = ".txt" #Indicamos la extensión y su carpeta. 
    "pdf" = ".pdf"
    "jpg" = ".jpg"
    "ova" = ".ova"
}
foreach ($extension in $carpetas_destino) {
    Join-path -Path $destinopdf -ChildPath $extension # si no existe lo crea
    
}

if (!(Test-Path $destinopdf)) { #Analiza si la ruta de destinopdf existe
    New-Item -Path $destinopdf -ItemType "Directory" -force # si no existe lo crea
}

copy-Item -path $origen*$extension -Destination $destinopdf 
        
