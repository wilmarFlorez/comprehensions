# ============================================================
#  COLLECTIONS — estructuras de datos especializadas
# ============================================================
from collections import Counter, deque, namedtuple, defaultdict


# Counter — contar ocurrencias
words = "the quick brown fox jumps over the lazy dog the fox".split()
count = Counter(words)

print("TOP 3:", count.most_common(3))
# [('the', 3), ('fox', 2), ('quick', 1)]

# Operaciones entre Counters
a = Counter("abracadabra")
b = Counter("alacazam")
print("Intersección:", a & b)  # elementos comunes mínimos
print("Unión:", a | b)         # elementos comunes máximos


# deque — cola de doble extremo (O(1) en ambos lados)
recent = deque(maxlen=3)
for item in ["a", "b", "c", "d", "e"]:
    recent.append(item)
print(f"\nÚltimos 3: {list(recent)}")  # ['c', 'd', 'e']

# Rotar
d = deque([1, 2, 3, 4, 5])
d.rotate(2)   # mueve 2 del final al inicio
print(f"Rotado: {list(d)}")  # [4, 5, 1, 2, 3]


# namedtuple — tupla con nombres
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"\nPoint: {p}, x={p.x}, y={p.y}")
print(f"Distancia: {(p.x**2 + p.y**2) ** 0.5:.2f}")


# defaultdict con función fábrica
word_index = defaultdict(list)
for i, word in enumerate(words):
    word_index[word].append(i)
print(f"\nÍndice: {dict(word_index)}")
