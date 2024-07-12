import csv
import random

fila_a_saltar = 0
planilla = []
with open ('examen.csv', 'r', newline='')as archivo_csv:
    reader = csv.reader(archivo_csv)
    for fila in reader:
        planilla.append(fila)

    for i, row in enumerate(reader):
        if i == fila_a_saltar:
            continue
        print (row)

def sueldo_aleatorio ():
    for empleado in planilla:
        empleado[2]=random.randint(300000, 2500000)
    

def sueldos_clasificados():
    total_sueld_menores = 0
    total_sueld_medianos = 0
    total_sueld_mayores = 0
    sueldos_menores = []
    sueldos_medianos = []
    sueldos_mayores = []
    for empleado in planilla:
        if empleado [2]<800000:
            total_sueld_menores = total_sueld_menores + 1
            sueldos_menores.append(empleado)
    print ("Sueldos menores a $800000: ", total_sueld_menores)
    for personas in sueldos_menores:
        print(personas)
    print("\n")
    
    for empleado in planilla:
        if empleado [2]>=800000 and empleado[2]<2000000:
            total_sueld_medianos = total_sueld_medianos + 1
            sueldos_medianos.append(empleado)
    print ("Sueldos entre $800000 y $2000000: ", total_sueld_medianos)
    for personas in sueldos_medianos:
        print(personas)
    print("\n")
    
    for empleado in planilla:
        if empleado[2]>2000000:
            total_sueld_mayores = total_sueld_mayores + 1
            sueldos_mayores.append(empleado)
    print ("Sueldos mayores a $2000000: ", total_sueld_mayores)
    for personas in sueldos_mayores:
        print(personas)
    print("\n")

def generar_reporte ():
    print ("Nombre / Cargo / Sueldo bruto / Dcto salud / Dcto AFP / Sueldo liquido")
    reporte = []
    for empleado in planilla:
        nombre=empleado [0]
        cargo=empleado[1]
        sueldo_bruto=empleado[2]
        dcto_salud = sueldo_bruto *0.07
        dcto_afp = sueldo_bruto * 0.12
        sueldo_liquido = sueldo_bruto - dcto_salud - dcto_afp
        reporte.append ([nombre, cargo, sueldo_bruto, int(dcto_salud), int(dcto_afp), int(sueldo_liquido)])
    for persona in reporte:
        print (persona)
    print ("\n")
    with open ('examen.csv', 'w', newline='')as archivo_csv:
        encabezado = ['nombre empleado', 'cargo', 'sueldo bruto', 'dcto salud', 'dcto afp', 'sueldo liquido']
        reporte.insert(0, encabezado)
        writer = csv.writer(archivo_csv)
        writer.writerows(reporte)
while True:
    opcion=int(input("Seleccione una opcion:\n 1) Asignar sueldos aleatorios\n 2) Clasificar sueldos \n 3) Guardar reporte \n 4) Salir \n"))
    if opcion==1:
        sueldo_aleatorio()
    if opcion==2:
        sueldos_clasificados()
    if opcion==3:
        generar_reporte()
    if opcion==4:
        print("Finalizando programa... ")
        break
   
