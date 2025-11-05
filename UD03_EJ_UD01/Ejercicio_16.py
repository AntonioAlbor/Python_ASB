"""Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene."""
num1 = input("Ingresa un número: ")
num_digitos = len(num1.strip())
print("El número tiene", num_digitos, "dígitos")