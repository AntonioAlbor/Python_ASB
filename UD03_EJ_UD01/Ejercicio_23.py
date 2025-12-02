"""Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
según sea el caso y el total a pagar de la compra"""

valor_compra = float(input("Ingrese el valor de compra: "))
metodo_pago = input("Ingrese el método de pago (contado/tarjeta): ").lower()

if metodo_pago == "contado":
    descuento = valor_compra * 0.05
    total_a_pagar = valor_compra - descuento
    print("Total a pagar:" , total_a_pagar)
elif metodo_pago == "tarjeta":
    recargo = valor_compra * 0.03
    total_a_pagar = valor_compra + recargo
    print("Total a pagar:", total_a_pagar)
else:
    print("Método de pago no válido. Por favor, ingrese 'contado' o 'tarjeta'.")




