"""Crea una aplicación que dibuje una escalera de números, siendo cada línea un número.
Nosotros le pasamos la altura por teclado"""
altura = int(input("Introduce la altura de la escalera: "))
for i in range(1, altura + 1):
    print(str(i) * i)
    