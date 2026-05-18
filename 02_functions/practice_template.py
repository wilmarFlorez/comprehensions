# ============================================================
#  PRÁCTICA — FUNCIONES
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


# Ejercicio 1: Closure básico
# Crea make_adder(n) que retorne una función que sume n a su argumento.
# make_adder(10)(5) -> 15

def make_adder(n):
    ...  # tu solución aquí

ejercicio(1, "closure make_adder",
    lambda: (make_adder(10)(5), make_adder(3)(7)),
    (15, 10),
)


# Ejercicio 2: *args
# Crea una función que reciba cualquier cantidad de números
# y retorne solo los pares.

def only_evens(*nums):
    ...  # tu solución aquí

ejercicio(2, "*args filtrar pares",
    lambda: only_evens(1, 2, 3, 4, 5, 6),
    (2, 4, 6),
)


# Ejercicio 3: **kwargs → string
# Crea build_query(**params) que genere un query string:
# build_query(name="alice", age=30) -> "name=alice&age=30"

def build_query(**params):
    ...  # tu solución aquí

ejercicio(3, "**kwargs query string",
    lambda: build_query(name="alice", age=30, city="bogota"),
    "name=alice&age=30&city=bogota",
)


# Ejercicio 4: Decorator simple
# Crea un decorator `shout` que convierta el resultado string a MAYÚSCULAS.

def shout(func):
    ...  # tu solución aquí

# NO borres esta función — aplica tu decorator aquí
# @shout
def whisper():
    return "hola mundo"

ejercicio(4, "decorator shout",
    lambda: whisper(),
    "HOLA MUNDO",
)


# Ejercicio 5: Función que retorna función
# Crea make_validator(min_len) que retorne una función
# que valide si un string tiene al menos min_len caracteres.

def make_validator(min_len):
    ...  # tu solución aquí

ejercicio(5, "validator con closure",
    lambda: (make_validator(3)("ab"), make_validator(3)("abc"), make_validator(5)("hola")),
    (False, True, False),
)


# Ejercicio 6: partial
# Usa functools.partial para crear `double` a partir de una función multiply(a, b).

def multiply(a, b):
    return a * b

double = ...  # usa partial aquí

ejercicio(6, "partial double",
    lambda: (double(5), double(12)),
    (10, 24),
)


# Ejercicio 7: Decorator con argumento
# Crea `prefix(tag)` que agregue un prefijo al resultado de la función.
# @prefix("LOG")
# def msg(): return "inicio"
# msg() -> "LOG: inicio"

def prefix(tag):
    ...  # tu solución aquí

# @prefix("LOG")
def msg():
    return "inicio"

ejercicio(7, "decorator con argumento",
    lambda: msg(),
    "LOG: inicio",
)


# Ejercicio 8: Composición
# Crea compose(f, g) que retorne una función h(x) = f(g(x)).

def compose(f, g):
    ...  # tu solución aquí

ejercicio(8, "composición de funciones",
    lambda: compose(str.upper, str.strip)("  hola  "),
    "HOLA",
)


# Ejercicio 9: Memoización manual
# Crea una función memoize(func) que cachee resultados.
# No uses functools.lru_cache.

def memoize(func):
    ...  # tu solución aquí

call_count = 0

# @memoize
def expensive(n):
    global call_count
    call_count += 1
    return n * n

ejercicio(9, "memoize manual",
    lambda: (expensive(5), expensive(5), expensive(3), call_count),
    (25, 25, 9, 2),  # call_count debe ser 2 (no 3) gracias al cache
)


# Ejercicio 10: Pipeline
# Crea pipeline(*funcs) que encadene funciones de izquierda a derecha.
# pipeline(f, g, h)(x) == h(g(f(x)))

def pipeline(*funcs):
    ...  # tu solución aquí

ejercicio(10, "pipeline de funciones",
    lambda: pipeline(str.strip, str.lower, str.title)("  HOLA MUNDO  "),
    "Hola Mundo",
)


# ============================================================
print(f"\n{'=' * 50}")
print(f"  RESULTADO: {passed}/{total} ejercicios correctos")
print(f"{'=' * 50}")
if passed == total:
    print("  ¡Perfecto! Todos los ejercicios completados.")
else:
    print(f"  Te faltan {total - passed} ejercicios. ¡Sigue intentando!")
