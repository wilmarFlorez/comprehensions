# Ejercicio 1:
# enumerate() agrega un contador automatico al iterable
# Listar los archivos de un directorio numerados.

files = ["readme.md", "script.py", "foto.png", "datos.csv", "config.json"]

# Genera: "1. readme.md", "2. script.py", etc.



# Ejercicio 2:
# Extrae todas las extensiones(sin duplicados)

files = [
    "notas.txt",
    "foto.png",
    "script.py",
    "readme.md",
    "app.py",
    "data.csv",
    "banner.png",
]


# Ejercicio 3:
# Extrae el nombre del archivo
routes = [
    "/home/user/docs/notas.txt",
    "/home/user/imgs/foto.png",
    "/home/user/code/script.py",
]


# Ejercicio 4:
# Extrae los archivos .py

files = ["notas.txt", "foto.png", "script.py", "readme.md", "app.py", "data.csv"]


# Ejercicio 5:
# Etiquetar cada archivo como "código" o "dato" según su extensión
# Si termina en .py -> "código" si no -> "dato"

files = ["script.py", "datos.csv", "app.py", "reporte.csv", "utils.py"]


# Ejercicio 6:
# filtrar archivos con extensión png o jpg y tranformar a mayusculas

files = ["notas.txt", "foto.png", "script.py", "banner.jpg", "app.py", "icono.png"]

# Ejercicio 7:
# Genera lineas tipo: "script.py -> 2.1 KB"
metadata = {
    "script.py": "2.1 KB",
    "foto.png": "840 KB",
    "notas.txt": "12 KB",
    "readme.md": "4.3 KB",
}


# Ejercicio 8:
# Un diccionario que mapea cada archivo a su extensión
# Salida esperada:
"""
script.py       -> .py
foto.png        -> .png
datos.csv       -> .csv
readme.md       -> .md
app.py          -> .py
"""


files = ["script.py", "foto.png", "datos.csv", "readme.md", "app.py"]


# Ejercicio 9:
# Todos los archivos en una sola lista
# ejemplo ['notas.txt', 'readme.md', 'informe.pdf', 'foto.png', 'banner.jpg'...]

directories = {
    "docs": ["notas.txt", "readme.md", "informe.pdf"],
    "imgs": ["foto.png", "banner.jpg"],
    "code": ["script.py", "app.py", "utils.py"],
}


# Ejercicio 10:
# zip() combina dos (o más) iterables elemento a elemento
# Combinar nombres de archivos y sus tamaños

names = ["script.py", "foto.png", "datos.csv", "readme.md"]
sizes = [12_400, 840_000, 4_200, 3_100]