# ============================================================
#  CONTEXT MANAGERS — with statement y __enter__/__exit__
# ============================================================


# Context manager con clase
class Timer:
    """Mide el tiempo de ejecución de un bloque."""

    def __enter__(self):
        import time
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self._start
        print(f"Tiempo: {self.elapsed:.4f}s")
        return False  # No suprimir excepciones

with Timer():
    total = sum(range(1_000_000))
    print(f"Total: {total}")


# Context manager con contextlib
from contextlib import contextmanager


@contextmanager
def temporary_value(obj, attr, new_value):
    """Cambia un atributo temporalmente y lo restaura al salir."""
    old_value = getattr(obj, attr)
    setattr(obj, attr, new_value)
    try:
        yield old_value
    finally:
        setattr(obj, attr, old_value)


class Config:
    debug = False

print(f"\nAntes: debug={Config.debug}")
with temporary_value(Config, "debug", True) as old:
    print(f"Dentro: debug={Config.debug} (era {old})")
print(f"Después: debug={Config.debug}")
