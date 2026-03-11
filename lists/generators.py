"""
Una list comprehension carga TODO en memoria de una vez.
Un generator expression calcula cada elemento bajo demanda (lazy).

  lista = [expr for x in iter]   # carga todo en RAM
  gen   = (expr for x in iter)   # genera uno a la vez

Usa () en lugar de []. Ideal para archivos grandes o streams.
sum(), any(), all(), max() consumen generators directamente.
"""

# Tienes millones de logs. Quieres sumar los tamaños sin cargarlos todos en memoria.

import random
random.seed(42)

files = [(f"log_{i:04d}.txt", random.randint(1_000, 500_000)) for i in range(10_1000)]

# ❌ List comp — carga 10.000 tamaños en RAM:
# total = sum([t for _, t in archivos])

# ✅ Generator — procesa uno a la vez, sin lista intermedia:
total = sum(t for _, t in files)


print(f"Archivos: {len(files):,}")
print(f"Total tamaño: {total / 1e6:.2f} MB")
print(f"Promedio: {total / len(files) / 1000:.1f} KB")