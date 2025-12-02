"""Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre
el porcentaje de descuento realizado."""

precio_articulo = float(input("Introduce el precio del artículo: "))
precio_venta = float(input("Introduce el precio de venta real: "))
descuento = ((precio_articulo - precio_venta) / precio_articulo) * 100
print("El porcentaje de descuento realizado es:" , descuento, "%")