#Ruta de origen de los archivos
$origen = "C:\Users\torre\Downloads"
$destino = "D:\Pruebas2\"

$CarpDest = @{
    txt = ".txt" #Indicamos la extensión y su carpeta. 
    pdf = ".pdf"
    jpg = ".jpg"
    ova = ".ova"
}

foreach ($extension in $CarpDest.GetEnumerator()) {
    $CarpeN = Join-path -Path $destino -ChildPath $extension.Value
    if (!(Test-Path $CarpeN)) { #Analiza si la ruta de destino existe
    New-Item -Path $CarpeN -ItemType "Directory" -force # si no existe lo crea
}
    Get-ChildItem -Path $origen -Filter [$extension.Value] -Recurse | Copy-Item -Destination $carpeN    

}






        
