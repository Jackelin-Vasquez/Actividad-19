Galletas = []  #Aqui se guardaran las galletas :)

#Clase base "Galleta"
class Galleta:
    def __init__(self, nombre, precio, peso):
        if not nombre:
            print("El nombre no puede estar vacio...")
            return
        if precio <= 0:
            print("El precio debe ser mayor a 0...")
            return
        if peso <= 0:
            print("El peso debe ser mayor a 0...")
            return
        self.nombre= nombre
        self.precio = precio
        self.peso= peso

    def mostrar_informacion(self):
        print(f"Nombre:{self.nombre}-Precio:{self.precio}-Peso:{self.peso}")

#Esta clase es "Hija" de la glase galleta
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
        return f"relleno de {self.sabor_relleno}"

#Esta clase hereda de clase galleta y clase relleno
class GalletaRellena(Galleta,Relleno):
    def __init__(self,nombre,precio,peso,sabor_relleno):
        Galleta.__init__(self,nombre,precio,peso)
        Relleno.__init__(self,sabor_relleno)

    def mostrar_informacion(self):
        print(f"Nombre:{self.nombre}-Precio:{self.precio}-Peso:{self.peso}-Relleno:{self.describir_relleno()}")

def menu():
    print(f"---Menú---\n1.Registrar Galleta Básica\n2.Registrar Galleta con Chispas\n3.Registrar Gallera Rellena")
    print(f"4.Listas Galletas\n5.Buscar por Nombre\n6.Eliminar por nombre.\n7.Salir.")

#Esta funcion servira para validar que el numero sea valido y si no volver a pedir, para evitar repetir el codigo una y otra vez
def numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error. Debe ingresar un número valido...")
        except Exception as e:
            print("Error.Ocurrio un error inespetado :(..",e)

#Funcion opción 1 para registrar galletas
def registrar_galleta():
    nombre= input("Ingrese nombre de gallera")
    encontrado= False
    for galleta in Galletas:
        if galleta.nombre.lower() == nombre.lower(): # se verifica que la galleta este o no en la lista
            print(f"Galleta {nombre} ya existe")
            encontrado= True
            break
    if not encontrado:
        precio= numero("Ingrese precio de gelleta:")
        peso= numero(("Ingrese peso de galleta:"))
        nueva_galleta= Galleta(nombre,precio,peso)
        Galletas.append(nueva_galleta)
        print(f"Galleta {nombre} registrada de forma existosa!")


#Funcion par aopcion 2
def registrar_galleta_chispas():
    encontrado= False
    galleta_chispas= input("Ingrese nombre de galleta con chispas:")
    for galleta in Galletas:
        if galleta.nombre.lower() == galleta_chispas.lower():
            print("Galleta ya resgitrada...")
            encontrado= True
            break
    if not encontrado:
        precio= numero("Ingrese precio de galleta con chispas:")
        peso= numero("Ingrese preso de galleta con chispas:")
        while True:
            try:
                cantida_chispas= int(input("Ingrese cantidad de chispas:"))
                if cantida_chispas <= 0:
                    print("La cantidad debe ser mayor que 0...")
                else:
                    break
            except ValueError:
                print("Error. Ingrese un número entero positivo...")
        nueva_galleta= GalletaChispas(galleta_chispas,precio,peso,cantida_chispas)
        Galletas.append(nueva_galleta)

#funcion opcion 3 - registro galleta con relleno
def registrar_galleta_rellena():
    nombre= input("Ingrese nombre de galleta rellena:")
    encontrado= False
    for galleta in Galletas:
        if galleta.nombre.lower() == nombre.lower():
            print("Galleta ya resgitrada...")
            encontrado= True
            break

    if not encontrado:
        precio= numero("Ingrese precio de galleta rellena:")
        peso= numero("Ingrese peso de galletra rellena:")
        relleno= input("Ingrese el relleno:")
        nueva_galleta= GalletaRellena(nombre,precio,peso,relleno)
        Galletas.append(nueva_galleta)

#funcion opcion 4 listado de galletas
def lista_galletas():
    if not Galletas:
        print("Lista de galletas vacia :(")
    else:
        for indice,galleta in enumerate(Galletas,start=1):
            print(f"{indice}.Información de galleta:")
            galleta.mostrar_informacion()
            print("---"*4)

#Funcion opcion 5- busqueda de galleta por nombre
def bucar_galleta_nombre():
    nombre= input("Ingrese nombre a buscar:")
    for galleta in Galletas:
        if galleta.nombre.lower() == nombre.lower():
            print("Galleta encontrado!")
            galleta.mostrar_informacion()
            break
    else:
        print(f"No se ha encontrado la galleta {nombre}...")

#funcion 6. Eliminar registro de galleta pro nombre
def eliminar_nombre():
    nombre= input("Ingrese nombre de galleta a eliminar:")
    for galleta in Galletas:
        if galleta.nombre.lower() == nombre.lower():
            Galletas.remove(galleta)
            print(f"{nombre} ha sido removida exitosamente!")
            break
    else:
        print(f"{nombre} no ha sido encontrada...")

#Programa principal
while True:
    #Menú
    menu()
    opcion= input("Ingrese una opcion:")

    match opcion:
        case "1":
            print("---Registro de galleta básica---")
            registrar_galleta()
        case "2":
            print("---Registr de Galleta con Chispas---")
            registrar_galleta_chispas()
        case "3":
            print("---Registro de Galletas Rellenas---")
            registrar_galleta_rellena()
        case "4":
            print("---Lista de galletas")
            lista_galletas()
        case "5":
            print("---Buscar por nombre---")
            bucar_galleta_nombre()
        case "6":
            print("---Eliminar por nombre---")
            eliminar_nombre()
        case "7":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion no valida...")