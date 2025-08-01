import requests

def obtener_info_obra(obra_id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obra_id}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        titulo = datos.get("title", "Sin título")
        artista = datos.get("artistDisplayName", "Artista desconocido")
        url_imagen = datos.get("primaryImage", "")
        return titulo, artista, url_imagen
    else:
        return None, None, None

def descargar_imagen(url_imagen):
    if url_imagen:
        respuesta = requests.get(url_imagen)
        if respuesta.status_code == 200:
            return respuesta.content
    return None
