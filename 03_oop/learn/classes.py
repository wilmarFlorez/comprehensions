# ============================================================
#  CLASSES — Lo esencial
#  __init__, métodos, propiedades, herencia.
# ============================================================


class File:
    """Representa un archivo con nombre y tamaño."""

    def __init__(self, name: str, size_bytes: int):
        self.name = name
        self.size_bytes = size_bytes

    @property
    def extension(self):
        return "." + self.name.rsplit(".", 1)[-1] if "." in self.name else ""

    @property
    def size_kb(self):
        return self.size_bytes / 1000

    def __repr__(self):
        return f"File({self.name!r}, {self.size_kb:.1f} KB)"

    def __eq__(self, other):
        return isinstance(other, File) and self.name == other.name

    def __lt__(self, other):
        return self.size_bytes < other.size_bytes


files = [
    File("script.py", 12_400),
    File("foto.png", 840_000),
    File("notas.txt", 4_200),
    File("readme.md", 3_100),
]

print("Todos:", files)
print("Ordenados:", sorted(files))
print("Mayor:", max(files))
print("Extensión:", files[0].extension)
