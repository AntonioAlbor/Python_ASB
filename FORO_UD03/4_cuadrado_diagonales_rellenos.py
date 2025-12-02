
numero=int(input("escribe un numero: "))
asterisco="*"
espacio=" "
print(asterisco*numero)
for i in range (1,numero//2+1):
    print(asterisco + (espacio*i) + asterisco + espacio * ((numero//2-i) +1) + asterisco)

for i in range (1,numero//2):
    print(asterisco + (espacio * (numero//2-i)) + asterisco + (espacio *(i+1)) + asterisco)

print(asterisco*numero)