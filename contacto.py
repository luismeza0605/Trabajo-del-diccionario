def agregar_contacto(contactos):
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el número de teléfono: ")
    contactos[nombre] = telefono
    print(f"El contacto {nombre} ha sido agregado correctamente.")

def buscar_contacto(contactos):
    nombre = input("Ingresa el nombre del contacto: ")
    if nombre in contactos:
        print(f"El número de teléfono de {nombre} es: {contactos[nombre]}")
    else:
        print(f"El contacto {nombre} no existe.")

def mostrar_contactos(contactos):
    if contactos:
        print("Contactos:")
        for nombre, telefono in contactos.items():
            print(f"- {nombre}: {telefono}")
            
    else:
        print("No hay contactos almacenados.")

def actualizar_contacto(contactos):
    nombre = input("Ingresa el nombre del contacto a actualizar: ")
    if nombre in contactos:
        nuevo_telefono = input("Ingresa el nuevo número de teléfono: ")
        contactos[nombre] = nuevo_telefono
        print(f"El número de teléfono de {nombre} ha sido actualizado correctamente.")
    else:
        print(f"El contacto {nombre} no existe.")

def eliminar_contacto(contactos):
    nombre = input("Ingresa el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
      
    
    else:
        print(f"El contacto {nombre} no existe.")

def main():
    contactos = {}
    while True:
        print("\nBienvenido a la gestión de contactos.")
        print("Opciones:")
        print("1. Agregar un contacto.")
        print("2. Buscar un contacto.")
        print("3. Mostrar todos los contactos.")
        print("4. Actualizar número de teléfono.")
        print("5. Eliminar un contacto.")
        print("6. Salir.")
        
        opcion = input("Ingresa tu opción: ")
        
        if opcion == '1':
            agregar_contacto(contactos)
        elif opcion == '2':
            buscar_contacto(contactos)
        elif opcion == '3':
            mostrar_contactos(contactos)
        elif opcion == '4':
            actualizar_contacto(contactos)
        elif opcion == '5':
            eliminar_contacto(contactos)
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor ingresa un número del 1 al 6.")

if __name__ == "__main__":
    main()
