def actualizar_estadisticas(estadisticas: dict[str, int], categoria: str):
    """
    Incrementa en 1 el contador de la categoría recibida.
    """

    if categoria in estadisticas:
        estadisticas[categoria] += 1
    else:
        estadisticas[categoria] = 1


def mostrar_estadisticas(estadisticas: dict[str, int]):
    """
    Muestra un resumen de los archivos organizados.
    """

    print("\n========== ESTADÍSTICAS ==========\n")

    total = 0

    for categoria, cantidad in estadisticas.items():
        print(f"{categoria}: {cantidad}")
        total += cantidad

    print("\n----------------------------------")
    print(f"Total de archivos procesados: {total}")