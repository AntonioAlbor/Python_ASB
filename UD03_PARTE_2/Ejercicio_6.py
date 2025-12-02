"""Programa que lea un número positivo N y calcule y visualice su factorial N! Siendo el
factorial:
0! = 1
1! = 1
2! = 2 * 1
3! = 3 * 2* 1
N! = N * (N-1) * (N-2) * … * """

N = int(input("Introduce un número positivo N: "))
factorial = 1
for i in range(1, N + 1):
    factorial *= i
print(f"El factorial de", N, "es", factorial)