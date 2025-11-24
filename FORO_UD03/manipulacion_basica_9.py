# Leer una cadena y contar cuántas vocales contiene.

vocales_minus = "aeiou"
vocales_mayus = "AEIOU"
cadena = input("Ingresa una frase: ")
contador_vocales = 0

for i in cadena:
    for k in vocales_minus:
        if i == k:
            contador_vocales  += 1
    for m in vocales_mayus:
        if i == m:
            contador_vocales += 1

print("Hay ", contador_vocales, " vocales")