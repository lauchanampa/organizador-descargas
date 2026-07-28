from organizer import obtener_carpeta_descargas, obtener_archivos

def main():
    print("=== Organizador de Descargas ===\n")

    carpeta_descargas = obtener_carpeta_descargas()

    print(f"Carpeta encontrada: {carpeta_descargas}\n")

    archivos = obtener_archivos(carpeta_descargas)

    print(f"Se encontraron {len(archivos)} archivos:\n")

    for archivo in archivos:
        print(f"- {archivo.name}")


if __name__ == "__main__":
    main()    