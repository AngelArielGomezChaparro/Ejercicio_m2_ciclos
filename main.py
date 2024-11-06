#Escriba un programa que entregue todos los divisores del número entero ingresado:

numeroint = int(input("escriba un numero para darle todos los divisores: "))

divisores = []

for i in range(1, numeroint + 1):
    if numeroint % i == 0:
        divisores.append(i)



    
         
print(f"los divisores de {numeroint} son: {divisores}")
                
