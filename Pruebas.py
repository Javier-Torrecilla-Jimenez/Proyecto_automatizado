usuarios = []
i = 1
while i <= 3:
    n1 = input(f"Dime el {i} nombre: ")
    i += 1
    usuarios.append(n1.strip().lower())
usuarios.sort()
print(usuarios)