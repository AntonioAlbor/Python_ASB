asterisco = "*"
espacio = "·"
altura = int(input("Introduce la altura del rombo: "))
a = altura // 2 - 1
espacios_dentro = "·"
k = 0

print(espacio * altura)
for i in range(altura // 2 - 1):
        print((espacio * k) + asterisco + (espacios_dentro * a) + asterisco + (espacios_dentro * a) + asterisco)
        a = a -1
        k = k + 1

print (asterisco * altura)
a += 1
k -= 1

for l in range(altura // 2 -1):
        print((espacio * k) + asterisco + (espacios_dentro * a) + asterisco + (espacios_dentro * a) + asterisco)
        a = a +1
        k = k -1
print(espacio * altura)