# Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene.

cadena = "Hola a todos 1 2"
cadena_nueva = ""
num = "0123456789"
contador = 0

for i in cadena:
    if i in num:
        cadena_nueva += i
        contador += 1

print("Hay ", contador, " numeros")
numeros_separados = " ".join(cadena_nueva)
print("Los numeros son: ", numeros_separados)
