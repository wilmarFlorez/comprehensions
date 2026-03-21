import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from data import CODE_EXTENSIONS, EXPECTED, access_log

# Paso 1
code_accesses = []
for user, path, date in access_log:
    if path.endswith(CODE_EXTENSIONS):
        code_accesses.append((user, path, date))

# Paso 2
named_accesses = []
for user, path, date in code_accesses:
    filename = path.rsplit("/", 1)[-1]
    named_accesses.append((user, filename))

# Paso 3
grouped = {}
for user, fname in named_accesses:
    if user not in grouped:
        grouped[user] = []
    grouped[user].append(fname)

# Paso 4
report = []
for user in sorted(grouped):
    files = grouped[user]
    line = f"{user:8} ({len(files)}): {', '.join(files)}"
    report.append(line)

assert report == EXPECTED
print("✓ Level 1 (for loops) — COMPLETADO")
for line in report:
    print(f"  {line}")
