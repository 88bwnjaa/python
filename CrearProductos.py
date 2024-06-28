def crear_producto():
    while True:
        nombre_producto = input("Ingrese el nombre del producto:\n")
        try:
            stock_producto = int(input("Ingrese el stock del producto:\n"))
            valor_producto = int(input("Ingrese el valor del producto:\n"))
        except ValueError:
            print("Valor ingresado no válido")
            continue
        if stock_producto > 0 and valor_producto > 0:
            producto =[]
            producto.append(nombre_producto)
            producto.append(str(stock_producto))
            producto.append(str(valor_producto))
            return producto
        else:
            print("El valor o stock ingresado no es correcto")
            

def guardar_producto(lista, producto):
    for prod in lista:
        if prod[0].lower() == producto[0].lower():
            prod[1] = str(producto[1])
            prod[2] = str(producto[2])
            return lista
        
    lista.append(producto)
    return lista
def imprimir_planilla_productos(lista):
    with open('Planilla.txt','w')as archivo:
        for producto in lista:
            archivo.write(f"Producto: {producto[0]}|| Stock: {producto[1]}|| Valor: {producto[2]}\n")


lista_productos = []
while True:
    producto = crear_producto()
    lista_productos = guardar_producto(lista_productos, producto)
    print(lista_productos)
    print("¿Desea agregar otro producto?")
    op =input(">").lower()
    if op == "si":
        continue
    else:
        op1 = input("1) Imprimir planilla de productos\n2) Cerrar programa\n>")
        match op1:
            case "1":
                imprimir_planilla_productos(lista_productos)
            case "2":
                break
        
            case default:
                print("Opcion no valida, por favor ingrese 1 o 2")
    
