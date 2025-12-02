"""Programa que lea 100 números no nulos y luego muestre un mensaje indicando cuántos
son positivos y cuantos negativos."""

contador_positivos = 0
contador_negativos = 0 
for _ in range(100):
    numero = int(input("Introduce un número no nulo: "))
    if numero > 0:
        contador_positivos += 1
    else:
        contador_negativos += 1

print("Números positivos:", contador_positivos)
print("Números negativos:", contador_negativos)