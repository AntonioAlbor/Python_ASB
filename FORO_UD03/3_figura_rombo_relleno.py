asterisco = "*"
espacio = " "
altura = int(input("Introduce la altura del rombo: "))
a = altura
k = 1

for i in range(altura - 1):
    print((espacio * a) + (asterisco * k))
    a = a - 1
    k = k + 2

for i in range(altura + 1):
    print((espacio * a) + (asterisco * k))
    a += 1
    k = k - 2