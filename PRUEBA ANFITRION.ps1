#Ruta de origen de los archivos
$origen = "C:\Users\torre\Downloads"
$destino = "D:\Pruebas2\"

$CarpDest = @{
    txt = ".txt" #Indicamos la extensión y su carpeta. 
    ova = ".ova"
    jpg = ".jpg"
    pdf = ".pdf"
}

foreach ($extension in $CarpDest.GetEnumerator()) {
    $CarpeN = Join-path -Path $destino -ChildPath $extension.Value # crea la ruta de destino de cada valor de el diccionario y la agrupa en la variable CarpeN
    if (!(Test-Path $CarpeN)) { #Analiza si la ruta de destino existe
    New-Item -Path $CarpeN -ItemType "Directory" -force # si no existe lo crea
    }
    #damos el valor de las claves a la variable de extensionestipo
    $extensionestipo = $extension.Value
#Bucle que realiza la accion de dentro de el por cada valor dentro de la variable de extensionestipo
$extensionestipo| ForEach-Object{ 
    #Coge todos los elementos de la ruta de origen con los valores de la variable y los copai en la ruta de destino 
    Get-ChildItem -Path $origen -filter *$extensionestipo| copy-item -Destination $CarpeN
}
}
$extor = Get-ChildItem -path $origen
$nombre = $extor.BaseName
$ext = $extor.Extension
$ext
$ext| ForEach-Object{
    if 
}

}

