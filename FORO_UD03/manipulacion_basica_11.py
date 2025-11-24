# Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.

cadena = "Hola a todos"
vocales = "aeiou"

for i in cadena:
    if i == vocales.lower():
        i += i
        print(i)