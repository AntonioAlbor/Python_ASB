# Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.

cadena = "palabra"
letra_remplazo= "b"
letra_original = "a"
nueva_cadena = ""


for i in (cadena):
    if i == letra_original:
        nueva_cadena = nueva_cadena + letra_remplazo
    else:
        nueva_cadena += i

print(cadena)
print(nueva_cadena) 