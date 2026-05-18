# ============================================================
#  PRÁCTICA — CONCURRENCIA
#  Escribe tu solución donde dice ... y ejecuta el archivo.
# ============================================================
import asyncio

passed = 0
total = 8


def ejercicio(num, descripcion, solucion, esperado):
    global passed
    try:
        resultado = solucion()
        if resultado is ...:
            print(f"- Ejercicio {num}: {descripcion} — pendiente")
            return
        assert resultado == esperado, f"{resultado}"
        passed += 1
        print(f"✓ Ejercicio {num}: {descripcion} — OK")
    except AssertionError as e:
        print(f"✗ Ejercicio {num}: {descripcion} — FALLÓ: {e}")
    except Exception:
        print(f"- Ejercicio {num}: {descripcion} — pendiente")


# Ejercicio 1: async/await básico
# Crea una función async que retorne "hola" después de 0 segundos.

async def say_hello():
    ...  # tu solución aquí

ejercicio(1, "async básico",
    lambda: asyncio.run(say_hello()),
    "hola",
)


# Ejercicio 2: asyncio.gather
# Ejecuta 3 coroutines en paralelo y retorna sus resultados.

async def double(n):
    return n * 2

async def run_all():
    ...  # usa asyncio.gather para ejecutar double(1), double(2), double(3)

ejercicio(2, "asyncio.gather",
    lambda: asyncio.run(run_all()),
    [2, 4, 6],
)


# Ejercicio 3: ThreadPoolExecutor
# Usa ThreadPoolExecutor para aplicar str.upper a una lista de palabras.

words = ["hola", "mundo", "python"]

ejercicio(3, "ThreadPoolExecutor",
    lambda: ...,  # usa pool.map(str.upper, words)
    ["HOLA", "MUNDO", "PYTHON"],
)


# Ejercicio 4: async generator
# Crea un async generator que yield números del 0 al n-1.

async def arange(n):
    ...  # yield con async

async def collect_arange():
    return [i async for i in arange(5)]

ejercicio(4, "async generator",
    lambda: asyncio.run(collect_arange()),
    [0, 1, 2, 3, 4],
)


# Ejercicio 5: asyncio.create_task
# Crea dos tasks que corran en paralelo.
# Ambas duermen 0s y retornan su argumento multiplicado.

async def multiply_task(n, factor):
    return n * factor

async def run_tasks():
    ...  # crea tasks con asyncio.create_task y espera ambas

ejercicio(5, "create_task",
    lambda: asyncio.run(run_tasks()),
    (10, 30),
)


# Ejercicio 6: asyncio.wait_for con timeout
# Crea una coroutine que maneje timeout.

async def slow_operation():
    await asyncio.sleep(10)
    return "completado"

async def with_timeout():
    ...  # usa asyncio.wait_for con timeout=0.1, retorna "timeout" si falla

ejercicio(6, "wait_for timeout",
    lambda: asyncio.run(with_timeout()),
    "timeout",
)


# Ejercicio 7: Semáforo — limitar concurrencia
# Simula que solo 2 "descargas" pueden correr a la vez.

async def limited_downloads():
    sem = asyncio.Semaphore(2)
    max_concurrent = 0
    current = 0

    async def download(i):
        nonlocal current, max_concurrent
        async with sem:
            current += 1
            max_concurrent = max(max_concurrent, current)
            await asyncio.sleep(0)
            current -= 1
            return i

    results = await asyncio.gather(*[download(i) for i in range(5)])
    return (sorted(results), max_concurrent <= 2)

ejercicio(7, "semáforo",
    lambda: asyncio.run(limited_downloads()),
    ([0, 1, 2, 3, 4], True),
)


# Ejercicio 8: asyncio.Queue
# Crea un productor que ponga 3 items y un consumidor que los lea.

async def producer_consumer():
    ...  # usa asyncio.Queue

ejercicio(8, "asyncio.Queue",
    lambda: ...,
    "pendiente — implementa producer/consumer",
)


# ============================================================
print(f"\n{'=' * 50}")
print(f"  RESULTADO: {passed}/{total} ejercicios correctos")
print(f"{'=' * 50}")
if passed == total:
    print("  ¡Perfecto! Todos los ejercicios completados.")
else:
    print(f"  Te faltan {total - passed} ejercicios. ¡Sigue intentando!")
