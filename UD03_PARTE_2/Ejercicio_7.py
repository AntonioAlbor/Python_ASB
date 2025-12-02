"""Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún
número negativo o no"""

ha_leido_negativo = False
for _ in range(100):
    numero = int(input("Introduce un número no nulo: "))
    if numero < 0:
        ha_leido_negativo = True

if ha_leido_negativo:
    print("Se ha leído al menos un número negativo")
else:
    print("No se ha leído ningún número negativo")