"""Programa que lee una secuencia de notas (con valores que van de 0 a 10) que termina con
el valor -1 y nos dice si hubo o no alguna nota con valor 10"""
nota_diez = False
while True: 
    nota = float(input("Introduce una nota (o -1 para terminar): "))
    if nota == -1:
        break
    if nota == 10:
        nota_diez = True

if nota_diez:
    print("Hubo al menos una nota con valor 10.")
else:
    print("No hubo ninguna nota con valor 10.")