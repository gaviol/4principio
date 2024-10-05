# Clase Prenda: Encapsula los datos y comportamiento comunes para cualquier prenda
class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Atributo público
        if precio >= 0:
            self.precio = precio
        else:
            raise ValueError("El precio no puede ser negativo.")
        if cantidad >= 0:
            self.cantidad = cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa.")
    
    # Método que muestra información básica de la prenda
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}")


# Clase RopaHombre: Hereda de Prenda y añade atributos específicos para ropa de hombre
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla  # Atributo específico de RopaHombre
    
    # Sobrescribe el método mostrar_info para incluir la talla
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla de Hombre: {self.talla}")
        print("-" * 30)


# Clase RopaMujer: Hereda de Prenda y añade atributos específicos para ropa de mujer
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla  # Atributo específico de RopaMujer
    
    # Sobrescribe el método mostrar_info para incluir la talla
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla de Mujer: {self.talla}")
        print("-" * 30)


# Clase Inventario: Abstrae la gestión de múltiples prendas en una lista
class Inventario:
    def __init__(self):
        self.prendas = []  # Lista para almacenar las prendas

    # Método para agregar una prenda al inventario
    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)
        print(f"'{prenda.nombre}' ha sido agregada al inventario.")
    
    # Método para mostrar el inventario completo
    def mostrar_inventario(self):
        if not self.prendas:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for prenda in self.prendas:
                prenda.mostrar_info()

    # Método para buscar una prenda por su nombre
    def buscar_prenda(self, nombre):
        for prenda in self.prendas:
            if prenda.nombre.lower() == nombre.lower():
                return prenda
        return None
    
    # Método para eliminar una prenda del inventario
    def eliminar_prenda(self, nombre):
        prenda = self.buscar_prenda(nombre)
        if prenda:
            self.prendas.remove(prenda)
            print(f"'{nombre}' ha sido eliminada del inventario.")
        else:
            print(f"'{nombre}' no está en el inventario.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de ropa para hombres y mujeres
    camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
    pantalon = RopaHombre("Pantalón de Hombre", 30.00, 30, "L")
    falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")
    blusa = RopaMujer("Blusa de Mujer", 22.00, 40, "M")

    # Crear el inventario y agregar prendas
    inventario = Inventario()
    inventario.agregar_prenda(camisa)
    inventario.agregar_prenda(pantalon)
    inventario.agregar_prenda(falda)
    inventario.agregar_prenda(blusa)

    # Mostrar el inventario
    inventario.mostrar_inventario()

    # Buscar una prenda específica
    prenda_encontrada = inventario.buscar_prenda("Camisa de Hombre")
    if prenda_encontrada:
        print(f"\nPrenda encontrada: {prenda_encontrada.nombre}")
    else:
        print("Prenda no encontrada.")

    # Eliminar una prenda del inventario
    inventario.eliminar_prenda("Blusa de Mujer")

    # Mostrar el inventario después de eliminar una prenda
    inventario.mostrar_inventario()
