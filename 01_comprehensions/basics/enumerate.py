# enumerate() agrega un contador automatico al iterable
# Listar los archivos de un directorio numerados.

files = ["readme.md", "script.py", "foto.png", "datos.csv", "config.json"]

# Genera: "1. readme.md", "2. script.py", etc.

enumerate_files = [f"{i+1:2}: {name}" for i, name in enumerate(files)]

for line in enumerate_files:
    print(line)