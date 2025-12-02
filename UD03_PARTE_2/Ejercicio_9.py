"""Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego
muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos."""

contador_positivos = 0
contador_negativos = 0
ha_leido_negativo = False
while True:
    numero = int(input("Introduce un número no nulo (0 para terminar): "))
    if numero == 0:
        break
    if numero > 0:
        contador_positivos += 1
    else:
        contador_negativos += 1
        ha_leido_negativo = True

print("Se ha leído algún número negativo:", ha_leido_negativo)
print("Números positivos:", contador_positivos)
print("Números negativos:", contador_negativos)