#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos 
# los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como 
# resultado 2 + 3 + 4 + 5 + 6 = 20.

print ("escriba dos numeros para sumar todos los q estan dentro de ellos")
numero1 = int(input("escriba su primer numero: "))
numero2 = int(input("escriba el segundo numero: "))

# esta variante if es para q aun el numero primero sea mayor funcione el codigo de todos modos

if numero1 > numero2:

    numero1, numero2 = numero2, numero1
#El comando sum suma una secuencia de numeros proporcionados por el comando range
suma = sum(range(numero1 + 1, numero2))

print(F"La suma de los numero entre {numero1} y {numero2} = {suma}")