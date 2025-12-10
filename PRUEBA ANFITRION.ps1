#Ruta de origen de los archivos
$origen = "C:\Users\torre\Downloads\"
$destino = "D:\Pruebas2\"

$CarpDest = @{
    txt = ".txt" #Indicamos la extensión y su carpeta. 
    ova = ".ova"
    jpg = ".jpg"
    pdf = ".pdf"
}



$extd = Get-ChildItem -path $origen -File #Le da a la variable el valor de los items de la ruta de origen
$exts = $extd.Extension.TrimStart('.') #Le da a la vairbale el valor de la extensiones pero le elimina el . del principio

foreach ($ext2 in $extd.Extension){ #Bucle para cada objeto dentro de la variable ext
    if ($CarpDest -notcontains $ext){ # Ejecuta el codigo de abajo si el diccionario no contiene alguna de las extension de la variable ext
        foreach ($ext1 in $extd) { #Para cada valor de extd le da la extension ext1
            $CarpDest[$exts] = $ext2 #Añade claves de clave-valor al diccionario
        }
    }

    foreach ($extension in $CarpDest.GetEnumerator()) {
    $CarpeN = Join-path -Path $destino -ChildPath $extension.Value # crea la ruta de destino de cada valor de el diccionario y la agrupa en la variable CarpeN
    if (!(Test-Path $CarpeN)) { #Analiza si la ruta de destino existe
    New-Item -Path $CarpeN -ItemType "Directory" -force # si no existe lo crea
    }
   
}
 #damos el valor de las claves a la variable de extensionestipo
    $extensionestipo = $extension.Value
#Bucle que realiza la accion de dentro de el por cada valor dentro de la variable de extensionestipo
    $extensionestipo| ForEach-Object{ 
    #Coge todos los elementos de la ruta de origen con los valores de la variable y los copai en la ruta de destino 
    Get-ChildItem -Path $origen -filter *$extensionestipo| move-item -Destination $CarpeN
    }
}



