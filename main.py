def calcular_pi(terminos):
    pi_aproximado = 0
    for n in range(terminos):
        # La fórmula de la serie de Leibniz
        pi_aproximado += ((-1) ** n) / (2 * n + 1)
    
    return 4 * pi_aproximado


decimales = int(input("Introduce el número de decimales que deseas para la aproximación de pi: "))


terminos = 1000000
pi_estimada = calcular_pi(terminos)


print(f"Aproximación de pi con {decimales} decimales: {round(pi_estimada, decimales)}")