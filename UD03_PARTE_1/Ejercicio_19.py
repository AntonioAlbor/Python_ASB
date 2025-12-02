"""Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,
con el siguiente menú de opciones:
Bienvenido a su Cajero Virtual
1. Ingresar dinero en cuenta
2. Retirar dinero de la cuenta
3. Salir"""
saldo = 1000.0
while True:
    print("Bienvenido a su Cajero Virtual")
    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")
    if opcion == '1':
        ingreso = float(input("Ingrese la cantidad a depositar: "))
        saldo += ingreso
        print(f"Has ingresado", ingreso, "dólares. Tu saldo actual es de:", saldo, "dólares.")
    elif opcion == '2':
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= retiro
            print(f"Has retirado", retiro, "dólares. Tu saldo actual es de:", saldo, "dólares.")
    elif opcion == '3':
        print("Gracias por usar el Cajero Virtual")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")