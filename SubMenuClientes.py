from pc_inventario import InventarioElectronico
from clientes import listaClientes

class SubMenuClientes:
    def __init__(self):
        self.clientes = listaClientes()

    def MenuClientes(self):
        inventario = InventarioElectronico()  # Crear una instancia de la clase InventarioElectronico

        while True: # SubMenuClientes se ejecuta hasta la opción salir
            print("********************")
            print("* SubMenu Clientes *")
            print("********************\n")
            print("1. Agregar cliente")
            print("2. Mostrar cliente")
            print("3. Modificar cliente")
            print("4. Eliminar clientes")
            print("5. Salir al Menú Principal\n")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                while True:  # Loop para agregar clientes hasta que el usuario decida salir
                    inventario.LimpiarPantalla()
                    self.clientes.AgregarCliente()
                    while True:
                        continuar = input("\n¿Desea continuar agregando clientes? (s/n): ").lower()
                        if continuar == 's' or continuar == 'n':
                            break
                        else:
                            print("Por favor, ingresa una opción válida (s/n).")
                    if continuar == 's':
                        # Si el usuario elige continuar ('s'), el bucle continúa y se agrega otro artículo.
                        continue
                    elif continuar == 'n':
                        # Si el usuario elige no continuar ('n'), se sale del bucle while.
                        break

            elif opcion == 2:
                inventario.LimpiarPantalla()
                self.clientes.MostrarClientes()
                print(" ")
                input("\nPresiona ¨s¨ para salir al Sub Menú: ")

            elif opcion == 3:
                while True:
                    inventario.LimpiarPantalla()
                    self.clientes.ModificarCliente()

                    while True:
                        continuar = input("\n¿Desea continuar modificando clientes? (s/n): ").lower()
                        if continuar == 's' or continuar == 'n':
                            break
                        else:
                            print("Por favor, ingresa una opción válida (s/n).")
                    if continuar == 's':
                        # Si el usuario elige continuar ('s'), el bucle continúa y se agrega otro artículo.
                        continue
                    elif continuar == 'n':
                        # Si el usuario elige no continuar ('n'), se sale del bucle while.
                        break

            elif opcion == 4:
                while True:
                    inventario.LimpiarPantalla()
                    self.clientes.EliminarCliente()

                    while True:
                        continuar = input("\n¿Desea continuar eliminando clientes? (s/n): ").lower()
                        if continuar == 's' or continuar == 'n':
                            break
                        else:
                            print("Por favor, ingresa una opción válida (s/n).")
                    if continuar == 's':
                        # Si el usuario elige continuar ('s'), el bucle continúa y se agrega otro artículo.
                        continue
                    elif continuar == 'n':
                        # Si el usuario elige no continuar ('n'), se sale del bucle while.
                        break

            elif opcion == 5:
                break
            inventario.LimpiarPantalla()


if __name__ == "__main__":
    while True:
        sub_menu_clientes = SubMenuClientes()
        sub_menu_clientes.MenuClientes()
