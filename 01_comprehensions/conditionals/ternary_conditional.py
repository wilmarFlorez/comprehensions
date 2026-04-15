# Etiquetar cada archivo como "código" o "dato" según su extensión
# Si termina en .py -> "código" si no -> "dato"

files = ["script.py", "datos.csv", "app.py", "reporte.csv", "utils.py"]


labels = [(f, "código") if f.endswith(".py") else (f, "dato") for f in files]

for name, type in labels:
    print(f"{name:15} -> {type}")
