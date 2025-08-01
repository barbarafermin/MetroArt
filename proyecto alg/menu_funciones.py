from API import obtener_info_obra, descargar_imagen
from PIL import Image

def mostrar_menu():
    while True:
        print("""Bienvenido a MetroArt!!!
                 
                Que deseas hacer:
                1. Consultar obra del MET
                2. Salir""")

        opcion = input("-> ")

        if opcion == "1":
            consultar_obra()
        elif opcion == "2":
            print("Gracias por su visita, see u later!!")
            break
        else:
            print("Opcion invalida, try again...")

def consultar_obra():
    obra_id = input("Ingrese el ID de la obra: ")
    if obra_id.isdigit():
        titulo, artista, url_imagen = obtener_info_obra(int(obra_id))
        if titulo and artista:
            print(f"Titulo: {titulo}")
            print(f"Artista: {artista}")

            if url_imagen:
                contenido = descargar_imagen(url_imagen)
                if contenido:
                    nombre = input("Nombre del archivo para guardar la imagen (sin extension): ")
                    ruta = f"{nombre}.jpg"
                    with open(ruta, "wb") as f:
                        f.write(contenido)
                    print(f"Imagen guardada como {ruta}")




                    '''Aqui se abre la imagen con Pillow (PIL)'''

                    imagen = Image.open(ruta)
                    print(f"Tamaño de la imagen: {imagen.size}")
                    print(f"Modo de color: {imagen.mode}")
                else:
                    print("No se pudo descargar la imagen.")
            else:
                print("Esta obra no tiene imagen disponible.")
        else:
            print("No se encontraron datos para ese ID.")
    else:
        print("El ID debe ser numérico.")
