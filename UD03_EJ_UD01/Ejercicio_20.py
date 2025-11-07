"""Escriba un programa que lea una calificación numérica entre 0 y 10 y la transforme en la
calificación alfabética, escribiendo el siguiente resultado (switch).
• De 0 a < 3 Muy Deficiente.
• De 3 a < 5 Insuficiente.
• De 5 a < 6 Suficiente.
• De 6 a < 7 Bien.
• De 7 a <9 Notable.
• De 9 a 10 Sobresaliente."""

calificacion = float(input("Ingrese una calificación numérica entre 0 y 10 "))
if calificacion >= 0 and calificacion < 3:
    print("Muy Deficiente")
elif calificacion >= 3 and calificacion < 5:
    print("Insuficiente")
elif calificacion >= 5 and calificacion < 6:
    print("Suficiente")
elif calificacion >= 6 and calificacion < 7:
    print("Bien")
elif calificacion >= 7 and calificacion < 9:
    print("Notable")
elif calificacion >= 9 and calificacion <= 10:
    print("Sobresaliente")
else:
    print("Calificación inválida")