# Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas).

cadena = " "
caracter = ""

while caracter != "0":
    if len(caracter) > 1:
        print("Error, ingresa solo un caracter")
    cadena = cadena + caracter
    print(cadena)
    caracter=input("Ingresa un caracter ")

print("La palabra es: ", cadena)