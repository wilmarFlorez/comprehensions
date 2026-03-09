import os

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


extensions = [os.path.splitext(f)[1] for f in files]

# Elimina duplicados usando un set
uniques = list(set(extensions))

print(uniques)
