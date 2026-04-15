# ============================================================
#  LEVEL 1 — FOR LOOPS CLÁSICOS
#  Resuelve usando solo for, if, variables y append.
#  NO uses comprehensions, map, filter ni lambda.
# ============================================================
from data import access_log, CODE_EXTENSIONS, EXPECTED

# Paso 1: Filtrar solo accesos a archivos de código (.py, .sh)
code_accesses = []
# tu código aquí ...


# Paso 2: Extraer solo el nombre del archivo (sin la ruta)
# Convierte ("alice", "/code/app.py", "2025-03-01") -> ("alice", "app.py")
named_accesses = []
# tu código aquí ...


# Paso 3: Agrupar por usuario
# Resultado: {"alice": ["app.py", "utils.py", ...], "bob": [...]}
grouped = {}
# tu código aquí ...


# Paso 4: Generar el reporte ordenado
report = []
# tu código aquí ...


# ============================================================
#  VERIFICACIÓN
# ============================================================
assert report == EXPECTED, f"\nEsperado:\n{EXPECTED}\n\nObtenido:\n{report}"
print("✓ Level 1 (for loops) — COMPLETADO")
for line in report:
    print(f"  {line}")
