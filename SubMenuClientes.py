def MenuClientes(self):
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
                while True:
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
                while True:
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

            elif opcion == 3:
                while True:
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
            elif opcion == 4:
                while True:
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

            elif opcion == 5:
                break

# En el Main
if __name__ == "__main__":
    while True:

