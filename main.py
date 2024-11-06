
# Inicializar variables
potencia = 1
fraccion = 0.5
suma_acumulada = 0.0

# Imprimir encabezado
print(f"{'Potencia':<10} {'Fraccion':<10} {'Suma':<10}")

# Calcular potencias fraccionales de dos
while fraccion > 0.000001:
    suma_acumulada += fraccion
    print(f"{potencia:<10} {fraccion:<10.6f} {suma_acumulada:<10.6f}")
    
    # Incrementar la potencia y calcular la siguiente fracción
    potencia += 1
    fraccion /= 2  # Cada fracción es la mitad de la anterior