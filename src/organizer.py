from pathlib import Path

def obtener_carpeta_descargas() -> Path:
    """
    Devuelve la ruta de la carpeta Descargas del usuario.
    """
    return Path.home() / "Downloads"

def obtener_archivos(carpeta: Path) -> List[Path]:
    """
    Devuelve una lista con todos los archivos de la carpeta recibida.
    """

    archivos = []

    "iterdir() es un método que recorre todo el contenido de una carpeta."
    for archivo in carpeta.iterdir():
        if archivo.is_file():
            "el append es un add para el array"
            archivos.append(archivo)

    return archivos   

def crear_carpetas(carpeta_descargas: Path, categorias: set[str]):

    for categoria in categorias:

        carpeta_destino = carpeta_descargas / categoria

        if not carpeta_destino.exists():

            carpeta_destino.mkdir()

            print(f"Carpeta '{categoria}' creada.")

def mover_archivo(archivo: Path, categoria: str, carpeta_descargas: Path):
    """
    Mueve un archivo a la carpeta correspondiente según su categoría.
    Si la carpeta no existe, la crea automáticamente.
    """

    carpeta_destino = carpeta_descargas / categoria

    if not carpeta_destino.exists():
        carpeta_destino.mkdir()
        print(f"Carpeta '{categoria}' creada.")

    nuevo_destino = obtener_nombre_disponible(carpeta_destino, archivo)

    archivo.rename(nuevo_destino)

    print(f"'{archivo.name}' movido a '{categoria}'.")


def obtener_nombre_disponible(carpeta_destino: Path, archivo: Path) -> Path:
    """
    Devuelve una ruta disponible para el archivo.
    Si ya existe un archivo con el mismo nombre, agrega (1), (2), (3), etc.
    """

    nuevo_destino = carpeta_destino / archivo.name

    if not nuevo_destino.exists():
        return nuevo_destino

    contador = 1
    nombre_base = archivo.stem
    extension = archivo.suffix

    while True:

        nuevo_nombre = f"{nombre_base} ({contador}){extension}"

        nuevo_destino = carpeta_destino / nuevo_nombre

        if not nuevo_destino.exists():
            return nuevo_destino

        contador += 1
        
                
                