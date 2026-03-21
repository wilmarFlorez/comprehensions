import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from data import CODE_EXTENSIONS, EXPECTED, access_log

# Pasos 1+2 combinados
named_code = [
    (u, p.rsplit("/", 1)[-1]) for u, p, _ in access_log if p.endswith(CODE_EXTENSIONS)
]

# Paso 3: agrupar con dict comp + list comp anidado
grouped = {
    u: [f for usr, f in named_code if usr == u]
    for u in dict.fromkeys(u for u, _ in named_code)
}

# Paso 4
report = [f"{u:8} ({len(fs)}): {', '.join(fs)}" for u, fs in sorted(grouped.items())]

assert report == EXPECTED
print("✓ Level 3 (one-liners) — COMPLETADO")
for line in report:
    print(f"  {line}")
