
import time
import requests
from nacionalidades import nations
class ApiRequest():
    def __init__(self):
        self.metUrl = "https://collectionapi.metmuseum.org"    
    
    def buscar_titulo_nombre(self, objectId):
        endpoint = f"/public/collection/v1/objects/{objectId}"
        respuesta = requests.get(f"{self.metUrl}{endpoint}")
        try:
            if respuesta.status_code == 200:
                data = respuesta.json()
                titulo = data.get("title", str)
                nombre = data.get("artistDisplayName", str)
                return (objectId, titulo, nombre)
            else:
                return (objectId, "No encontrado", "No encontrado")
        except Exception as e:
            print(f"[DEBUG] Error al decodificar JSON para objeto {objectId}: {e}")
            return (objectId, "Error JSON", "Error JSON")

    def obtener_departamentos(self):
        endpoint = "/public/collection/v1/departments"
        respuesta = requests.get(f"{self.metUrl}{endpoint}")
        if respuesta.status_code == 200:
            print(f"Los departamentos son: {respuesta.json()}")
        elif respuesta.status_code == 404:
            print("El recurso solicitado no se pudo encontrar en el servidor.")
        elif respuesta.status_code == 500:
            print("Ha ocurrido un error en el servidor.")
        else:
            pass 

    def obtener_nacionalidades(self):
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
        
        endpoint = f"/public/collection/v1/objects?departmentIds={departamentId}"
        respuesta = requests.get(f"{self.metUrl}{endpoint}")
        if respuesta.status_code == 200:
            obras = respuesta.json().get("objectIDs", [])
            if obras:
                for objectId in obras:
                    resultado = self.buscar_titulo_nombre(objectId)
                    if resultado[1] not in ["No encontrado", "Error JSON"]:
                        print(f"Obra encontrada en el departamento {departamentId}: {resultado}")
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

    def buscar_obras_por_nacionalidad(self, nacionalidad):
        endpoint = f"/public/collection/v1/search?artistOrCulture=true&q={nacionalidad.lower()}"
        respuesta = requests.get(f"{self.metUrl}{endpoint}")
        if respuesta.status_code == 200:
            obras = respuesta.json().get("objectIDs", [])
            if obras:
                for objectId in obras:
                    resultado = self.buscar_titulo_nombre(objectId)
                    if resultado[1] not in ["No encontrado", "Error JSON"]:
                        print(f"Obra encontrada de origen: {nacionalidad}: {resultado}")
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
    
    def buscar_obras_por_nombre(self, nombre):
        endpoint = f"/public/collection/v1/search?artistOrCulture=true&q={nombre.lower()}"
        respuesta = requests.get(f"{self.metUrl}{endpoint}")
        if respuesta.status_code == 200:
            obras = respuesta.json().get("objectIDs", [])
            if obras:
                for objectId in obras:
                    resultado = self.buscar_titulo_nombre(objectId)
                    if resultado[1] not in ["No encontrado", "Error JSON"]:
                        print(f"Obra encontrada de {nombre}: {resultado}")
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

    def obtener_detalles_obra(self, objectId):
        """Obtiene y muestra los detalles completos de una obra por su ID."""
        endpoint = f"/public/collection/v1/objects/{objectId}"
        try:
            respuesta = requests.get(f"{self.metUrl}{endpoint}")
            if respuesta.status_code == 200:
                data = respuesta.json()
                titulo = data.get("title", "No encontrado")
                artista = data.get("artistDisplayName", "No encontrado")
                nacionalidad = data.get("artistNationality", "No encontrado")
                nacimiento = data.get("artistBeginDate", "No encontrado")
                muerte = data.get("artistEndDate", "No encontrado")
                clasificacion = data.get("classification", "No encontrado")
                año = data.get("objectDate", "No encontrado")
                imagen = data.get("primaryImage", "No encontrado")
                print(f"\nDetalles de la obra {objectId}:")
                print(f"Título: {titulo}")
                print(f"Artista: {artista}")
                print(f"Nacionalidad: {nacionalidad}")
                print(f"Fecha de nacimiento: {nacimiento}")
                print(f"Fecha de muerte: {muerte}")
                print(f"Clasificación: {clasificacion}")
                print(f"Año: {año}")
                print(f"Imagen: {imagen}")
            else:
                print(f"No se encontró la obra {objectId} o hubo un error con la API. Código: {respuesta.status_code}")
        except Exception as e:
            print(f"Error al obtener detalles de la obra {objectId}: {e}")