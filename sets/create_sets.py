# Usuarios únicos que tienen archivos en el directorio
# Salida esperada ['alice', 'bob', 'charlie']

logs = [
    ("alice",   "script.py"),
    ("bob",     "foto.png"),
    ("alice",   "datos.csv"),
    ("charlie", "readme.md"),
    ("bob",     "config.json"),
    ("alice",   "app.py"),
]

users = {usuario for usuario, file in logs}

print(f"Usuarios únicos: {sorted(users)}")
