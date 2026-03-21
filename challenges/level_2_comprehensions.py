# ============================================================
#  LEVEL 2 — COMPREHENSIONS
#  Reescribe cada paso usando list/dict comprehensions.
#  Cada paso debe ser UNA sola comprehension.
# ============================================================
from data import access_log, CODE_EXTENSIONS, EXPECTED

# Paso 1: Filtrar accesos a código (list comprehension con if)
code_accesses = ___


# Paso 2: Extraer (usuario, nombre_archivo) — list comprehension con transformación
named_accesses = ___


# Paso 3: Agrupar por usuario
# Pista: este paso necesita un dict + for (o defaultdict). No todo cabe en un comprehension.
grouped = {}
for user, fname in named_accesses:
    grouped.setdefault(user, []).append(fname)


# Paso 4: Generar el reporte (list comprehension sobre el dict)
report = ___


# ============================================================
#  VERIFICACIÓN
# ============================================================
assert report == EXPECTED, f"\nEsperado:\n{EXPECTED}\n\nObtenido:\n{report}"
print("✓ Level 2 (comprehensions) — COMPLETADO")
for line in report:
    print(f"  {line}")
