# Leer una cadena y eliminar todos los espacios, construyendo una cadena continua.

cadena = "Hola a todos"
cadena_nueva = ""

for i in cadena:
    if i != " ":
        cadena_nueva += i

print(cadena_nueva)