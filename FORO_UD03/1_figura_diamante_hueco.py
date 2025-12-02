asterisco = "*"
espacio = " "
altura = int(input("Introduce la altura del rombo: "))
a = altura
espacios_dentro = " "
k = -1

for i in range(altura - 1):
    if i == 0:
        print((espacio * a) + asterisco + (espacios_dentro * k))
        a = a - 1
        k = k + 2
    else:
        print((espacio * a) + asterisco + (espacios_dentro * k) + asterisco)
        a = a - 1
        k = k + 2

for i in range(altura):
    if i == altura -1:
        print((espacio * a) + asterisco + (espacios_dentro * k))
        a += 1  
        k = k - 2
    else:
        print((espacio * a) + asterisco + (espacios_dentro * k) + asterisco)
        a = a + 1
        k = k - 2

