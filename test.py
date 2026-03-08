# zip() combina dos (o más) iterables elemento a elemento

# Combinar nombres de archivos y sus tamaños

names = ["script.py", "foto.png", "datos.csv", "readme.md"]
sizes = [12_400, 840_000, 4_200, 3_100]


report = [ (name, size//1000) for name, size in zip(names, sizes)]

for name, size in report:
    print(f"{name:15} {size:>6} MB")