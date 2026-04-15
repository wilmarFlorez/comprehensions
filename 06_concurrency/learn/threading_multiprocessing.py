# ============================================================
#  THREADING vs MULTIPROCESSING
#  Threading: para I/O bound (archivos, red, DB)
#  Multiprocessing: para CPU bound (cálculos pesados)
# ============================================================
import threading
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# Threading — ejecutar I/O en paralelo
def download(url, delay=1):
    """Simula una descarga."""
    time.sleep(delay)
    return f"descargado: {url}"


urls = [f"https://api.example.com/data/{i}" for i in range(5)]

# Con ThreadPoolExecutor (forma moderna)
print("THREADING (I/O bound):")
start = time.perf_counter()

with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(download, urls))

elapsed = time.perf_counter() - start
print(f"  {len(results)} descargas en {elapsed:.2f}s (vs {len(urls)}s secuencial)")


# CPU bound — multiprocessing
def heavy_calc(n):
    """Cálculo pesado simulado."""
    return sum(i * i for i in range(n))


print("\nMULTIPROCESSING (CPU bound):")
start = time.perf_counter()

with ProcessPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(heavy_calc, [5_000_000] * 4))

elapsed = time.perf_counter() - start
print(f"  4 cálculos en {elapsed:.2f}s")
