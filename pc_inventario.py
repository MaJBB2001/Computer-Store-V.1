import os

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class InventarioElectronico(Singleton):
    def __init__(self):
        self.articulos = {
            1: ("Laptop HP Core i5", 150000),
            2: ("Teléfono Samsung A54", 70000),
            3: ("Tablet Acer", 35000),
            4: ("Reloj inteligente", 20000),
            5: ("Audifonos entrada Tipo C", 15000),
            6: ("Parlantes con Bluetooth", 10000),
            7: ("Cámara digital ProHT", 60000),
            8: ("Mouse Kipxtreme", 8400),
            9: ("Impresora multifunción Epson", 130000),
            10: ("Router Wi-Fi Linksys", 35000)
        }
        self.CargarInventario("Inventario.txt")  # Carga el inventario prestablecido en diccionario

    # Patrón de diseño Decorador
    def FuncionDecoradora(funcion):
        def LineasAdoros(*args, **kwargs):
            print("•" * 33)
            print(">>>>>>>>> COMPUTER STORE <<<<<<<<")
            print("•" * 33)
            funcion(*args, **kwargs)  # Llamada a la función original con los mismos argumentos
        return LineasAdoros

    def CargarInventario(self, nombreArchivo):  # Carga el archivo TXT del inventario si existe
        try:
            with open(nombreArchivo, "r") as archivo:
                for linea in archivo:
                    numero, nombre, precio = linea.strip().split(": ")
                    self.articulos[int(numero)] = (nombre, float(precio))
        except FileNotFoundError:
            print("El archivo de inventario no existe.")
        except Exception as e:
            print("Error al cargar el inventario:", str(e))
            self.articulos = {}

    @FuncionDecoradora    # Llamada a la función Decoradora
    def AgregarArticulo(self):
            print("        Agregar Artículo        ")
            print("        ˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅\n")
            nombre = input("Ingrese el nombre del nuevo artículo: ")
            precio = float(input("Ingrese el precio del nuevo artículo: "))

            # Encuentra el nuevo número del artículo
            numero = max(self.articulos.keys()) + 1 if self.articulos else 1

            # Agrega el nuevo artículo
            self.articulos[numero] = (nombre, precio)
            print("\nArtículo agregado correctamente.")
            self.GuardarInventario("Inventario")

    def BuscarArticulos(self, letra):
        while True:
            articulosEncontrados = []
            inventario = InventarioElectronico()
           # inventario.LimpiarPantalla()
            for numero, (nombre, precio) in self.articulos.items():
                if nombre.startswith(letra):
                    articulosEncontrados.append((numero, nombre, precio))

            if articulosEncontrados:
                print("")
                print(f"Artículos que empiezan con la letra '{letra}':")
                print("_" * 40)

                for numero, nombre, precio in articulosEncontrados:
                    print(f"{numero}. {nombre}: {precio}")
                break
            else:
                print(f"No se encontraron artículos que empiecen con la letra '{letra}'.")
                respuesta = input("\n¿Desea intentar con otra letra? (s/n): ")
                if respuesta.lower() != 's':
                    break
                letra = input("\nIngrese otra letra: ")

        return articulosEncontrados

    @FuncionDecoradora
    def ModificarArticulo(self):
        print("        Modificar Artículo        ")
        print("        ˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅\n")
        while True:
            letra = input("Ingrese la letra inicial del artículo a buscar: ")
            if letra.isalpha() and len(letra) == 1:
                break
            else:
                print("Por favor, ingrese una sola letra.")

        articulos = self.BuscarArticulos(letra)

        if not articulos:
            print(f"No se encontraron artículos que empiecen con la letra '{letra}'.")
            return

        num_articulo_input = input("\nIngrese el número del artículo que desea modificar: ")

        try:
            num_articulo = int(num_articulo_input)
        except ValueError:
            print("El número de artículo no es válido.")
            return

        if num_articulo not in [articulo[0] for articulo in articulos]:
            print("El número de artículo no es válido.")
            return

        print(
            f"\nArtículo seleccionado: {num_articulo}. {self.articulos[num_articulo][0]} - Precio: {self.articulos[num_articulo][1]}")

        nuevo_nombre = input("Ingrese el nuevo nombre del artículo: ")
        nuevo_precio_input = input("Ingrese el nuevo precio del artículo: ")

        try:
            nuevo_precio = float(nuevo_precio_input)
        except ValueError:
            print("El precio ingresado no es válido.")
            return

        if nuevo_nombre:
            self.articulos[num_articulo] = (nuevo_nombre, self.articulos[num_articulo][1])

        if nuevo_precio:
            self.articulos[num_articulo] = (self.articulos[num_articulo][0], nuevo_precio)

        print("\nArtículo modificado correctamente.")
        self.GuardarInventario("Inventario")

    @FuncionDecoradora
    def MostrarInventario(self):
        print("              Inventario ")
        print("-" * 40)  # Línea decorativa
        print("{:<5} {:<25} {:<10}".format("Nº", "Nombre", "Precio"))
        print("-" * 40)

        for numero, (nombre, precio) in self.articulos.items():
            print("{:<5} {:<25} {:<10}".format(numero, nombre, precio))

    @FuncionDecoradora
    def EliminarArticulo(self):
        print("        Eliminar Artículo        ")
        print("        ˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅˅\n")
        letra = input("Ingrese la letra inicial del artículo a eliminar: ")
        articulos = self.BuscarArticulos(letra)

        if not articulos:
            print(f"No se encontraron artículos que empiecen con la letra '{letra}'.")
            return
        num_articulo = int(input("\nIngrese el número del artículo que desea eliminar: "))

        if num_articulo not in [articulo[0] for articulo in articulos]:
            print("El número de artículo no es válido.")
            return
        print(
            f"\nArtículo seleccionado: {num_articulo}. {self.articulos[num_articulo][0]} - Precio: {self.articulos[num_articulo][1]}")
        confirmacion = input("¿Está seguro de que desea eliminar este artículo? (s/n): \n")

        if confirmacion.lower() == 's':
            del self.articulos[num_articulo]
            print("Artículo eliminado correctamente.")
            self.GuardarInventario("Inventario")
        else:
            print("Operación de eliminación cancelada.")

    def GuardarInventario(self, nombreArchivo):
        with open(nombreArchivo + ".txt", "wt") as archivo:
            for numero, (nombre, precio) in self.articulos.items():
                archivo.write(f"{numero}: {nombre}: {precio}\n")

    def LimpiarPantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
