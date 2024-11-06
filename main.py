def collatz_sequence(n):
    secuencia = []
    while n != 1:
        secuencia.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    secuencia.append(1)  # Agregar el último término (1)
    return secuencia

# Solicitar al usuario que ingrese un número
n = int(input("n: "))

# Imprimir la secuencia de Collatz para el número ingresado
secuencia = collatz_sequence(n)
print(" ".join(map(str, secuencia)))

# Graficar los largos de las secuencias de Collatz para los números menores que n
print("\nLongitudes de las secuencias de Collatz:")
for i in range(1, n + 1):
    longitud = len(collatz_sequence(i))
    print(f"{i} {'*' * longitud}")