import csv

# Inicializa el inventario como un diccionario
inventario = {}

# Cargar datos del archivo CSV si existe
def cargar_inventario():
    try:
        with open('data\inventario.csv', newline='') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for fila in lector_csv:
                producto = fila['Producto']
                cantidad = int(fila['Cantidad'])
                precio = float(fila['Precio'])
                inventario[producto] = {'Cantidad': cantidad, 'Precio': precio}
    except FileNotFoundError:
        # Si el archivo CSV no existe, simplemente continuamos con un inventario vacío
        pass

# Guardar datos en el archivo CSV
def guardar_inventario():
    with open('data\inventario.csv', mode='w', newline='') as archivo_csv:
        campos = ['Producto', 'Cantidad', 'Precio']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        
        for producto, detalles in inventario.items():
            escritor_csv.writerow({'Producto': producto, 'Cantidad': detalles['Cantidad'], 'Precio': detalles['Precio']})

# Agregar un producto al inventario
def agregar_producto(producto, cantidad, precio):
    if producto in inventario:
        inventario[producto]['Cantidad'] += cantidad
    else:
        inventario[producto] = {'Cantidad': cantidad, 'Precio': precio}

# Vender un producto del inventario
def vender_producto(producto, cantidad):
    if producto in inventario and inventario[producto]['Cantidad'] >= cantidad:
        inventario[producto]['Cantidad'] -= cantidad
    else:
        print(f"No hay suficiente stock de {producto}.")

if __name__ == '__main__':
    cargar_inventario()

    while True:
        print("Menú de Inventario")
        print("1. Agregar Producto")
        print("2. Vender Producto")
        print("3. Mostrar Inventario")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar_producto(producto, cantidad, precio)
            guardar_inventario()
        elif opcion == '2':
            producto = input("Nombre del producto a vender: ")
            cantidad = int(input("Cantidad a vender: "))
            vender_producto(producto, cantidad)
            guardar_inventario()
        elif opcion == '3':
            print("Inventario:")
            for producto, detalles in inventario.items():
                print(f"{producto}: Cantidad: {detalles['Cantidad']}, Precio: {detalles['Precio']}")
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")