# ============================================================
#  ITERTOOLS — herramientas para iteración avanzada
# ============================================================
import itertools

# chain — concatenar iterables sin copiar
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

print(list(itertools.chain(a, b, c)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# islice — rebanar sin cargar todo en memoria (como [start:stop])
infinitos = itertools.count(1)  # 1, 2, 3, 4, ...
print(list(itertools.islice(infinitos, 5)))  # [1, 2, 3, 4, 5]


# groupby — agrupar elementos consecutivos iguales
# IMPORTANTE: los datos DEBEN estar ordenados por la clave
datos = [
    ("code", "app.py"),
    ("code", "utils.py"),
    ("docs", "readme.md"),
    ("docs", "api.md"),
    ("imgs", "foto.png"),
]

for key, group in itertools.groupby(datos, key=lambda x: x[0]):
    files = [f for _, f in group]
    print(f"{key}: {files}")


# product — producto cartesiano (reemplaza for anidados)
colors = ["rojo", "azul"]
sizes = ["S", "M", "L"]

combos = list(itertools.product(colors, sizes))
print(f"\nCombinaciones ({len(combos)}):")
for color, size in combos:
    print(f"  {color}-{size}")


# starmap — map() pero desempaquetando tuplas
pairs = [(2, 3), (4, 5), (6, 7)]
print(list(itertools.starmap(lambda a, b: a * b, pairs)))  # [6, 20, 42]
