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
