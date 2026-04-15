# Genera lineas tipo: "script.py -> 2.1 KB"
metadata = {
    "script.py": "2.1 KB",
    "foto.png": "840 KB",
    "notas.txt": "12 KB",
    "readme.md": "4.3 KB",
}

# Genera lineas tipo: "script.py -> 2.1 KB"
report = [f"{name:15} -> {size}" for name, size in metadata.items()]

for line in report:
    print(line)
