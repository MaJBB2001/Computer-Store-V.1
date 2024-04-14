class Cliente:
    def __init__(self, idCliente, nombre, telefono):
        self.idCliente = idCliente
        self.nombre = nombre
        self.telefono = telefono

class listaClientes:
    def __init__(self):
        self.clientes = []

# Patron de diseño decotador. Decora con encabezados las demás funciones
    def FuncionDecoradora(funcion):
        def LineasAdoros(*args, **kwargs):
            print("•" * 33)
            print(">>>>>>>>> COMPUTER STORE <<<<<<<<")
            print("•" * 33)
            funcion(*args, **kwargs)  # Llamada a la función original con los mismos argumentos
        return LineasAdoros

    @FuncionDecoradora
    def AgregarCliente(self):
        print("        Agregar Cliente         ")
        print("        ˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅\n")

        # Comprobar si el ID del cliente ya existe
        while True:
            idCliente = input("Ingrese el ID del cliente: ")
            if idCliente.isdigit():  # Solo recibe números
                idExistente = False
                for cliente in self.clientes:
                    if cliente.idCliente == idCliente:
                        idExistente = True
                        break
                if not idExistente:
                    break
                else:
                    print("El ID ya existe. Inténtelo de nuevo.\n")
            else:
                print("El ID debe ser numérico. Inténtelo de nuevo.\n")

        while True:
            nombre = input("Ingrese el nombre del cliente: ")
            if nombre.isalpha():  # Solo recibe letras
                break
            else:
                print("El nombre debe contener solo letras. Inténtelo de nuevo.")

        while True:
            telefono = input("Ingrese el teléfono del cliente: ")
            if telefono.isdigit():  # Solo recibe números
                break
            else:
                print("El teléfono debe contener solo números. Inténtelo de nuevo.\n")

        nuevoCliente = Cliente(idCliente, nombre, telefono)
        self.clientes.append(nuevoCliente)
        print("")
        print(f"Cliente '{nombre}' agregado con éxito.")
        self.GuardarClientes()

    @FuncionDecoradora
    def MostrarClientes(self):
        if not self.clientes:  # Solo cargar si la lista de clientes está vacía
            self.CargarClientes("Clientes.txt")

        if self.clientes:
            print("             Listado de clientes        ")
            print("_" * 50)
            print("{:<15} {:<20} {:<15}".format("ID", "Nombre", "Teléfono"))
            print("-" * 50)
            for cliente in self.clientes:
                print("{:<15} {:<20} {:<15}".format(cliente.idCliente, cliente.nombre, cliente.telefono))
        else:
            print("No hay clientes registrados.")

    @FuncionDecoradora
    def ModificarCliente(self):
        print("        Modificar Cliente       ")
        print("        ˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅       \n")
        idCliente = input("Ingrese el ID del cliente que desea modificar: ")
        encontrado = False
        for cliente in self.clientes:
            if cliente.idCliente == idCliente:
                encontrado = True
                nuevoNombre = input("Ingrese el nuevo nombre del cliente: ")
                nuevoTelefono = input("Ingrese el nuevo teléfono del cliente: ")
                cliente.nombre = nuevoNombre
                cliente.telefono = nuevoTelefono
                print("Cliente modificado con éxito.")
                break

        if not encontrado:
            print("Cliente no encontrado.")

        self.GuardarClientes()

    @FuncionDecoradora
    def EliminarCliente(self):
        print("        Eliminar Cliente         ")
        print("        ˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅\n")
        idCliente = input("Ingrese el ID del cliente que desea eliminar: ")
        encontrado = False
        for cliente in self.clientes:
            if cliente.idCliente == idCliente:
                encontrado = True
                self.clientes.remove(cliente)
                print("Cliente eliminado con éxito.")
                break

        if not encontrado:
            print("Cliente no encontrado.")
        self.GuardarClientes()

    def CargarClientes(self, archivoTxt="Clientes.txt"):
        try:
            with open(archivoTxt, "r") as archivo:
                for linea in archivo:
                    idCliente, nombre, telefono = linea.strip().split(",")
                    # Verificar si el cliente ya está en la lista antes de agregarlo
                    clienteEncontrado = False
                    for cliente in self.clientes:
                        if cliente.idCliente == idCliente:
                            clienteEncontrado = True
                            break
                    if not clienteEncontrado:
                        nuevoCliente = Cliente(idCliente, nombre, telefono)
                        self.clientes.append(nuevoCliente)
            print("Clientes cargados exitosamente desde el archivo:", archivoTxt)
        except FileNotFoundError:
            print("El archivo de clientes no existe.")
        except Exception as e:
            print("Error al cargar los clientes:", str(e))

    def GuardarClientes(self, archivoTxt="Clientes.txt"):
        try:
            with open(archivoTxt, "a") as archivo:
                for cliente in self.clientes:
                    # Revisa si el cliente ya está en el archivo antes de agregarlo
                    clienteEncontrado = False
                    with open(archivoTxt, "r") as lecArchivo:
                        for linea in lecArchivo:
                            idClienteArchivo, _, _ = linea.strip().split(",")
                            if cliente.idCliente == idClienteArchivo:
                                clienteEncontrado = True
                                break
                    if not clienteEncontrado:
                        archivo.write(f"{cliente.idCliente},{cliente.nombre},{cliente.telefono}\n")
        except Exception as e:
            print("Error al guardar los clientes:", str(e))
