# Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.

cadena = "HolA a todos"
vocales = "aeiou"
nueva_cadena= ""

for i in cadena:
    if i.lower() in vocales:
        nueva_cadena += i*2
    else:
        nueva_cadena += i


print(nueva_cadena)