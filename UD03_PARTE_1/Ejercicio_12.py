"""Escriba un programa que lea un número y dice si es positivo o negativo, consideramos el
cero como positivo."""
num1 = float(input("Ingrese un número"))
num2 = float(input("Ingrese otro número"))
if num1 >= 0:
    print("El número", num1,"es positivo")
else:
    print(f"El número", num2, "es negativo")