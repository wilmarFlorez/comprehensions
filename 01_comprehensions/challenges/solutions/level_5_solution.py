from functools import reduce

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from data import CODE_EXTENSIONS, EXPECTED, access_log

# Paso 1: filter
code_accesses = list(filter(lambda x: x[1].endswith(CODE_EXTENSIONS), access_log))

# Paso 2: map
named_accesses = list(map(lambda x: (x[0], x[1].rsplit("/", 1)[-1]), code_accesses))

# Paso 3: reduce para agrupar
grouped = reduce(
    lambda acc, item: {**acc, item[0]: acc.get(item[0], []) + [item[1]]},
    named_accesses,
    {},
)

# Paso 4: map para formatear
report = list(
    map(
        lambda item: f"{item[0]:8} ({len(item[1])}): {', '.join(item[1])}",
        sorted(grouped.items()),
    )
)

assert report == EXPECTED
print("✓ Level 5 (funcional) — COMPLETADO")
for line in report:
    print(f"  {line}")
