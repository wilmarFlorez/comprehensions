# ============================================================
#  LEVEL 3 — ONE-LINERS
#  Resuelve TODO el problema en UNA sola expresión por paso.
#  Máximo 4 líneas de código (una por paso). Sin variables auxiliares.
#  Puedes anidar comprehensions y usar walrus operator (:=).
# ============================================================
from data import access_log, CODE_EXTENSIONS, EXPECTED

# Combina pasos 1+2 en una sola list comprehension:
# Filtra por extensión Y extrae nombre del archivo a la vez.
named_code = ___


# Paso 3 en una sola expresión:
# Agrupa usando un truco: dict comp + list comp anidado.
# Pista: primero obtener los usuarios únicos, luego filtrar archivos por cada uno.
grouped = ___


# Paso 4 en una sola expresión:
report = ___


# ============================================================
#  VERIFICACIÓN
# ============================================================
assert report == EXPECTED, f"\nEsperado:\n{EXPECTED}\n\nObtenido:\n{report}"
print("✓ Level 3 (one-liners) — COMPLETADO")
for line in report:
    print(f"  {line}")
