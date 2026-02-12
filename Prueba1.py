with open("datos.txt", "r") as re:
    for valores in re:
        valores = valores.lower().strip().replace(" ", "")
        with open("datos_limpios.txt", "a") as wr:
            wr.write(valores + "\n") 
            print(1)
 
 