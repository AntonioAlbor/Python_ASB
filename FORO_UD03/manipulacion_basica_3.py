#Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.

palabra = input("Ingresa una palabra ")
letra = input("Ingresa una letra ")
contador = 0

for i in range (len(palabra)):
    if palabra[i] == letra:
        contador += 1

print("La letra", letra, "aparece", contador, "veces")