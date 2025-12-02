"""Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos
la altura de la pirámide por teclado. Este es un ejemplo:"""

asterisco = "*"
espacio = " "

altura = int(input("Introduce la altura de la pirámide invertida: "))

k = 0
h = altura * 2 - 1  

for i in range(altura):
    print((espacio * k) + (asterisco * h))
    k = k + 1  
    h = h - 2 