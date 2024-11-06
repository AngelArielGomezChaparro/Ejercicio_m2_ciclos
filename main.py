def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


n = 10  # Comenzar desde 10!
suma_e = 0.0
ultimo_termino = 1.0  # Para el primer término (1/10!)
diferencia = float('inf')  # Inicializar con infinito


while diferencia >= 0.0001:
    nuevo_termino = 1 / factorial(n)
    suma_e += nuevo_termino
    
    
    if n > 10:  # Para evitar la diferencia inicial
        diferencia = abs(nuevo_termino - ultimo_termino)
    
    ultimo_termino = nuevo_termino
    n += 1  # Incrementar n para calcular el siguiente factorial


print(f"Valor aproximado de e: {suma_e + 1}")  # Agregar el 1 por el término 1/0!