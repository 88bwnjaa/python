
def sueldo_liquido(sueldo_bruto):
    desc_salud = 70000
    desc_afp = 120000
    sueldo_bruto-= desc_salud + desc_afp
    return sueldo_bruto
def registrar_trabajador():
        cargos=("CEO", "DESARROLLADOR", "ANALISTA")
        trabajador = input("Ingrese el nombre del trabajador: ")
        cargo_trabajador = input("Ingrese el cargo: ")
        sueldo_trabajador = int(input("Ingrese el sueldo bruto: "))
        if cargo_trabajador.upper() in cargos:
            lista_trabajadores=[]
            lista_trabajadores.append(trabajador)
            lista_trabajadores.append(cargo_trabajador)
            lista_trabajadores.append(sueldo_trabajador)
            lista_trabajadores.append(70000)
            lista_trabajadores.append(120000)
            SueldoLiquido = sueldo_liquido(sueldo_trabajador)
            lista_trabajadores.append(SueldoLiquido)
            return lista_trabajadores
        else:
            return None
def imprimir_planilla(matriz):
    encabezado= "Nombre\t\tCargo\t\tSueldo bruto\tDesc. Salud\tDesc. AFP\tSueldo liquido\n"
    filas= []
    for fila in matriz:
        filas_convertidas= "\t".join(map(str, fila)) + "\n"
        filas.append(filas_convertidas)
    planilla = encabezado + "".join(filas)
    with open('Planilla.txt', 'w') as archivo:
        archivo.write(planilla)
    return planilla
    
matriz_trabajadores = []
while True:
    print("1.- Registrar trabajador\n2.- Listar todos los trabajadores\n3.- Imprimir planilla de sueldos\n4.- Salir\n")
    op = input()
    match op:
        case "1":
            trabajador=registrar_trabajador()
            if trabajador != None:
                matriz_trabajadores.append(trabajador)
            else: 
                print("El cargo ingresado no es válido")
        case "2":
            for trabajador in matriz_trabajadores:
                print(trabajador)
        case "3":
            imprimir_planilla(matriz_trabajadores)
            print("Planilla impresa con éxito")
                
        case "4":
            break 
