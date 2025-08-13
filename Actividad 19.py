Galletas = []  #Aqui se guardaran las galletas :)

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

class GalletaRellena(Galleta,Relleno):
    def __init__(self,nombre,precio,peso,sabor_relleno):
        Galleta.__init__(self,nombre,precio,peso)
        Relleno.__init__(self,sabor_relleno)

        def mostrar_informacion(self):
            print(f"Nombre:{self.nombre}-Precio:{self.precio}-Peso:{self.peso}-Relleno:{self.describir_relleno()}")

def menu():
    print(f"---Menú---\n1.Registrar Galleta Básica\n2.Registrar Galleta con Chispas\n3.Registrar Gallera Rellena")
    print(f"4.Listas Galletas\n5.Buscar por Nombre\n6.Eliminar por nombre.\n7.Salir.")

#Funcion opcion 1 para registrar galletas
def registrar_galleta():
    nombre= input("Ingrese nombre de gallera")
    encontrado= False
    for galleta in Galletas:
        if galleta.nombre.lower() == nombre.lower():
            print(f"Galleta {nombre} ya existe")
            encontrado= True
            break
    if not encontrado:
        try:
            precio= float(input("Ingrese precio de galleta:"))
            peso= float(input("Ingrese peso de galleta:"))
            galletas= Galleta(nombre,precio,peso)
            Galletas.append(galletas)
            print("Galleta resgistrada :D!")
        except ValueError:
            print("Error.Ingrese número valido...")
        except Exception as e:
            print("Ocurrio un error inesperado :(:",e)