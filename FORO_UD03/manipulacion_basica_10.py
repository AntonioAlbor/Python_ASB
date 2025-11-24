# Leer una cadena y contar cuántos caracteres son letras mayúsculas.

cadena = input("Introduce una frase: ")
contador_mayus = 0

for i in cadena:
    if i == i.upper():
        contador_mayus += 1
    if i == " ":
        contador_mayus -= 1

print("Hay", contador_mayus, " de mayusculas")