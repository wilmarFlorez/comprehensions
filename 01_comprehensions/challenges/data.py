# Datos compartidos para todos los niveles.
# Importa desde aquí: from data import access_log, CODE_EXTENSIONS

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

# ============================================================
#  PROBLEMA (igual para todos los niveles):
#
#  1. Filtrar solo los accesos a archivos de código (.py, .sh)
#
#  2. Extraer solo el nombre del archivo (sin la ruta)
#
#  3. Agrupar los archivos por usuario
#
#  4. Generar un reporte ordenado por usuario con este formato:
#     "alice    (4): app.py, utils.py, test_app.py, models.py"
#     "bob      (3): server.py, views.py, helpers.py"
#     "charlie  (2): deploy.sh, main.py"
#
#  RESULTADO ESPERADO (para validar con asserts):
# ============================================================

EXPECTED = [
    "alice    (4): app.py, utils.py, test_app.py, models.py",
    "bob      (3): server.py, views.py, helpers.py",
    "charlie  (2): deploy.sh, main.py",
]
