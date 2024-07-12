lista = []
ceo = []
desarrollador = []
analista_de_datos = []
ceo2 = []
desarrollador2 = []
analista_de_datos2 = []

def registrar_trabajador (nombre, cargo, sueldo_b):
    dcto_salud = int(sueldo_b*0.07)
    dcto_afp = int(sueldo_b*0.12)
    sueldo_l = sueldo_b - dcto_salud - dcto_afp
    lista.append([nombre, cargo, sueldo_b, dcto_salud, dcto_afp, sueldo_l])
    if cargo=="ceo":
        for fila in lista:
            if fila[1]=="ceo":
                ceo.append(fila)
                for i in range(len(ceo)):
                    if ceo[i] not in ceo2:
                        ceo2.append(ceo[i])
    if cargo=="desarrollador":
        for fila in lista:
            if fila[1]=="desarrollador":
                desarrollador.append(fila)
                for i in range(len(desarrollador)):
                    if desarrollador[i] not in desarrollador2:
                        desarrollador2.append(desarrollador[i])
    if cargo=="analista de datos":
        for fila in lista:
            if fila[1]=="analista de datos":
                analista_de_datos.append(fila)
                for i in range(len(analista_de_datos)):
                    if analista_de_datos[i] not in analista_de_datos2:
                        analista_de_datos2.append(analista_de_datos[i])

def lista_trabajadores ():
    with open ('lista_trabajadores.txt', 'w', newline='') as lista_trabajadores:
        lista_trabajadores.write ("Nombre / Cargo / Sueldo bruto / Descuento salud / Descuento AFP / Sueldo liquido  \n")
        for trabajador in lista:
            lista_trabajadores.write(f"{trabajador}\n")
    archivo= open ('lista_trabajadores.txt', 'r')
    contenido = archivo.read()
    print (contenido)
    archivo.close

def imprimir_planilla ():
    op2=int (input("Seleccione una opción de cargo para imprimir \n 1) Todos los cargos \n 2) Ceo \n 3) Desarrollador \n 4) Analista de datos \n"))
    if op2 == 1:
        with open ('lista_trabajadores.txt', 'w', newline='') as lista_trabajadores:
            lista_trabajadores.write ("Nombre / Cargo / Sueldo bruto / Descuento salud / Descuento AFP / Sueldo liquido  \n")
            for trabajador in lista:
                lista_trabajadores.write(f"{trabajador}\n")
    if op2==2:
        with open ('planilla_ceo.txt', 'w', newline='') as planilla_ceo:
            planilla_ceo.write ("Nombre / Cargo / Sueldo bruto / Descuento salud / Descuento AFP / Sueldo liquido  \n")
            for trabajador in ceo2:
                planilla_ceo.write(f"{trabajador}\n")
    if op2==3:
        with open ('planilla_desarrollador.txt', 'w', newline='') as planilla_desarrollador:
            planilla_desarrollador.write("Nombre / Cargo / Sueldo bruto / Descuento salud / Descuento AFP / Sueldo liquido  \n")
            for trabajador in desarrollador2:
                planilla_desarrollador.write(f"{trabajador}\n")
    if op2==4:
        with open ('planilla_analista_de_datos.txt', 'w', newline='') as planilla_analista_de_datos:
            planilla_analista_de_datos.write("Nombre / Cargo / Sueldo bruto / Descuento salud / Descuento AFP / Sueldo liquido  \n")
            for trabajador in analista_de_datos2:
                planilla_analista_de_datos.write(f"{trabajador}\n")

while True:
    op = int(input ("Elija una opción \n 1) Registrar trabajador \n 2) Lista de trabajadores \n 3) Imprimir planilla de sueldos \n 4) Salir del programa \n"))
    if op == 1:
        nombre = input ("Ingrese el nombre del trabajador: ")
        cargo = input ("Ingrese el cargo del trabajador: ")
        sueldo_b = int (input ("Ingrese el sueldo bruto: "))
        registrar_trabajador (nombre, cargo, sueldo_b)
    if op == 2:
        lista_trabajadores()
    if op == 3:
        imprimir_planilla ()
    if op == 4:
        break
