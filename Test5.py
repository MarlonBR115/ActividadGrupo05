import unittest
from io import StringIO
import sys


# Definición de las clases Producto e Inventario (asumimos que están en el mismo archivo)

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalles(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado.")

    def eliminar_producto(self, producto_nombre):
        self.productos = [p for p in self.productos if p.nombre != producto_nombre]
        print(f"Producto '{producto_nombre}' eliminado, si existía.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                producto.mostrar_detalles()


# Pruebas unitarias
class TestInventario(unittest.TestCase):

    def setUp(self):
        """ Configuración inicial para cada prueba """
        self.inventario = Inventario()
        self.producto1 = Producto("Laptop", 1000.0, 5)
        self.producto2 = Producto("Mouse", 20.0, 10)

    def test_agregar_producto(self):
        """ Prueba agregar un producto al inventario """
        self.inventario.agregar_producto(self.producto1)
        self.assertIn(self.producto1, self.inventario.productos)
        self.assertEqual(len(self.inventario.productos), 1)

    def test_eliminar_producto(self):
        """ Prueba eliminar un producto del inventario """
        self.inventario.agregar_producto(self.producto1)
        self.inventario.eliminar_producto("Laptop")
        self.assertNotIn(self.producto1, self.inventario.productos)
        self.assertEqual(len(self.inventario.productos), 0)

    def test_mostrar_inventario_vacio(self):
        """ Prueba que se muestre el mensaje de inventario vacío """
        captured_output = StringIO()
        sys.stdout = captured_output  # Redirige la salida estándar a una variable
        self.inventario.mostrar_inventario()
        sys.stdout = sys.__stdout__  # Restaura la salida estándar
        self.assertEqual(captured_output.getvalue().strip(), "El inventario está vacío.")

    def test_mostrar_inventario_con_productos(self):
        """ Prueba que se muestren los detalles de los productos en el inventario """
        self.inventario.agregar_producto(self.producto1)
        self.inventario.agregar_producto(self.producto2)
        captured_output = StringIO()
        sys.stdout = captured_output
        self.inventario.mostrar_inventario()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertIn("Producto: Laptop, Precio: 1000.0, Cantidad: 5", output)
        self.assertIn("Producto: Mouse, Precio: 20.0, Cantidad: 10", output)


if __name__ == "__main__":
    unittest.main()

