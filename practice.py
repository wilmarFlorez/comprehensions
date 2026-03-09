# Ejercicio 1:
# enumerate() agrega un contador automatico al iterable
# Listar los archivos de un directorio numerados.

files = ["readme.md", "script.py", "foto.png", "datos.csv", "config.json"]

# Genera: "1. readme.md", "2. script.py", etc.

enumerate_files = [f"{index} {file}" for index, file in enumerate(files, 1)]

print("\nEjercicio 1:")



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

print("\nEjercicio 2:")



# Ejercicio 3:
# Extrae el nombre del archivo
routes = [
    "/home/user/docs/notas.txt",
    "/home/user/imgs/foto.png",
    "/home/user/code/script.py",
]

print("\nEjercicio 3:")



# Ejercicio 4:
# Extrae los archivos .py

files = ["notas.txt", "foto.png", "script.py", "readme.md", "app.py", "data.csv"]

print("\nEjercicio 4:")


# Ejercicio 5:
# Etiquetar cada archivo como "código" o "dato" según su extensión
# Si termina en .py -> "código" si no -> "dato"

files = ["script.py", "datos.csv", "app.py", "reporte.csv", "utils.py"]
print("\nEjercicio 5:")


# Ejercicio 6:
# filtrar archivos con extensión png o jpg y tranformar a mayusculas

files = ["notas.txt", "foto.png", "script.py", "banner.jpg", "app.py", "icono.png"]

print("\nEjercicio 6:")


# Ejercicio 7:
# Genera lineas tipo: "script.py -> 2.1 KB"
metadata = {
    "script.py": "2.1 KB",
    "foto.png": "840 KB",
    "notas.txt": "12 KB",
    "readme.md": "4.3 KB",
}

print("\nEjercicio 7:")



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


print("\nEjercicio 8:")



# Ejercicio 9:
# Todos los archivos en una sola lista
# ejemplo ['notas.txt', 'readme.md', 'informe.pdf', 'foto.png', 'banner.jpg'...]

directories = {
    "docs": ["notas.txt", "readme.md", "informe.pdf"],
    "imgs": ["foto.png", "banner.jpg"],
    "code": ["script.py", "app.py", "utils.py"],
}

print("\nEjercicio 9:")



# Ejercicio 10:
# zip() combina dos (o más) iterables elemento a elemento
# Combinar nombres de archivos y sus tamaños

names = ["script.py", "foto.png", "datos.csv", "readme.md"]
sizes = [12_400, 840_000, 4_200, 3_100]

print("\nEjercicio 10:")
