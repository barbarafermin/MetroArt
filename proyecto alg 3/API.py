from image import gestorImagen
from obras import ObraResumida, ObraDetallada
from departamento import Departamento
import time
import requests
from nacionalidades import nations
class ApiRequest():
    """Clase que representa las solicitudes a la API del MET.
    """
    def __init__(self):
        self.metUrl = "https://collectionapi.metmuseum.org"    
    
    def buscar_titulo_nombre(self, objectId):
        """Busca una obra en el MET por su ID y devuelve su título y nombre del artista.

        Args:
            objectId (int): El ID de la obra a buscar.

        Returns:
            ObraResumida: Un objeto ObraResumida con la información de la obra.
        """
        endpoint = f"/public/collection/v1/objects/{objectId}"
        respuesta = requests.get(f"{self.metUrl}{endpoint}")
        try:
            if respuesta.status_code == 200:
                data = respuesta.json()
                titulo = data.get("title", "No encontrado")
                nombre = data.get("artistDisplayName", "No encontrado")
                return ObraResumida(objectId, titulo, nombre)
            else:
                return None
        except Exception as e:
            print(f"[DEBUG] Error al decodificar JSON para objeto {objectId}: {e}")
            return None

    def obtener_departamentos(self):
        """Obtiene la lista de departamentos disponibles en el MET.

        Returns:
            list: Una lista de objetos Departamento que representan los departamentos disponibles.
        """
        endpoint = "/public/collection/v1/departments"
        respuesta = requests.get(f"{self.metUrl}{endpoint}")
        lista_departamentos = []
        if respuesta.status_code == 200:
            data = respuesta.json()
            departamentos = data.get("departments", [])
            for dep in departamentos:
                d = Departamento(dep.get("departmentId", 0), dep.get("displayName", ""))
                lista_departamentos.append(d)
            print("Departamentos disponibles:")
            for d in lista_departamentos:
                print(f"{d.departmentId} - {d.displayName}")
        elif respuesta.status_code == 404:
            print("El recurso solicitado no se pudo encontrar en el servidor.")
        elif respuesta.status_code == 500:
            print("Ha ocurrido un error en el servidor.")
        else:
            pass
        return lista_departamentos

    def obtener_nacionalidades(self):
        """Muestra las nacionalidades disponibles."""
        n = nations()
        lista = input("""Que nacionalidades desearia ver?:
                      1.- De la "A" a la "B"
                      2.- De la "C" a la "E" 
                      3.- De la "F" a la "I"
                      4.- De la "J" a la "O"
                      5.- De la "P" a la "Z"
                      -> """)
        if lista == "1":
            print(n.nacionalidades_ab)
        elif lista == "2":
            print(n.nacionalidades_ce)
        elif lista == "3":
            print(n.nacionalidades_fi)
        elif lista == "4":
            print(n.nacionalidades_jo)
        elif lista == "5":
            print(n.nacionalidades_pz)
        else:
            print("Opcion invalida, try again...")

    def buscar_obras_por_departamento(self, departamentId):
        """Busca obras en el MET por ID de departamento.

        Args:
            departamentId (int): El ID del departamento a buscar.

        Returns:
            list: Una lista de objetos ObraResumida que coinciden con la búsqueda.
        """
        endpoint = f"/public/collection/v1/objects?departmentIds={departamentId}"
        respuesta = requests.get(f"{self.metUrl}{endpoint}")
        lista_obras = []
        if respuesta.status_code == 200:
            obras = respuesta.json().get("objectIDs", [])
            if obras:
                for objectId in obras:
                    resultado = self.buscar_titulo_nombre(objectId)
                    if resultado is not None and resultado.titulo not in ["No encontrado", "Error JSON"]:
                        lista_obras.append(resultado)
                        print(f"Obra encontrada en el departamento {departamentId}: {resultado.objectId}, {resultado.titulo}, {resultado.artista}")
                    time.sleep(0.013)
            else:
                print(f"No se encontraron obras en el departamento {departamentId}.")
        elif respuesta.status_code == 404:
            print("El recurso solicitado no se pudo encontrar en el servidor.")
        elif respuesta.status_code == 500:
            print("Ha ocurrido un error en el servidor.")
        elif respuesta.status_code == 502:
            print("Error 502: El servidor de la API tuvo un problema. Intenta nuevamente más tarde o prueba con otro departamento.")
        else:
            print(f"Error inesperado: Código {respuesta.status_code}")
        return lista_obras

    def buscar_obras_por_nacionalidad(self, nacionalidad):
        """Busca obras en el MET por nacionalidad de autor.

        Args:
            nacionalidad (str): La nacionalidad del autor a buscar.

        Returns:
            list: Una lista de objetos ObraResumida que coinciden con la búsqueda.
        """
        endpoint = f"/public/collection/v1/search?artistOrCulture=true&q={nacionalidad.lower()}"
        respuesta = requests.get(f"{self.metUrl}{endpoint}")
        lista_obras = []
        if respuesta.status_code == 200:
            obras = respuesta.json().get("objectIDs", [])
            if obras:
                for objectId in obras:
                    resultado = self.buscar_titulo_nombre(objectId)
                    if resultado is not None and resultado.titulo not in ["No encontrado", "Error JSON"]:
                        lista_obras.append(resultado)
                        print(f"Obra encontrada de origen: {nacionalidad}: {resultado.objectId}, {resultado.titulo}, {resultado.artista}")
                    time.sleep(0.013)
            else:
                print(f"No se encontraron obras de origen {nacionalidad}.")
        elif respuesta.status_code == 404:
            print("El recurso solicitado no se pudo encontrar en el servidor.")
        elif respuesta.status_code == 500:
            print("Ha ocurrido un error en el servidor.")
        elif respuesta.status_code == 502:
            print("Error 502: El servidor de la API tuvo un problema. Intenta nuevamente más tarde o prueba con otro departamento.")
        else:
            print(f"Error inesperado: Código {respuesta.status_code}")
        return lista_obras
    
    def buscar_obras_por_nombre(self, nombre):
        """Busca obras en el MET por nombre de autor.

        Args:
            nombre (str): El nombre del autor a buscar.

        Returns:
            list: Una lista de objetos ObraResumida que coinciden con la búsqueda.
        """
        endpoint = f"/public/collection/v1/search?artistOrCulture=true&q={nombre.lower()}"
        respuesta = requests.get(f"{self.metUrl}{endpoint}")
        lista_obras = []
        if respuesta.status_code == 200:
            obras = respuesta.json().get("objectIDs", [])
            if obras:
                for objectId in obras:
                    resultado = self.buscar_titulo_nombre(objectId)
                    if resultado is not None and resultado.titulo not in ["No encontrado", "Error JSON"]:
                        lista_obras.append(resultado)
                        print(f"Obra encontrada de {nombre.capitalize()}: {resultado.objectId}, {resultado.titulo}, {resultado.artista}")
                    time.sleep(0.013)
            else:
                print(f"No se encontraron obras de {nombre}.")
        elif respuesta.status_code == 404:
            print("El recurso solicitado no se pudo encontrar en el servidor.")
        elif respuesta.status_code == 500:
            print("Ha ocurrido un error en el servidor.")
        elif respuesta.status_code == 502:
            print("Error 502: El servidor de la API tuvo un problema. Intenta nuevamente más tarde o prueba con otro departamento.")
        else:
            print(f"Error inesperado: Código {respuesta.status_code}")
        return lista_obras

    def obtener_detalles_obra(self, objectId):
        """Llama a la API para obtener los detalles de una obra en el MET.

        Args:
            objectId (int): El ID de la obra a consultar.

        Returns:
            ObraDetallada: Un objeto que contiene los detalles de la obra.
        """
        endpoint = f"/public/collection/v1/objects/{objectId}"
        try:
            respuesta = requests.get(f"{self.metUrl}{endpoint}")
            if respuesta.status_code == 200:
                data = respuesta.json()
                titulo = data.get("title", "No encontrado")
                artista = data.get("artistDisplayName", "No encontrado")
                nacionalidad = data.get("artistNationality", "No encontrado")
                fecha_nacimiento = data.get("artistBeginDate", "No encontrado")
                fecha_muerte = data.get("artistEndDate", "No encontrado")
                clasificacion = data.get("classification", "No encontrado")
                año = data.get("objectDate", "No encontrado")
                imagen = data.get("primaryImage", "No encontrado")
                obra = ObraDetallada(objectId, titulo, artista, nacionalidad, fecha_nacimiento, fecha_muerte, clasificacion, año, imagen)
                print(f"\nDetalles de la obra {objectId}:")
                print(f"Título: {obra.titulo}")
                print(f"Artista: {obra.artista}")
                print(f"Nacionalidad: {obra.nacionalidad}")
                print(f"Fecha de nacimiento: {obra.fecha_nacimiento}")
                print(f"Fecha de muerte: {obra.fecha_muerte}")
                print(f"Clasificación: {obra.clasificacion}")
                print(f"Año: {obra.año}")
                print(f"Imagen: {obra.imagen}")
                ver_imagen = input("Deseas ver la imagen de la obra? (si/no): ").lower()
                if ver_imagen == "si":
                    img = gestorImagen()
                    nombre_archivo = f"obra_{obra.titulo}_{objectId}"
                    img.guardar_imagen_desde_url(obra.imagen, nombre_archivo)
                else:
                    pass
                return obra
            else:
                print(f"No se encontró la obra {objectId} o hubo un error con la API. Código: {respuesta.status_code}")
                return None
        except Exception as e:
            print(f"Error al obtener detalles de la obra {objectId}: {e}")
            return None