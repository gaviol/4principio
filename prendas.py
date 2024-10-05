# Clase Producto: Representa un ítem de ropa
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}")


# Herencia: RopaHombre y RopaMujer heredan de Producto
class RopaHombre(Producto):
    def __init__(self, nombre, precio, talla, cantidad):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


class RopaMujer(Producto):
    def __init__(self, nombre, precio, talla, cantidad):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


# Clase Categoria: Agrupa productos de la misma categoría
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        print(f"Categoría: {self.nombre}")
        for producto in self.productos:
            producto.mostrar_info()
            print("-" * 30)


# Clase Tienda: Gestiona el inventario y el proceso de compra
class Tienda:
    def __init__(self):
        self.categorias = []
        self.carrito = []
    
    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)
    
    def mostrar_catalogo(self):
        print("Catálogo de productos:")
        for categoria in self.categorias:
            categoria.mostrar_productos()
    
    def seleccionar_producto(self, nombre_producto):
        for categoria in self.categorias:
            for producto in categoria.productos:
                if producto.nombre.lower() == nombre_producto.lower():
                    if producto.cantidad > 0:
                        self.carrito.append(producto)
                        producto.cantidad -= 1  # Disminuir la cantidad en stock
                        print(f"{producto.nombre} ha sido añadido al carrito.")
                    else:
                        print(f"{producto.nombre} está agotado.")
                    return
        print(f"{nombre_producto} no se encontró en el catálogo.")
    
    def procesar_compra(self):
        if not self.carrito:
            print("El carrito está vacío.")
            return
        total = sum(producto.precio for producto in self.carrito)
        print("Procesando compra...")
        print(f"Total a pagar: ${total:.2f}")
        print("¡Gracias por su compra!")
        self.carrito.clear()  # Limpiar el carrito después de la compra


# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos de ropa
    camisa_hombre = RopaHombre("Camisa", 25.00, "M", 50)
    pantalon_hombre = RopaHombre("Pantalón", 30.00, "L", 30)
    vestido_mujer = RopaMujer("Vestido", 45.00, "S", 10)
    blusa_mujer = RopaMujer("Blusa", 22.00, "M", 40)
    
    # Crear categorías
    categoria_hombre = Categoria("Ropa para Hombre")
    categoria_mujer = Categoria("Ropa para Mujer")
    
    # Agregar productos a las categorías
    categoria_hombre.agregar_producto(camisa_hombre)
    categoria_hombre.agregar_producto(pantalon_hombre)
    categoria_mujer.agregar_producto(vestido_mujer)
    categoria_mujer.agregar_producto(blusa_mujer)
    
    # Crear la tienda y agregar categorías
    tienda = Tienda()
    tienda.agregar_categoria(categoria_hombre)
    tienda.agregar_categoria(categoria_mujer)
    
    # Mostrar el catálogo
    tienda.mostrar_catalogo()
    
    # Seleccionar productos para comprar
    tienda.seleccionar_producto("Camisa")
    tienda.seleccionar_producto("Blusa")
    
    # Procesar la compra
    tienda.procesar_compra()
