from API import ApiRequest
from PIL import Image


class menu():
    def __init__(self):
        pass

    def consultar_obra(self):
        accion = input("""Que deseas hacer?
                    1. Ver lista de obras por departamento
                    2. Ver lista de obras por Nacionalidad de autor
                    3. Ver lista de obras por nombre de autor
                    ->   """)
        if accion.isdigit():
            if accion == "1":
                api = ApiRequest()
                api.obtener_departamentos()
                buscarObraDepartamento = input("Deseas buscar una obra por departamento? (si/no): ").lower()
                if buscarObraDepartamento == "si":
                    departamentId = int(input("Introduce el id del departamento: "))
                    api.buscar_obras_por_departamento(departamentId)
            elif accion == "2":
                api = ApiRequest()
                api.obtener_nacionalidades()
                buscarObraNacionalidad = input("Deseas buscar una obra por nacionalidad? (si/no): ").lower()
                if buscarObraNacionalidad == "si":
                    nacionalidad = input("Introduce la nacionalidad del autor: ")
                    api.buscar_obras_por_nacionalidad(nacionalidad)
            elif accion == "3":
                api = ApiRequest()
                nombre = input("Introduce el nombre del autor: ")
                api.buscar_obras_por_nombre(nombre)
        else:
            print("Opcion invalida, try again...")

    def obtener_detalles_obra(self, objectId):
        api = ApiRequest()
        resultado = api.obtener_detalles_obra(objectId)

    def mostrar_menu(self):
        while True:
            print("""Bienvenido a MetroArt!!!
                    
                    Que deseas hacer:
                    1. Consultar obras del MET
                    2. Obtener detalles de una obra
                    3. Salir""")

            opcion = input("-> ")

            if opcion == "1":
                self.consultar_obra()
            elif opcion == "2":
                objectId = int(input("Introduce el ID de la obra: "))
                self.obtener_detalles_obra(objectId)
                accion = input("Deseas ver la imagen de la obra? (si/no): ").lower()
                if accion == "si":
                    pass

            elif opcion == "3":
                print("Gracias por su visita, see u later!!")
                break
            else:
                print("Opcion invalida, try again...")


