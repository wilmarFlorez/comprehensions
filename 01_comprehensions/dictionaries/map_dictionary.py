import os

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

# {"script.py": ".py", "foto.png": ".png",...}
extensions = {file: os.path.splitext(file)[1] for file in files}

for name, ext in extensions.items():
    print(f"{name:15} -> {ext}")
