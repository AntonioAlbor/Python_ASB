"""Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
Visualizar el descuento y el total a pagar por la compra."""

valor_compra = float(input("Ingrese el valor de compra: "))
dia_semana = input("Ingrese el día de la semana: ").lower()
if dia_semana == "martes" or dia_semana == "jueves":
    descuento = valor_compra * 0.15
    total_a_pagar = valor_compra - descuento
    print("Descuento aplicado:", descuento)
    print("Total a pagar:", total_a_pagar)
else:
    print("No se aplica descuento")
    print("Total a pagar:", valor_compra)