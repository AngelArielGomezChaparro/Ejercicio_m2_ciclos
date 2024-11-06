#Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los 
#tramos del viaje.
#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo 
#total de viaje en formato horas:minutos.
#El programa deja de pedir tiempos de viaje cuando se ingresa un 0.





print("Ingrese la duración de cada tramo en minutos (ingrese 0 para finalizar)")


duraciones = []


while True:
    duracion = int(input("Duración tramo: "))
    if duracion == 0:
        break  # Termina el bucle si se ingresa 0
    duraciones.append(duracion)  # Agregar la duración del tramo a la lista


tiempoTotalMinutos = sum(duraciones)
horas = tiempoTotalMinutos // 60
minutos = tiempoTotalMinutos % 60


print(f"El tiempo total de tramo a sido: {horas} horas con {minutos} minutos")

                
