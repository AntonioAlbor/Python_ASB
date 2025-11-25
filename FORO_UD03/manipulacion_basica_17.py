# Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez.

cadena = input("Ingresa una cadena: ")
cadena_procesada = cadena.lower()
caracteres_duplicados = ""

for i in cadena_procesada:
    if i not in caracteres_duplicados:
        if cadena_procesada.count(i) > 1:
            caracteres_duplicados += i

print("Los caracteres que se repiten son:", " ".join(caracteres_duplicados))

