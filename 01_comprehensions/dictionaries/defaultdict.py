from collections import defaultdict

# Agrupa los archivos del directorio por extensión para saber cuántos hay de cada tipo.

files = [
    "script.py",
    "foto.png",
    "app.py",
    "datos.csv",
    "banner.jpg",
    "utils.py",
    "reporte.csv",
    "logo.png",
]

# Agrupa por extensión
groups = defaultdict(list) 
for f in files:
    ext = f.rsplit(".")[1]
    groups[ext].append(f)


print(groups)

# List comp para el reporte final
report = [
    f".{ext:6}->{len(files):2} archivo(s): {', '.join(files)}"
    for ext, files in sorted(groups.items())
]

for line in report:
    print(line)