class ObraDetallada:
    """Clase que representa una obra de arte detallada en el MET, con informacion como:
    titulo, nombre del artista, nacionalidad del artista, fecha de nacimiento, fecha de 
muerte, clasificacion, año de creación e imagen de la obra.
    """
    def __init__(self, objectId, titulo, artista, nacionalidad, fecha_nacimiento, fecha_muerte, clasificacion, año, imagen):
        self.objectId = objectId
        self.titulo = titulo
        self.artista = artista
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte
        self.clasificacion = clasificacion
        self.año = año
        self.imagen = imagen

class ObraResumida:
    def __init__(self, objectId, titulo, artista):
        self.objectId = objectId
        self.titulo = titulo
        self.artista = artista

