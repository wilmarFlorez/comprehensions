# ============================================================
#  PRÁCTICA — DATA STRUCTURES
#  Escribe tu solución donde dice ... y ejecuta el archivo.
# ============================================================

passed = 0
total = 10


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


# Ejercicio 1: Counter — top 3
# Encuentra las 3 letras más frecuentes en el texto.

text = "abracadabra"

ejercicio(1, "Counter top 3",
    lambda: ...,  # Counter(...).most_common(3)
    [("a", 5), ("b", 2), ("r", 2)],
)


# Ejercicio 2: Counter — operaciones
# ¿Cuántas letras tienen en común "hello" y "world"?

ejercicio(2, "Counter intersección",
    lambda: ...,  # (Counter("hello") & Counter("world")).total() o sum
    2,  # 'l' y 'o'
)


# Ejercicio 3: deque — últimos N
# Simula un historial que guarda solo los últimos 3 comandos.
# Agrega: "ls", "cd", "mkdir", "rm", "cat"

ejercicio(3, "deque últimos 3",
    lambda: ...,  # usa deque(maxlen=3)
    ["mkdir", "rm", "cat"],
)


# Ejercicio 4: deque — rotar
# Rota [1, 2, 3, 4, 5] una posición a la derecha.

ejercicio(4, "deque rotate",
    lambda: ...,
    [5, 1, 2, 3, 4],
)


# Ejercicio 5: defaultdict — agrupar
# Agrupa estas palabras por su longitud.
words_5 = ["hi", "hey", "ok", "bye", "no", "yes"]

ejercicio(5, "defaultdict agrupar",
    lambda: ...,  # {2: ["hi", "ok", "no"], 3: ["hey", "bye", "yes"]}
    {2: ["hi", "ok", "no"], 3: ["hey", "bye", "yes"]},
)


# Ejercicio 6: heapq — top N
# Encuentra los 3 números más grandes de la lista.

nums_6 = [42, 17, 93, 8, 55, 71, 3, 88]

ejercicio(6, "heapq top 3",
    lambda: ...,  # heapq.nlargest(...)
    [93, 88, 71],
)


# Ejercicio 7: heapq — merge
# Combina dos listas ordenadas en una sola lista ordenada.

a7 = [1, 4, 7, 10]
b7 = [2, 5, 6, 9]

ejercicio(7, "heapq merge",
    lambda: ...,  # list(heapq.merge(...))
    [1, 2, 4, 5, 6, 7, 9, 10],
)


# Ejercicio 8: bisect — insertar ordenado
# Inserta 35 en [10, 20, 30, 40, 50] y retorna la lista resultante.

ejercicio(8, "bisect insort",
    lambda: ...,
    [10, 20, 30, 35, 40, 50],
)


# Ejercicio 9: namedtuple
# Crea un namedtuple Color(r, g, b) y retorna la suma de sus componentes.

ejercicio(9, "namedtuple Color",
    lambda: ...,  # Color(255, 128, 0) -> sum
    383,
)


# Ejercicio 10: Combinado
# Dado un log de errores, retorna el error más frecuente y cuántas veces apareció.

errors = ["timeout", "404", "timeout", "500", "404", "timeout", "404", "timeout"]

ejercicio(10, "error más frecuente",
    lambda: ...,  # ("timeout", 4)
    ("timeout", 4),
)


# ============================================================
print(f"\n{'=' * 50}")
print(f"  RESULTADO: {passed}/{total} ejercicios correctos")
print(f"{'=' * 50}")
if passed == total:
    print("  ¡Perfecto! Todos los ejercicios completados.")
else:
    print(f"  Te faltan {total - passed} ejercicios. ¡Sigue intentando!")
