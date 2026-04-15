# ============================================================
#  DECORATORS
#  Un decorator envuelve una función para agregar comportamiento
#  sin modificar la función original.
# ============================================================
import time
from functools import wraps


# Decorator básico: medir tiempo de ejecución
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} tardó {elapsed:.4f}s")
        return result
    return wrapper


@timer
def slow_sum(n):
    return sum(range(n))


print(slow_sum(1_000_000))


# Decorator con argumentos
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hola, {name}!")


greet("Wilmar")
