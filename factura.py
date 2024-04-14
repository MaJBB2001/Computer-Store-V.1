import tkinter as tk
from pc_inventario import InventarioElectronico

inventario = InventarioElectronico()  # Crear una instancia del inventario

# Imprime la factura en inglés o español

class ImprimirFacturaIngles():  # Adapta impresión en idioma inglés
    def ImprimirFactura(self, productosFacturados, total, descuento, iva, numeroFactura, idCliente):
        inventario.LimpiarPantalla()
        print("*" * 70)
        print("                             INVOICE                         ")
        print("                          Computer Store                     ")
        print("*" * 70)
        print("Invoice Number:", numeroFactura)
        print("Customer:", BuscaNombreCliente(idCliente))
        print("-" * 70)
        print("{:<10} {:<30} {:<10} {:<10} {:<10}".format("N°", "Name", "Price", "Quantity", "Subtotal"))
        for i, (numeroArticulo, nombreProducto, precioProducto, cantidad, subtotal) in enumerate(productosFacturados, 1):
            print("{:<10} {:<30} {:<10} {:<10} {:<10}".format(numeroArticulo, nombreProducto, precioProducto, cantidad, subtotal))
        print("\nSubtotal:", total)
        print("Discount:", descuento)
        print("Tax:", iva)
        print("Total to pay:", total + iva - descuento)

