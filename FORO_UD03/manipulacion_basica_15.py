#  Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'.

cadena = input("Ingresa una frase ")
vocal = "aeiou"
cadena_nueva = ""
caracter_nuevo = "*"

for i in cadena:
    if i.lower() in vocal:
        cadena_nueva += i.replace(i, caracter_nuevo)
    else:
        cadena_nueva += i

print(cadena_nueva)