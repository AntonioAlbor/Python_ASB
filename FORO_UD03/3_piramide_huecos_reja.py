asterisco = "*"
espacio = " "
altura = int(input("Introduce la altura del rombo: "))
a = altura - 1
espacios_dentro = " "
k = -1

for i in range(altura - 1):
    if i == 0:
        print((espacio * a) + asterisco + (espacios_dentro * k))
        a = a - 1
        k = k + 2
    elif i == altura //  2:
        print((espacio * a) + (asterisco + espacios_dentro)*(i+1))
        a = a - 1
        k = k + 2
    else:
        print((espacio * a) + asterisco + (espacios_dentro * k) + asterisco)
        a = a - 1
        k = k + 2

print (asterisco * ((altura * 2) - 1))


