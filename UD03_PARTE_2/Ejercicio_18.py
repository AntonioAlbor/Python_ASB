"""Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia
(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla"""
A = int(input("Introduce el valor de A: "))
B = int(input("Introduce el valor de B: "))

resultado = 1  

for i in range(B):
    resultado = resultado * A   

print("El resultado de", A, "elevado a", B, "es:", resultado)