# Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres (sin usar los métodos upper() o lower()).

minusculas = "abcdefghijklmnopqrstuvwxyzáéíóúñ"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÑ"
cadena_original = "Hola a todos"
nueva_cadena = ""
for caracter in cadena_original:
    caracter_transformado = caracter
    if caracter in minusculas:
        indice = minusculas.index(caracter)
        caracter_transformado = mayusculas[indice]
    nueva_cadena += caracter_transformado

print(nueva_cadena)
