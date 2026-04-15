# ============================================================
#  PRÁCTICA — DESIGN PATTERNS
#  Escribe tu solución donde dice ... y ejecuta el archivo.
# ============================================================

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


# Ejercicio 1: Strategy — funciones como estrategia
# Crea 3 funciones de ordenamiento:
# sort_asc(lst), sort_desc(lst), sort_by_len(lst)
# Y una función apply_sort(lst, strategy) que aplique la estrategia.

ejercicio(1, "strategy con funciones",
    lambda: ...,  # apply_sort(["banana", "pie", "manzana"], sort_by_len)
    ["pie", "banana", "manzana"],
)


# Ejercicio 2: Observer — EventEmitter básico
# Crea una clase EventEmitter con on(event, callback) y emit(event, *args).
# emitter.on("greet", lambda name: ...) -> emitter.emit("greet", "Alice")

ejercicio(2, "observer EventEmitter",
    lambda: ...,
    "pendiente — implementa EventEmitter",
)


# Ejercicio 3: Factory — crear objetos por tipo
# Crea make_shape(type, **kwargs) que retorne dicts:
# make_shape("circle", radius=5) -> {"type": "circle", "radius": 5, "area": 78.54}
# make_shape("rect", w=4, h=3) -> {"type": "rect", "w": 4, "h": 3, "area": 12}
import math

def make_shape(shape_type, **kwargs):
    ...  # tu solución aquí

ejercicio(3, "factory make_shape",
    lambda: ...,  # (make_shape("circle", radius=5)["area"], make_shape("rect", w=4, h=3)["area"])
    (round(math.pi * 25, 2), 12),
)


# Ejercicio 4: Registry — decorator para registrar
# Crea un decorator @command(name) que registre funciones en un dict.

commands = {}

def command(name):
    ...  # tu solución aquí

# @command("hello")
# def hello_cmd(user): return f"Hello, {user}!"
# @command("bye")
# def bye_cmd(user): return f"Bye, {user}!"

ejercicio(4, "registry con decorator",
    lambda: ...,  # commands["hello"]("Alice")
    "Hello, Alice!",
)


# Ejercicio 5: Pipeline / Chain
# Crea una clase Pipeline donde puedas encadenar .pipe(func).
# Pipeline("HELLO WORLD").pipe(str.lower).pipe(str.title).result -> "Hello World"

# class Pipeline: ...

ejercicio(5, "pipeline chain",
    lambda: ...,  # Pipeline("hello world").pipe(str.upper).pipe(str.split).result
    ["HELLO", "WORLD"],
)


# Ejercicio 6: Singleton con decorator
# Crea un decorator @singleton que asegure que solo existe una instancia.

def singleton(cls):
    ...  # tu solución aquí

# @singleton
# class Database:
#     def __init__(self): self.connected = True

ejercicio(6, "singleton decorator",
    lambda: ...,  # Database() is Database()
    True,
)


# Ejercicio 7: Builder pattern
# Crea QueryBuilder con .select(), .where(), .limit() y .build().
# QueryBuilder().select("name").where("age > 18").limit(10).build()
# -> "SELECT name WHERE age > 18 LIMIT 10"

# class QueryBuilder: ...

ejercicio(7, "builder pattern",
    lambda: ...,
    "SELECT name WHERE age > 18 LIMIT 10",
)


# Ejercicio 8: Decorator pattern (no confundir con Python decorators)
# Crea funciones que envuelvan un mensaje:
# bold("hi") -> "<b>hi</b>"
# italic("hi") -> "<i>hi</i>"
# Combina: bold(italic("hi")) -> "<b><i>hi</i></b>"

def bold(text):
    ...

def italic(text):
    ...

ejercicio(8, "decorator pattern",
    lambda: ...,  # bold(italic("hola"))
    "<b><i>hola</i></b>",
)


# ============================================================
print(f"\n{'=' * 50}")
print(f"  RESULTADO: {passed}/{total} ejercicios correctos")
print(f"{'=' * 50}")
if passed == total:
    print("  ¡Perfecto! Todos los ejercicios completados.")
else:
    print(f"  Te faltan {total - passed} ejercicios. ¡Sigue intentando!")
