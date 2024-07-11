# en un cine con asientos enumerados, debe decir que espacio está ocupado y cual no
import csv

def menu ():
    print (""""
           Ingrese una de las siguientes opciones:
           1) Reservar un asiento
           2) Buscar asiento
           3) Revisar estado de asiento
           4) Venta diaria
           5) Exportar
           6) Salir
           """)

def reservar_asiento (cine=[]):
    num_asiento = input("Ingrese el numero de asiento: \n")
    nombre = input ("ingrese su nombre: \n")
    apellido = input ("ingrese su apellido: \n")
    rut = input ("ingrese su rut: \n")

    for espacio in cine:
        if espacio [0] == num_asiento:
            espacio[1] = "asiento ocupado"
            espacio[3] = nombre
            espacio[4] = apellido
            espacio[5] = rut
            print ("asiento reservado")
            print (espacio)
            break

def buscar_asiento (cine =[]):
    num_asiento = input ("ingrese el numero de asiento")
    for espacio in cine:
        if espacio [0] == num_asiento:
            return espacio

def estado_cine (cine = []):
    for espacio in cine:
        print (espacio)

def venta (cine=[]):
    total = 0
    for espacio in cine:
        total += espacio[2] if espacio [1] == "asiento ocupado" else 0
    return total

def guardar(cine):
    with open('cine.csv', 'w', newline='') as csv_file:
        archivo = ['asiento', 'estado', 'valor', 'nombre','apellido', 'rut']
        cine.insert(0, archivo)
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows (cine)


cine = []


filas_de_cine = 5
cine_por_fila = 10
for fila in range (1, filas_de_cine+ 1):
    for asiento in range (1, cine_por_fila + 1):
        num_asiento = str(10*fila + asiento)
        if fila == 3:
            cine.append([num_asiento, "disponible", 5000, "", "", ""])
        if fila == 4:
            cine.append([num_asiento, "disponible", 5500, "", "", ""])
        if fila == 1:
            cine.append([num_asiento, "disponible", 3000, "", "", ""])
        if fila == 2:
            cine.append([num_asiento, "disponible", 3000, "", "", ""])
        if fila == 5:
            cine.append([num_asiento, "disponible", 3000, "", "", ""])


while True:
    try:
        menu()
        opcion = input ("Ingrese una opción (1-6): ")
        if opcion == "6":
            print ("Adios!")
            break
        elif opcion == "1":
            reservar_asiento(cine)
        elif opcion == "2":
            print(buscar_asiento(cine))
        elif opcion == "3":
            estado_cine(cine)
        elif opcion == "4":
            print ("La venta diaria del dia es: ", venta(cine))
        elif opcion == "5":
            guardar(cine)
        else:
            print ("Opcion no valida.")
    except ValueError:
        print ("ingrese una opcion valida")