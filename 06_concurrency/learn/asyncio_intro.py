# ============================================================
#  ASYNCIO — concurrencia con async/await
# ============================================================
import asyncio


async def fetch_data(name, delay):
    """Simula una llamada a API con delay."""
    print(f"  ⏳ {name}: iniciando...")
    await asyncio.sleep(delay)
    print(f"  ✓ {name}: completado ({delay}s)")
    return {"source": name, "data": f"resultado de {name}"}


async def main():
    # Secuencial — 3 segundos total
    print("SECUENCIAL:")
    r1 = await fetch_data("API-1", 1)
    r2 = await fetch_data("API-2", 1)
    r3 = await fetch_data("API-3", 1)

    # Concurrente — 1 segundo total (todas en paralelo)
    print("\nCONCURRENTE:")
    results = await asyncio.gather(
        fetch_data("API-A", 1),
        fetch_data("API-B", 1),
        fetch_data("API-C", 1),
    )
    print(f"  Resultados: {[r['source'] for r in results]}")


asyncio.run(main())
