from pc_inventario import InventarioElectronico

inventario = InventarioElectronico()  # Crear una instancia del inventario
def MostrarMenu():

    print("*" * 35)
    print("___________BIENVENIDOS_________")
    print("________ Cumputer Store________")
    print("*" * 35)
    print("\nSeleccione una opción:\n")
    print("1. Ver inventario")
    print("2. Modificar inventario")
    print("3. Agregar artículo")
    print("4. Eliminar artículo")
    print("5. Facturar Venta")
    print("6. Clientes")
    print("7. Guardar")
    print("8. Salir")

def main():

    while True:

        MostrarMenu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            inventario.LimpiarPantalla()
            inventario.MostrarInventario()
            input("\nPresione Enter para regresar al Menú...")
            inventario.LimpiarPantalla()

        elif opcion == "2":
            print("-" * 30)
            print("*** Inciando Modificar ***")
            print("-" * 30)
        elif opcion == "3":
            print("-" * 30)
            print("*** Inciando Agregar***")
            print("-" * 30)
        elif opcion == "4":
            print("-" * 30)
            print("*** Inciando Eliminar***")
            print("-" * 30)
        elif opcion == "5":
            print("-" * 30)
            print("*** Inciando Guardar ***")
            print("-" * 30)
        elif opcion == "6":
            print("-" * 30)
            print("*** Inciando Guardar ***")
            print("-" * 30)
        elif opcion == "7":
            print("-" * 30)
            print("*** Inciando Guardar ***")
            print("-" * 30)
        elif opcion == "8":
            input("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            input("Presione Enter para continuar...")
if __name__ == "__main__":
    main()
