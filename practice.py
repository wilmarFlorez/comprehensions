#!/usr/bin/env python3
"""
Sistema de práctica diaria con repetición espaciada.
Ejecuta: python practice.py

Selecciona ejercicios aleatorios de todos los módulos,
priorizando los que no has practicado recientemente.
"""
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

PROGRESS_FILE = Path(__file__).parent / "progress.json"

MODULES = {
    "01_comprehensions": "Comprehensions y iteración",
    "02_functions": "Funciones, closures, decorators",
    "03_oop": "OOP, dataclasses, dunder methods",
    "04_iterators": "Iteradores, generators, itertools",
    "05_error_handling": "Excepciones y context managers",
    "06_concurrency": "Async, threading, multiprocessing",
    "07_testing": "Pytest, fixtures, mocks",
    "08_data_structures": "Collections, heapq, bisect",
    "09_typing": "Type hints, Protocol, generics",
    "10_patterns": "Design patterns pythónicos",
}


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {"history": {}, "streaks": {"current": 0, "best": 0, "last_date": None}}


def save_progress(progress: dict):
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2, ensure_ascii=False))


def get_stale_modules(progress: dict, top_n: int = 3) -> list[str]:
    """Retorna los módulos menos practicados recientemente."""
    history = progress.get("history", {})
    scored = []
    for mod in MODULES:
        last = history.get(mod, {}).get("last_practiced", "2000-01-01")
        count = history.get(mod, {}).get("times_practiced", 0)
        scored.append((last, count, mod))
    scored.sort()  # más antiguo primero
    return [mod for _, _, mod in scored[:top_n]]


def update_streak(progress: dict):
    today = datetime.now().strftime("%Y-%m-%d")
    streaks = progress["streaks"]
    last = streaks.get("last_date")

    if last == today:
        return  # ya practicó hoy

    yesterday = (datetime.now().replace(hour=0) - __import__("datetime").timedelta(days=1)).strftime("%Y-%m-%d")
    if last == yesterday:
        streaks["current"] += 1
    else:
        streaks["current"] = 1

    streaks["best"] = max(streaks["best"], streaks["current"])
    streaks["last_date"] = today


def show_dashboard(progress: dict):
    streaks = progress["streaks"]
    history = progress.get("history", {})

    print("=" * 55)
    print("  PYTHON MASTERY — Panel de progreso")
    print("=" * 55)
    print(f"  Racha actual: {streaks['current']} días | Mejor: {streaks['best']} días")
    print()

    for mod, desc in MODULES.items():
        info = history.get(mod, {})
        times = info.get("times_practiced", 0)
        last = info.get("last_practiced", "nunca")
        bar = "█" * min(times, 20)
        status = f"{times:>3}x | último: {last}"
        print(f"  {mod:<22} {bar:<20} {status}")

    print()


def _module_paths(module: str) -> tuple[Path, Path]:
    """Retorna (template, working) para un módulo."""
    module_dir = Path(__file__).parent / module
    return module_dir / "practice_template.py", module_dir / "practice.py"


def ensure_working_copy(module: str) -> Path | None:
    """Garantiza que existe el working copy. Lo crea desde el template si falta."""
    template, working = _module_paths(module)
    if working.exists():
        return working
    if not template.exists():
        print(f"  ⚠ {module}/practice_template.py no encontrado")
        return None
    working.write_text(template.read_text())
    print(f"  ✱ Working copy creado: {module}/practice.py (desde template)")
    return working


def reset_module(module: str) -> bool:
    """Sobreescribe el working copy desde el template."""
    template, working = _module_paths(module)
    if not template.exists():
        print(f"  ⚠ {module}/practice_template.py no encontrado")
        return False
    working.write_text(template.read_text())
    print(f"  ✓ Reset: {module}/practice.py")
    return True


def run_module(module: str):
    """Ejecuta el practice.py de un módulo (crea working copy si falta)."""
    practice_file = ensure_working_copy(module)
    if practice_file is None:
        return False

    print(f"\n{'─' * 55}")
    print(f"  {module}: {MODULES.get(module, '')}")
    print(f"{'─' * 55}\n")

    result = subprocess.run(
        [sys.executable, str(practice_file)],
        cwd=str(practice_file.parent),
    )
    return result.returncode == 0


def main():
    progress = load_progress()

    if "--dashboard" in sys.argv:
        show_dashboard(progress)
        return

    if "--reset" in sys.argv:
        idx = sys.argv.index("--reset")
        if idx + 1 >= len(sys.argv):
            print("Uso: python practice.py --reset <módulo|all>")
            return
        target = sys.argv[idx + 1]
        if target == "all":
            for m in MODULES:
                reset_module(m)
        elif target in MODULES:
            reset_module(target)
        else:
            print(f"Módulo '{target}' no existe. Disponibles: {', '.join(MODULES)}, all")
        return

    if "--module" in sys.argv:
        idx = sys.argv.index("--module")
        if idx + 1 < len(sys.argv):
            mod = sys.argv[idx + 1]
            if mod in MODULES:
                run_module(mod)
                today = datetime.now().strftime("%Y-%m-%d")
                history = progress.setdefault("history", {})
                mod_info = history.setdefault(mod, {"times_practiced": 0})
                mod_info["times_practiced"] += 1
                mod_info["last_practiced"] = today
                update_streak(progress)
                save_progress(progress)
            else:
                print(f"Módulo '{mod}' no existe. Disponibles:")
                for m, d in MODULES.items():
                    print(f"  {m}: {d}")
            return

    # Modo interactivo: mostrar dashboard y sugerir
    show_dashboard(progress)
    stale = get_stale_modules(progress)

    print("  Sugeridos para hoy (menos practicados):")
    for i, mod in enumerate(stale, 1):
        print(f"    {i}. {mod}: {MODULES[mod]}")

    print(f"\n  Ejecuta:    python practice.py --module {stale[0]}")
    print(f"  Resetear:   python practice.py --reset {stale[0]}")
    print("  Ver todo:   python practice.py --dashboard")


if __name__ == "__main__":
    main()
