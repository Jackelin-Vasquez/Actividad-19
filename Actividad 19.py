class Galleta:
    def __init__(self, nombre, precio, peso):
        if not nombre:
            print("El nombre no puede estar vacio...")
        if precio <= 0:
            print("El precio debe ser mayor a 0...")
        if peso <= 0:
            print("El peso debe ser mayor a 0...")
        self.nombre= nombre
        self.precio = precio
        self.peso= peso

    def mostrar_informacion(self):
        print(f"Nombre:{self.nombre}-Precio:{self.precio}-Peso:{self.peso}")

class GalletaChispas(Galleta):
    def __init__(self,nombre,precio,peso,canitdad_chispas):
        super().__init__(nombre,precio,peso)
        if canitdad_chispas <= 0:
            print("La cantidad de chispas debe ser mayor a 0")
        self.cantidad_chispas= canitdad_chispas

    def mostrar_informacion(self):
        print(f"Nombre:{self.nombre}-Precio:{self.precio}-Peso:{self.peso}-Cantidad Chispas{self.cantidad_chispas}")

class Relleno:
    def __init__(self,sabor_relleno):
        self.sabor_relleno= sabor_relleno

    def describir_relleno(self):
        print(f"relleno de {self.sabor_relleno}")
