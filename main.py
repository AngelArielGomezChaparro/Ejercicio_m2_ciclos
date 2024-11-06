#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:

import math


numero = int(input("Ingrese el exponente máximo para las potencias de 2: "))


for i in range(numero + 1):
    potencia =  math.pow(2, i)

    print(f"{int(potencia)}")