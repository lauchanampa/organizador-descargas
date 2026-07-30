# 📂 Download Organizer

<p align="center">

Organiza automáticamente los archivos de tu carpeta **Descargas** según su tipo, creando las carpetas necesarias y evitando archivos duplicados.

</p>

---

## ✨ Características

- 📁 Detecta automáticamente la carpeta **Descargas** del usuario.
- 📄 Clasifica los archivos según su extensión.
- 📂 Crea automáticamente las carpetas necesarias.
- 🚫 Evita sobrescribir archivos con el mismo nombre.
- 📊 Muestra estadísticas al finalizar la organización.
- 🧩 Código modular y fácil de mantener.

---

## 📸 Ejemplo

### Antes

```text
Downloads/
│
├── foto.jpg
├── parcial.pdf
├── video.mp4
├── musica.mp3
└── archivo.zip
```

### Después

```text
Downloads/
│
├── 📁 Imagenes/
│      └── foto.jpg
│
├── 📁 Documentos/
│      └── parcial.pdf
│
├── 📁 Videos/
│      └── video.mp4
│
├── 📁 Musica/
│      └── musica.mp3
│
└── 📁 Comprimidos/
       └── archivo.zip
```

---

## 📊 Estadísticas

Al finalizar la ejecución, el programa muestra un resumen como este:

```text
========== ESTADÍSTICAS ==========

Imagenes: 8
Documentos: 5
Videos: 2
Musica: 4
Comprimidos: 1
PDF: 3

----------------------------------
Total de archivos procesados: 23
```

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio.

```bash
git clone https://github.com/lauchanampa/organizador-descargas.git
```

2. Entrar al proyecto.

```bash
cd organizador-descargas
```

3. Ejecutar el programa.

```bash
python src/main.py
```

---

## 📌 Categorías soportadas

- 📄 Documentos
- 📕 PDF
- 🖼️ Imágenes
- 🎬 Videos
- 🎵 Música
- 📊 Presentaciones
- 📦 Comprimidos
- ⚙️ Ejecutables
- 📂 Otros

---

## 📄 Licencia

Este proyecto está distribuido bajo la licencia **MIT**.

---

<p align="center">

Hecho con ❤️ mientras aprendía Python y desarrollo de software.

</p>
