# ============================================================
#  functools — herramientas para funciones de orden superior
# ============================================================
from functools import lru_cache, partial, reduce


# partial — fijar argumentos de una función
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(5))  # 25
print(cube(3))    # 27


# lru_cache — memoización automática
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))  # 12586269025 — instantáneo gracias al cache
print(fibonacci.cache_info())


# reduce — acumular valores
nums = [1, 2, 3, 4, 5]

# Producto de todos los números
product = reduce(lambda acc, x: acc * x, nums)
print(f"Producto: {product}")  # 120

# Encontrar el string más largo
words = ["hola", "mundo", "python", "es", "genial"]
longest = reduce(lambda a, b: a if len(a) >= len(b) else b, words)
print(f"Más largo: {longest}")  # python
