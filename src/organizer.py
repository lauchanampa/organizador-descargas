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

    nuevo_destino = carpeta_destino / archivo.name

    archivo.rename(nuevo_destino)

    print(f"'{archivo.name}' movido a '{categoria}'.")
                
                