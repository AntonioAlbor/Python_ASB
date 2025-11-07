"""Escriba un programa que calcula el salario neto semanal de un trabajador en función del
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
• Las primeras 35 horas se pagan a tarifa normal.
• Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
• Las tasas de impuesto son:
o Los primeros 500€ son libres de impuestos.
o Los siguientes 400€ tiene un 25% de impuesto.
o Los restantes un 45% de impuesto.
Escribe el nombre del trabajador, salario bruto, tasas y salario neto."""

num_horas_total = float(
    input("Ingrese el número de horas trabajadas en la semana"))
tarifa_normal = float(input("Ingrese la tarifa normal por hora"))
nombre_trabajador = input("Ingrese el nombre del trabajador")
salario_bruto = 0
num_horas_35 = 35
num_horas_extra = 0

if num_horas_total <= 35:
    salario_bruto = num_horas_total * tarifa_normal
else:
    num_horas_extra = num_horas_total - 35
    salario_bruto = (num_horas_35 * tarifa_normal) + \
        (num_horas_extra * tarifa_normal * 1.5)

    if salario_bruto <= 500:
        tasa_impuesto = 0
        salario_neto = salario_bruto
    else:
        if salario_bruto <= 900:
            tasa_impuesto = (salario_bruto - 500) * 0.25
            salario_neto = salario_bruto - tasa_impuesto
        else:
            tasa_impuesto = (400 * 0.25) + ((salario_bruto - 900) * 0.45)
            salario_neto = salario_bruto - tasa_impuesto
print("Nombre del trabajador:", nombre_trabajador)
print("Salario bruto:", salario_bruto)
print("Tasas de impuesto:", tasa_impuesto)
print("Salario neto:", salario_neto)