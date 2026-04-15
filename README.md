# Python Mastery — De cero a master

Práctica progresiva de Python con repetición espaciada. 10 módulos, cada uno con ejemplos y ejercicios con auto-verificación.

## Inicio rápido

```bash
# Ver panel de progreso y sugerencias
python practice.py

# Practicar un módulo específico
python practice.py --module 01_comprehensions

# O directamente
python 02_functions/practice.py
```

## Estructura

```
├── practice.py              # Panel de progreso + repetición espaciada
├── progress.json             # Tracking automático (se genera solo)
│
├── 01_comprehensions/        # List/dict/set comprehensions, generators
│   ├── learn/                # Ejemplos explicados por tema
│   ├── challenges/           # 5 niveles del mismo problema
│   └── practice.py           # 10 ejercicios con asserts
│
├── 02_functions/             # Closures, decorators, *args/**kwargs, functools
│   ├── learn/
│   └── practice.py
│
├── 03_oop/                   # Classes, dataclasses, dunder methods
│   ├── learn/
│   └── practice.py
│
├── 04_iterators/             # itertools, generators, yield, __iter__
│   ├── learn/
│   └── practice.py
│
├── 05_error_handling/        # try/except/else/finally, context managers
│   ├── learn/
│   └── practice.py
│
├── 06_concurrency/           # asyncio, threading, multiprocessing
│   ├── learn/
│   └── practice.py
│
├── 07_testing/               # pytest, fixtures, mocks, parametrize
│   ├── learn/
│   └── practice.py           # Implementa funciones para que tests pasen
│
├── 08_data_structures/       # Counter, deque, heapq, bisect, namedtuple
│   ├── learn/
│   └── practice.py
│
├── 09_typing/                # Type hints, Protocol, generics, TypedDict
│   ├── learn/
│   └── practice.py
│
└── 10_patterns/              # Strategy, Observer, Factory, Registry, Builder
    ├── learn/
    └── practice.py
```

## Cómo funciona

### Cada módulo tiene:

- **`learn/`** — Archivos ejecutables con ejemplos explicados. Léelos, ejecútalos, modifícalos.
- **`practice.py`** — Ejercicios con auto-verificación. Reemplaza `...` con tu solución:

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

Usa `pytest` en lugar de asserts manuales:

```bash
pip install pytest
python -m pytest 07_testing/practice.py -v
```

## Requisitos

- Python 3.12+
- pytest (opcional, para módulo 07)