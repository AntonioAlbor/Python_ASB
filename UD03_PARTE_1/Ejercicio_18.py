"""Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de
10"""
num1 = float(input("Ingrese un número: "))
if num1 % 10 == 0:
    print("El número es múltiplo de 10")
else:
    print("El número no es múltiplo de 10")