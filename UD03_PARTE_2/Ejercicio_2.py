"""Programa que muestre los números pares comprendidos entre el 1 y el 200. Para ello utiliza
un contador y suma de 2 en 2."""

for numero in range(2, 201):
    if numero % 2 == 0:
        print(numero)