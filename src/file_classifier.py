from pathlib import Path

CATEGORIAS = {
    "PDF": [".pdf"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Musica": [".mp3", ".wav", ".flac"],
    "Comprimidos": [".zip", ".rar", ".7z"],
    "Documentos": [".doc", ".docx", ".txt", ".odt", ".rtf"],
    "Hojas de Calculo": [".xls", ".xlsx", ".csv", ".ods" ],
    "Presentaciones": [".ppt", ".pptx", ".odp"],
    "Ejecutables": [".exe", ".msi"]
}

def obtener_categoria(archivo: Path) -> str:
    "con el lower .PDF, .Pdf y .pdf se tratan exactamente igual."
    extension = archivo.suffix.lower()

    "Para cada categoría y su lista de extensiones dentro del diccionario..."
    for categoria, extensiones in CATEGORIAS.items():
        "Si la extensión pertenece a esta lista de extensiones, devolvé el nombre de la categoría."
        if extension in extensiones:
            return categoria

    return "Otro"