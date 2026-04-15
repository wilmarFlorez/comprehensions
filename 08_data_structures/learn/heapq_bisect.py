# ============================================================
#  HEAPQ y BISECT — búsqueda y prioridad eficientes
# ============================================================
import bisect
import heapq

# heapq — min-heap (el menor siempre arriba)
tasks = [(3, "email"), (1, "bug crítico"), (2, "review"), (1, "deploy")]

# Los N más pequeños/grandes
print("Top 2 urgentes:", heapq.nsmallest(2, tasks))
print("Top 2 menos urgentes:", heapq.nlargest(2, tasks))

# Cola de prioridad manual
heap = []
heapq.heappush(heap, (3, "low"))
heapq.heappush(heap, (1, "critical"))
heapq.heappush(heap, (2, "medium"))

while heap:
    priority, task = heapq.heappop(heap)
    print(f"  [{priority}] {task}")


# bisect — inserción ordenada en lista O(log n)
print()
sorted_list = [10, 20, 30, 40, 50]

# ¿Dónde insertar 35 para mantener el orden?
pos = bisect.bisect(sorted_list, 35)
print(f"Insertar 35 en posición {pos}")

# Insertar manteniendo orden
bisect.insort(sorted_list, 35)
print(f"Lista: {sorted_list}")

# Búsqueda binaria: ¿existe el 30?
def binary_search(lst, target):
    i = bisect.bisect_left(lst, target)
    return i < len(lst) and lst[i] == target

print(f"¿30 existe? {binary_search(sorted_list, 30)}")
print(f"¿37 existe? {binary_search(sorted_list, 37)}")
