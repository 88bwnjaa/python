#Funcion para crear el producto, stock y valor
def crear_producto():
    while True:
        nombre_producto = input("Ingrese el nombre del producto:\n")
        try:
            stock_producto = int(input("Ingrese el stock del producto:\n"))
            valor_producto = int(input("Ingrese el valor del producto:\n"))
        except ValueError:
            print("Valor ingresado no válido")
            continue#Si el valor ingresado no es un numero reiniciamos la iteracion 
        if stock_producto > 0 and valor_producto > 0:
            producto =[]#Lista con los valores de nuestro producto
            producto.append(nombre_producto)#Agregamos todos los valores a la lista
            producto.append(str(stock_producto))#Str() para transformar ambos valores de enteros a cadenas
            producto.append(str(valor_producto))
            return producto
        else:
            print("El valor o stock ingresado no es correcto")

#Funcion para agregar el producto creado a una matriz de productos 
def guardar_producto(lista, producto):#Recibimos como parametros la matriz y el producto creado
    for prod in lista:                #Con el fin de verificar si el producto ya existe en la matriz o no
        if prod[0].lower() == producto[0].lower():
            prod[1] = str(producto[1])#En el caso de que ya exista
            prod[2] = str(producto[2])#Actualizamos el valor y stock al nuevo que se está ingresando 
            return lista
        
    lista.append(producto)#Si el producto no existe en la matriz simplemente lo agregaremos a esta
    return lista

#Funcion que itera sobre la matriz de productos para imprimir un archivo .txt de la misma
def imprimir_planilla_productos(lista):
    with open('Planilla.txt','w')as archivo:
        for producto in lista:
            archivo.write(f"Producto: {producto[0]} || Stock: {producto[1]} || Valor: {producto[2]}\n")

#Inicializamos fuera del bucle la matriz donde estaran todos los productos creados 
lista_productos = []
#Bucle principal de interaccion con el usuario 
while True:
    #Llamamos ambas funciones y guardamos el retorno en las respectivas variables
    producto = crear_producto()
    lista_productos = guardar_producto(lista_productos, producto)
    print(lista_productos)
    print("¿Desea agregar otro producto?")
    op =input(">").lower()
    if op == "si": #Siempre que el usuario responda "si" el bucle se seguirá ejecutando para seguir agregando productos
        continue
    else:
        op1 = input("1) Imprimir planilla de productos\n2) Cerrar programa\n>")
        while True:#Un segundo bucle para que se siga ejecutando hasta que las opciones sean 1 o 2
            match op1:
                case "1":
                    imprimir_planilla_productos(lista_productos)#Llamada a la funcion para imprimir planilla
                    break
                case "2":    
                    break #Salimos de este bucle pero aun queda el principal
    
                case default:
                    print("Opcion no valida, por favor ingrese 1 o 2")
                    op1 = input("1) Imprimir planilla de productos\n2) Cerrar programa\n>")

    if op1 == "2":#Condicional para cerrar el programa en caso de que anteriormente el usuario haya
        break     #Seleccionado esa opcion 
