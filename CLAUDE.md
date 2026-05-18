# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A Spanish-language, self-paced Python learning project. 10 numbered modules (`01_comprehensions` through `10_patterns`) covering core Python topics, plus a root-level dashboard with spaced-repetition tracking. No application code, no external dependencies — pure Python 3.12+ exercises. Comments, exercise descriptions, and dashboard output are in Spanish; preserve that when editing.

## Commands

```bash
# Show progress dashboard + suggested modules for today
python practice.py

# Run a specific module's exercises (auto-creates practice.py from template if missing)
python practice.py --module 02_functions

# Reset the working copy back to the blank template
python practice.py --reset 02_functions
python practice.py --reset all

# Module 07 is the only one that uses pytest. Generate the working copy first:
python practice.py --module 07_testing   # creates 07_testing/practice.py
python -m pytest 07_testing/practice.py -v

# Run a single test:
python -m pytest 07_testing/practice.py::TestFizzBuzz::test_fizz -v
```

## Architecture

### Module shape (applies to 02–10)

Every numbered module follows the same layout:
- `learn/` — runnable example files, one topic per file. Read, execute, modify.
- `practice_template.py` — **canonical** exercises file, tracked in git, always with `...` placeholders. Treat as read-only source of truth.
- `practice.py` — **working copy**, gitignored. Auto-created on first `--module` run by copying the template. The learner edits this file to solve exercises.

Critical: when editing exercises, modify `practice_template.py`, never `practice.py`. The pattern `[0-9][0-9]_*/practice.py` is in `.gitignore`.

Module `01_comprehensions` is richer: it has `learn/`-equivalent subdirs by topic (`basics/`, `conditionals/`, `dictionaries/`, `lists/`, `sets/`) plus a `challenges/` directory with 5 difficulty levels (`level_1_for_loops.py` → `level_5_functional.py`) solving the same problem progressively.

Module `07_testing` is the only one that uses `pytest` and inverts the exercise pattern: instead of asserts checking solutions, the learner implements stub functions/classes to make a fixed pytest suite pass. Don't modify the `--- TESTS (NO MODIFICAR) ---` blocks.

### Exercise verification pattern (modules other than 07)

`practice_template.py` files define a helper like `ejercicio(num, descripcion, solucion, esperado)` that:
- Runs `solucion()` (a lambda the learner fills in).
- If it returns `...` (the sentinel `Ellipsis`), the exercise is reported as **pendiente**.
- Otherwise compares against `esperado` and prints ✓ / ✗.
- Catches `AssertionError` separately from other exceptions so a broken exercise doesn't halt the rest.

When adding exercises, keep this contract: leave `lambda: ...` as the placeholder so untouched exercises show as pending rather than failing.

### Root dashboard and progress tracking

`practice.py` at the root is the entry point users typically run. It:
- Reads/writes `progress.json` (gitignored — it's personal tracking, never commit it).
- Tracks `times_practiced` and `last_practiced` per module, plus a daily streak.
- `get_stale_modules()` sorts modules by `(last_practiced, times_practiced)` ascending and suggests the 3 oldest — this is the spaced-repetition heuristic.
- `--module <name>` calls `ensure_working_copy()` (creates `<module>/practice.py` from the template if missing) then runs it as a subprocess, then bumps counters.
- `--reset <name|all>` overwrites the working copy from the template without running it.

`main.py` is just a thin wrapper that re-execs `practice.py`.

The canonical module list lives in the `MODULES` dict in `practice.py`. Adding a new module means adding it there *and* creating `<module>/practice_template.py`.
