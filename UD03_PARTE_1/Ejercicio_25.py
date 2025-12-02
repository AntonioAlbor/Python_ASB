"""La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
control switch)."""

nombre = input("Ingrese el nombre del postulante: ")
opcion_facultad = input("Ingrese el número de la facultad a la que va a postular (1=Ingeniería, 2=Medicina, 3=Derecho, 4=Arquitectura): ")

importe = 0.00
mensualidad = 0.00
nombre_facultad = ""

if opcion_facultad == "1":
    nombre_facultad = "Ingeniería"
    importe = 1200.00
    mensualidad = 300.00
elif opcion_facultad == "2":
    nombre_facultad = "Medicina"
    importe = 1500.00
    mensualidad = 400.00
elif opcion_facultad == "3":
    nombre_facultad = "Derecho"
    importe = 1000.00
    mensualidad = 250.00
elif opcion_facultad == "4":
    nombre_facultad = "Arquitectura"
    importe = 1300.00
    mensualidad = 350.00
else:
    print("Opción de facultad no válida.")
    nombre_facultad = "Opción Inválida"

if importe > 0:
    igv = (importe + mensualidad) * 0.18
    monto_final = importe + mensualidad + igv

    print("Nombre:", nombre)
    print("Facultad:", nombre_facultad)
    print("Importe:", importe)
    print("Mensualidad:", mensualidad)
    print("IGV (18%):", igv)
    print("Monto final a pagar:", monto_final)