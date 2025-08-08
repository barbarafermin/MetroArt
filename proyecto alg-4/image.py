import requests
from PIL import Image
from io import BytesIO

class gestorImagen():
    """Clase que gestiona la visualización y descarga de imágenes.
    """
    def __init__(self):
        pass
    
    def mostrar_imagen(self, url):
        """Muestra una imagen desde una URL.

        Args:
            url (str): La URL de la imagen a mostrar.
        """
        try:
            respuesta = requests.get(url)
            if respuesta.status_code == 200:
                imagen = Image.open(BytesIO(respuesta.content))
                imagen.show()
            else:
                print(f"Error al descargar la imagen: {respuesta.status_code}")
        except Exception as e:
            print(f"Error al mostrar la imagen: {e}")

    def mostrar_imagen_desde_archivo(self, nombre_archivo):
        """Muestra una imagen desde un archivo local.

        Args:
            nombre_archivo (str): La ruta del archivo de imagen a mostrar.
        """
        try:
            imagen = Image.open(nombre_archivo)
            imagen.show()
        except Exception as e:
            print(f"Error al mostrar la imagen desde el archivo: {e}")

    def guardar_imagen_desde_url(self, url, nombre_archivo):
        """Guarda una imagen desde una URL en un archivo local.

        Args:
            url (str): La URL de la imagen a descargar.
            nombre_archivo (str): El nombre del archivo donde se guardará la imagen.
        """
        try:
            ext = url.split('.')[-1]
            if ext.lower() not in ['jpg', 'jpeg', 'png', 'gif']:
                print("Formato de imagen no soportado. Usa jpg, jpeg, png o gif.")
                return
            nombre_archivo += f".{ext}"
            respuesta = requests.get(url)
            if respuesta.status_code == 200:
                imagen = Image.open(BytesIO(respuesta.content))
                imagen.save(nombre_archivo)
                print(f"Imagen guardada como {nombre_archivo}")
                self.mostrar_imagen_desde_archivo(nombre_archivo)
            else:
                print(f"Error al descargar la imagen: {respuesta.status_code}")
        except Exception as e:
            print(f"Error al guardar la imagen: {e}")


