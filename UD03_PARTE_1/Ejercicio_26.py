"""En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
Si los tres dados son seis, mostrar el mensaje “Excelente”
Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
Si un dado se obtiene seis, mostrar el mensaje “Regular”
Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
(Use el control switch)."""
dado1 = int(input("Ingrese el valor del primer dado (1-6): "))
dado2 = int(input("Ingrese el valor del segundo dado (1-6): "))
dado3 = int(input("Ingrese el valor del tercer dado (1-6): "))
contador_seises = 0
if dado1 == 6:
    contador_seises += 1
if dado2 == 6:
    contador_seises += 1
if dado3 == 6:
    contador_seises += 1
if contador_seises == 3:
    print("Excelente")
elif contador_seises == 2:
    print("Muy bien")
elif contador_seises == 1:
    print("Regular")
else:
    print("Pésimo")