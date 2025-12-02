"""Programa que muestre en líneas separadas lo siguiente:
ZYWXVUTSRQPONMLKJIHGFEDCBA, YWXVUTSRQPONMLKJIHGFEDCBA,
WXVUTSRQPONMLKJIHGFEDCBA, ...., DCBA, CBA, BA, A."""


alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabeto = alfabeto[::-1] 
for i in range(len(alfabeto)):
    print(alfabeto[i:])