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

# Paso 1: Sin os.path — usar endswith sobre el string
code_accesses = [(u, p) for u, p, _ in access_log if p.endswith(CODE_EXTENSIONS)]

# Paso 2: rsplit en vez de os.path.basename
named_accesses = [(u, p.rsplit("/", 1)[-1]) for u, p in code_accesses]

# Paso 3: dict.setdefault en vez de defaultdict
grouped = {}
for user, fname in named_accesses:
    grouped.setdefault(user, []).append(fname)

# Paso 4
report = [f"{u:8} ({len(fs)}): {', '.join(fs)}" for u, fs in sorted(grouped.items())]

assert report == EXPECTED
print("✓ Level 4 (sin imports) — COMPLETADO")
for line in report:
    print(f"  {line}")
