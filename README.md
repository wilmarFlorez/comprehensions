# Python Mastery — De cero a master

Práctica progresiva de Python con repetición espaciada. 10 módulos, cada uno con ejemplos y ejercicios con auto-verificación.

## Inicio rápido

```bash
# Ver panel de progreso y sugerencias
python practice.py

# Practicar un módulo específico (crea practice.py desde el template si no existe)
python practice.py --module 01_comprehensions

# Resetear un módulo (vuelve a dejarlo en blanco con ...)
python practice.py --reset 01_comprehensions

# Resetear todos
python practice.py --reset all

# O ejecutar directamente
python 02_functions/practice.py
```

### Templates vs working copies

Cada módulo tiene dos archivos:

- **`practice_template.py`** — versionado en git. Siempre con `...` como placeholders. Es la "fuente canónica" del ejercicio.
- **`practice.py`** — tu copia de trabajo. **No versionada** (gitignored). Aquí escribís tus soluciones. Se genera automáticamente desde el template la primera vez, y `--reset` la sobreescribe.

Esto hace real la repetición espaciada: cuando volvés a un módulo después de días, `--reset` te devuelve la pizarra en blanco.

## Estructura

```
├── practice.py              # Panel de progreso + repetición espaciada
├── progress.json             # Tracking automático (se genera solo)
│
├── 01_comprehensions/        # List/dict/set comprehensions, generators
│   ├── learn/                # Ejemplos explicados por tema
│   ├── challenges/           # 5 niveles del mismo problema
│   ├── practice_template.py  # Versión canónica con ...
│   └── practice.py           # Tu copia de trabajo (gitignored)
│
├── 02_functions/             # Closures, decorators, *args/**kwargs, functools
│   ├── learn/
│   └── practice_template.py
│
├── 03_oop/                   # Classes, dataclasses, dunder methods
│   ├── learn/
│   └── practice_template.py
│
├── 04_iterators/             # itertools, generators, yield, __iter__
│   ├── learn/
│   └── practice_template.py
│
├── 05_error_handling/        # try/except/else/finally, context managers
│   ├── learn/
│   └── practice_template.py
│
├── 06_concurrency/           # asyncio, threading, multiprocessing
│   ├── learn/
│   └── practice_template.py
│
├── 07_testing/               # pytest, fixtures, mocks, parametrize
│   ├── learn/
│   └── practice_template.py  # Implementa funciones para que tests pasen
│
├── 08_data_structures/       # Counter, deque, heapq, bisect, namedtuple
│   ├── learn/
│   └── practice_template.py
│
├── 09_typing/                # Type hints, Protocol, generics, TypedDict
│   ├── learn/
│   └── practice_template.py
│
└── 10_patterns/              # Strategy, Observer, Factory, Registry, Builder
    ├── learn/
    └── practice_template.py
```

## Cómo funciona

### Cada módulo tiene:

- **`learn/`** — Archivos ejecutables con ejemplos explicados. Léelos, ejecútalos, modifícalos.
- **`practice_template.py`** — Plantilla canónica de los ejercicios. **No la edites directamente**.
- **`practice.py`** — Copia de trabajo generada desde el template. Reemplaza `...` con tu solución:

```
✓ Ejercicio 1: closure make_adder — OK
✗ Ejercicio 2: *args filtrar pares — FALLÓ: (1, 3, 5)
- Ejercicio 3: **kwargs query string — pendiente
```

### Repetición espaciada

El `practice.py` raíz trackea cuándo practicaste cada módulo y te sugiere repasar los que llevan más tiempo sin tocar:

```bash
python practice.py
```

```
  PYTHON MASTERY — Panel de progreso
  Racha actual: 3 días | Mejor: 7 días

  01_comprehensions        ████████             8x | último: 2026-04-14
  02_functions             ███                  3x | último: 2026-04-10
  03_oop                                        0x | último: nunca
  ...

  Sugeridos para hoy:
    1. 03_oop: OOP, dataclasses, dunder methods
    2. 06_concurrency: Async, threading, multiprocessing
```

## Módulo 07 (testing) es especial

Usa `pytest` en lugar de asserts manuales. Primero genera la copia de trabajo, luego ejecutá pytest sobre ella:

```bash
pip install pytest
python practice.py --module 07_testing   # crea 07_testing/practice.py si falta
python -m pytest 07_testing/practice.py -v
```

## Requisitos

- Python 3.12+
- pytest (opcional, para módulo 07)