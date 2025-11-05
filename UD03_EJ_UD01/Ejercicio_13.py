"""Escriba un programa que lea dos números y lo visualiza en orden ascendente."""
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 < num2:
    print("Los números en orden ascendente son:", num1, num2)
else:
    print("Los números en orden ascendente son:", num2, num1)