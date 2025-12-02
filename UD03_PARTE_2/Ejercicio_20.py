"""Programa que dada una cantidad de euros que el usuario introduce por teclado (múltiplo de
5 €) mostrará los billetes de cada tipo que serán necesarios para alcanzar dicha cantidad
(utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar el mínimo de billetes posible.
Por ejemplo, si el usuario introduce 145 el programa indicará que será necesario 1 billete de 100
€, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo 29 billetes de 5, que aunque
sume 145 € no es el mínimo número de billetes posible)."""

cantidad = int(input("Introduce la cantidad de euros (múltiplo de 5): "))

billetes_500 = cantidad // 500
cantidad = cantidad % 500

billetes_200 = cantidad // 200
cantidad = cantidad % 200

billetes_100 = cantidad // 100
cantidad = cantidad % 100

billetes_50 = cantidad // 50
cantidad = cantidad % 50

billetes_20 = cantidad // 20
cantidad = cantidad % 20

billetes_10 = cantidad // 10
cantidad = cantidad % 10

billetes_5 = cantidad // 5
cantidad = cantidad % 5

if billetes_500 > 0:
    print("Billetes de 500€:", billetes_500)
if billetes_200 > 0:
    print("Billetes de 200€:", billetes_200)
if billetes_100 > 0:
    print("Billetes de 100€:", billetes_100)
if billetes_50 > 0:
    print("Billetes de 50€:", billetes_50)
if billetes_20 > 0:
    print("Billetes de 20€:", billetes_20)
if billetes_10 > 0:
    print("Billetes de 10€:", billetes_10)
if billetes_5 > 0:
    print("Billetes de 5€:", billetes_5)