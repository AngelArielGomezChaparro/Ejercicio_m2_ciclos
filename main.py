altura = int(input("Ingrese cuántas filas quiere que tenga: "))
ancho = int(input("Ingrese cuántas columnas quiere que tenga: "))

for i in range(altura):
    print("*" * ancho)


altura = int(input("Altura: "))

for i in range(1, altura + 1):
    print("*" * i)



lado = int(input("Lado: "))

# Triángulo superior
for i in range(lado):
    print(" " * (lado - i - 1) + "*" * (2 * i + 1))

# Triángulo inferior
for i in range(lado - 1):
    print(" " * (i + 1) + "*" * (2 * (lado - i - 2) + 1))
