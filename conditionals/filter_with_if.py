# Extrae los archivos .py

files = ["notas.txt", "foto.png", "script.py", "readme.md", "app.py", "data.csv"]

pythons = [file for file in files if file.endswith(".py")]

print(pythons)