def agregar_producto(inventario):
    nombre = input("Ingresa el nombre del producto: ")
    cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad
    print("Producto agregado al inventario.")

def vender_producto(inventario):
    nombre = input("Ingresa el nombre del producto a vender: ")
    if nombre in inventario:
        cantidad = int(input(f"Ingrese la cantidad a vender de {nombre}: "))
        if cantidad <= inventario[nombre]:
            inventario[nombre] -= cantidad
            print("Venta realizada.")
        else:
            print("No hay suficiente stock.")
    else:
        print("El producto no existe en el inventario.")

def mostrar_inventario(inventario):
    if inventario:
        print("Inventario:")
        for nombre, cantidad in inventario.items():
            print(f"- {nombre}: {cantidad}")
    else:
        print("El inventario está vacío.")

def main():
    inventario = {}
    while True:
        print("\nBienvenido al sistema de inventario de la tienda.")
        print("1. Agregar un producto al inventario")
        print("2. Vender un producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            vender_producto(inventario)
        elif opcion == '3':
            mostrar_inventario(inventario)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor ingresa un número del 1 al 4.")

if __name__ == "__main__":
    main()
