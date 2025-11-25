# Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes
# (sin listas, usando condiciones y concatenación).

cadena = input("Introduce una cadena: ")
resultado = ""

for i in cadena:
    i = i.lower()

    if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
        resultado += i

print(resultado)