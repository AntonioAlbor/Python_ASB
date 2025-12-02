"""Programa donde el usuario "piensa" un número del 1 al 100 y el ordenador intenta
adivinarlo. Es decir, el ordenador irá proponiendo números una y otra vez hasta adivinarlo (el
usuario deberá indicarle al ordenador si es mayor, menor o igual al número que ha pensado)"""
print("Piensa un número del 1 al 100 y yo intentaré adivinarlo.")
bajo = 1
alto = 100  
intentos = 0
while True:
    intentos += 1
    adivinanza = (bajo + alto) // 2
    respuesta = input("¿Es", adivinanza, "(mayor/menor/igual): ").lower()
    if respuesta == "igual":
        print("¡He adivinado tu número",adivinanza, "en", intentos,  "intentos!")
        break
    elif respuesta == "mayor":
        bajo = adivinanza + 1
    elif respuesta == "menor":
        alto = adivinanza - 1
    else:
        print("Por favor, responde con 'mayor', 'menor' o 'igual'.")