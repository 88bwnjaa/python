import json
def sueldo_liquido(sueldo_bruto):
    desc_salud = 70000
    desc_afp = 120000
    sueldo_bruto-= desc_salud + desc_afp
    return sueldo_bruto
def registrar_trabajador():
        lista_trabajadores=[]
        trabajador = input("Ingrese el nombre del trabajador: ")
        lista_trabajadores.append(trabajador)
        cargo_trabajador = input("Ingrese el cargo: ")
        lista_trabajadores.append(cargo_trabajador)
        sueldo_trabajador = int(input("Ingrese el sueldo bruto: "))
        lista_trabajadores.append(sueldo_trabajador)
        SueldoLiquido = sueldo_liquido(sueldo_trabajador)
        lista_trabajadores.append(SueldoLiquido)
        return lista_trabajadores
    
def imprimir_planilla(matriz):
    planilla = " ".join(matriz)
    for i in matriz:
        with open('Planilla.txt', 'w') as archivo:
            archivo.write(planilla)
    return planilla
    
matriz_trabajadores = [
]
while True:
    print("1.- Registrar trabajador\n2.- Listar todos los trabajadores\n3.- Imprimir planilla de sueldos\n4.- Salir\n")
    op = input()
    match op:
        case "1":
            trabajador=registrar_trabajador()
            matriz_trabajadores.append(trabajador)
        case "2":
            for trabajador in matriz_trabajadores:
                print(trabajador)
        case "3":
            imprimir_planilla(matriz_trabajadores)
                
        case "4":
            break