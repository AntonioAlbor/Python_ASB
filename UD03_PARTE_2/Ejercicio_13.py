"""Crea una aplicación que dibuje una escalera de números, siendo cada línea números
empezando en uno y acabando en el numero de la línea. Este es un ejemplo, si introducimos un
5 como altura"""

altura = int(input("Introduce la altura de la escalera: "))

for i in range(1, altura + 1):
    numero = 0
    for j in range(1, i + 1):
        numero = numero * 10 + j
    print(numero)