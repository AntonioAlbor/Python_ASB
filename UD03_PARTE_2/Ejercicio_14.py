"""Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura
de la pirámide por teclado. Este es un ejemplo, si introducimos 5 de altura:"""

asterisco = "*"
espacio = " "

altura = int(input("Introduce la altura de la pirámide: "))

k = altura - 1
h = 1

for i in range(altura):
    print((espacio * k) + (asterisco * h))

    k = k - 1      
    h = h + 2  
