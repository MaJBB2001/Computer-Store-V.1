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

    def MostrarInventario(self):
        print("              Inventario ")
        print("-" * 40)  # Línea decorativa
        print("{:<5} {:<25} {:<10}".format("Nº", "Nombre", "Precio"))
        print("-" * 40)

        for numero, (nombre, precio) in self.articulos.items():
            print("{:<5} {:<25} {:<10}".format(numero, nombre, precio))

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

    def LimpiarPantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

def FuncionDecoradora(funcion):
    def LineasAdoros(*args, **kwargs):
        print("•" * 33)
        print(">>>>>>>>> COMPUTER STORE <<<<<<<<")
        print("•" * 33)
        funcion(*args, **kwargs)  # Llamada a la función original con los mismos argumentos
    return LineasAdoros
