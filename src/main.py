from organizer import obtener_carpeta_descargas, obtener_archivos, crear_carpetas
from file_classifier import obtener_categoria

def main():
    print("=== Organizador de Descargas ===\n")

    carpeta_descargas = obtener_carpeta_descargas()

    print(f"Carpeta encontrada: {carpeta_descargas}\n")

    archivos = obtener_archivos(carpeta_descargas)

    "el len es un contador"
    print(f"Se encontraron {len(archivos)} archivos:\n")

    for archivo in archivos:
        print(f"- {archivo.name}")

    print("\n")
    
    for archivo in archivos:
        categoria = obtener_categoria(archivo)

        print(f"{archivo.name} --> {categoria}")

    print("\n")

    categorias = set()

    for archivo in archivos:
        categoria = obtener_categoria(archivo)
        categorias.add(categoria)  

    crear_carpetas(carpeta_descargas, categorias)

if __name__ == "__main__":
    main()    