# ============================================================
#  LEVEL 5 — FUNCIONAL (map, filter, reduce, lambda)
#  Resuelve usando SOLO funciones de orden superior.
#  NO uses comprehensions ni for loops explícitos.
#  Herramientas permitidas: map, filter, reduce, lambda, sorted
# ============================================================
from functools import reduce
from data import access_log, CODE_EXTENSIONS, EXPECTED

# Paso 1: Filtrar accesos a código usando filter() + lambda
code_accesses = ___


# Paso 2: Extraer (usuario, nombre_archivo) usando map() + lambda
named_accesses = ___


# Paso 3: Agrupar por usuario usando reduce()
# reduce() recibe: función(acumulador, elemento) -> nuevo_acumulador
# Empieza con un dict vacío como acumulador.
# Pista:
#   reduce(lambda acc, item: ..., named_accesses, {})
#   Dentro del lambda necesitas actualizar el dict.
#   Truco: {**acc, user: acc.get(user, []) + [fname]}
grouped = ___


# Paso 4: Generar reporte usando map() sobre el dict
report = ___


# ============================================================
#  VERIFICACIÓN
# ============================================================
assert report == EXPECTED, f"\nEsperado:\n{EXPECTED}\n\nObtenido:\n{report}"
print("✓ Level 5 (funcional) — COMPLETADO")
for line in report:
    print(f"  {line}")
