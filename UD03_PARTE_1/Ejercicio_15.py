"""Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales
son iguales."""
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 == num2 == num3:
    print("Los tres números son iguales.")
    mayor = num1
    menor = num1
elif num1 >= num2 and num1 >= num3:
    mayor = num1
    if num2 >= num3:
        menor = num3
    else:
        menor = num2
elif num2 >= num1 and num2 >= num3:
    mayor = num2
    if num1 >= num3:
        menor = num3
    else:
        menor = num1
else:
    mayor = num3
    if num1 >= num2:
        menor = num2
    else:
        menor = num1

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
