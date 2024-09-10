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


def mostrar_menu():
    print("\nMenu:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            producto = Producto(nombre, precio, cantidad)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            print("\nInventario actual:")
            print("----------------------------------------")
            inventario.mostrar_inventario()
            print("----------------------------------------")
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)

        elif opcion == "3":
            print("\nInventario actual:")
            inventario.mostrar_inventario()

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")


if __name__ == "__main__":
    main()