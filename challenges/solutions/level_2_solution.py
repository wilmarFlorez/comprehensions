import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from data import CODE_EXTENSIONS, EXPECTED, access_log

# Paso 1
code_accesses = [(u, p, d) for u, p, d in access_log if p.endswith(CODE_EXTENSIONS)]

# Paso 2
named_accesses = [(u, p.rsplit("/", 1)[-1]) for u, p, _ in code_accesses]

# Paso 3
grouped = {}
for user, fname in named_accesses:
    grouped.setdefault(user, []).append(fname)

# Paso 4
report = [f"{u:8} ({len(fs)}): {', '.join(fs)}" for u, fs in sorted(grouped.items())]

assert report == EXPECTED
print("✓ Level 2 (comprehensions) — COMPLETADO")
for line in report:
    print(f"  {line}")
