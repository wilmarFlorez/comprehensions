# ============================================================
#  LEVEL 4 — SIN IMPORTS
#  Resuelve sin usar NINGÚN import (ni os, ni collections).
#  Solo builtins: str.split(), str.rsplit(), str.endswith(),
#  sorted(), dict, list, tuple, etc.
# ============================================================

# Copia local de los datos (sin depender de import)
access_log = [
    ("alice", "/code/app.py", "2025-03-01"),
    ("bob", "/imgs/banner.png", "2025-03-01"),
    ("alice", "/code/utils.py", "2025-03-02"),
    ("charlie", "/docs/readme.md", "2025-03-02"),
    ("bob", "/code/server.py", "2025-03-03"),
    ("alice", "/imgs/logo.png", "2025-03-03"),
    ("charlie", "/code/deploy.sh", "2025-03-04"),
    ("alice", "/code/test_app.py", "2025-03-04"),
    ("bob", "/docs/api.md", "2025-03-05"),
    ("charlie", "/code/main.py", "2025-03-05"),
    ("alice", "/code/models.py", "2025-03-06"),
    ("bob", "/code/views.py", "2025-03-06"),
    ("charlie", "/imgs/icon.svg", "2025-03-07"),
    ("alice", "/docs/changelog.md", "2025-03-07"),
    ("bob", "/code/helpers.py", "2025-03-08"),
]

CODE_EXTENSIONS = (".py", ".sh")

EXPECTED = [
    "alice    (4): app.py, utils.py, test_app.py, models.py",
    "bob      (3): server.py, views.py, helpers.py",
    "charlie  (2): deploy.sh, main.py",
]

# ============================================================
#  RESTRICCIÓN: no puedes usar os.path ni ningún import.
#  Para obtener el nombre del archivo usa str.rsplit("/", 1)
#  Para obtener la extensión usa str.rsplit(".", 1)
# ============================================================

# Paso 1: Filtrar archivos de código SIN os.path
# Pista: path.rsplit(".", 1)[-1] te da la extensión sin el punto
code_accesses = ___


# Paso 2: Extraer nombre del archivo SIN os.path.basename
# Pista: path.rsplit("/", 1)[-1] te da el nombre del archivo
named_accesses = ___


# Paso 3: Agrupar por usuario SIN defaultdict ni collections
grouped = ___


# Paso 4: Generar reporte
report = ___


# ============================================================
#  VERIFICACIÓN
# ============================================================
assert report == EXPECTED, f"\nEsperado:\n{EXPECTED}\n\nObtenido:\n{report}"
print("✓ Level 4 (sin imports) — COMPLETADO")
for line in report:
    print(f"  {line}")
