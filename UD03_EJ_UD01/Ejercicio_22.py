"""Escriba un programa que recibe como datos de entrada una hora expresada en horas,
minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán,
transcurrido un segundo"""

hora = int(input("Ingrese la hora (0-23): "))
minuto = int(input("Ingrese los minutos (0-59): "))
segundo = int(input("Ingrese los segundos (0-59): "))
segundo += 1
if segundo == 60:
    segundo = 0
    minuto += 1
    if minuto == 60:
        minuto = 0
        hora += 1
        if hora == 24:
            hora = 0
print("La hora después de un segundo será:", hora, minuto, segundo)