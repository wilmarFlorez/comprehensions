# ============================================================
#  PRÁCTICA — ERROR HANDLING Y CONTEXT MANAGERS
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


# Ejercicio 1: try/except básico
# Crea safe_int(value) que convierta a int. Si falla retorna None.

def safe_int(value):
    ...  # tu solución aquí

ejercicio(1, "safe_int",
    lambda: (safe_int("42"), safe_int("abc"), safe_int(3.7)),
    (42, None, 3),
)


# Ejercicio 2: try/except/else
# Crea divide(a, b) que retorne el resultado o "error" si b es 0.
# Usa else para retornar el resultado (no lo pongas en el try).

def divide(a, b):
    ...  # tu solución aquí

ejercicio(2, "divide con else",
    lambda: (divide(10, 3), divide(10, 0)),
    (10 / 3, "error"),
)


# Ejercicio 3: finally
# Crea process(value) que: intente convertir a int,
# retorne ("ok", int_value) o ("fail", None),
# pero SIEMPRE imprima "done" (usa finally).
# Para el test, solo validamos el retorno.

def process(value):
    ...  # tu solución aquí

ejercicio(3, "finally",
    lambda: (process("5"), process("x")),
    (("ok", 5), ("fail", None)),
)


# Ejercicio 4: Excepción personalizada
# Crea NegativeError(ValueError) que reciba un número.
# Crea abs_only(n) que lance NegativeError si n < 0, sino retorne n.

# class NegativeError(ValueError): ...

def abs_only(n):
    ...  # tu solución aquí

ejercicio(4, "excepción custom",
    lambda: ...,  # (abs_only(5), type(error_capturado).__name__)
    (5, "NegativeError"),
)


# Ejercicio 5: Múltiples except
# Crea get_item(lst, index) que retorne:
# el elemento si existe, "index_error" si IndexError, "type_error" si TypeError.

def get_item(lst, index):
    ...  # tu solución aquí

ejercicio(5, "múltiples except",
    lambda: (get_item([1, 2, 3], 1), get_item([1, 2], 5), get_item([1, 2], "a")),
    (2, "index_error", "type_error"),
)


# Ejercicio 6: Context manager con clase
# Crea Indenter que mantenga un nivel de indentación.
# Cada `with Indenter()` aumenta un nivel.
# indent.print("hola") imprime "    hola" (4 espacios por nivel).

# class Indenter: ...  # __enter__, __exit__, print()

ejercicio(6, "context manager clase",
    lambda: ...,  # captura el output indentado
    "pendiente — implementa Indenter",
)


# Ejercicio 7: contextmanager decorator
# Crea un context manager `suppress(*exceptions)` que suprima
# las excepciones indicadas (como contextlib.suppress pero manual).
from contextlib import contextmanager

# @contextmanager
# def suppress(*exceptions): ...

ejercicio(7, "suppress context manager",
    lambda: ...,
    "pendiente — implementa suppress",
)


# Ejercicio 8: raise from
# Crea load_json(text) que intente parsear JSON.
# Si falla, lance ValueError("JSON inválido") FROM la excepción original.
import json

def load_json(text):
    ...  # tu solución aquí

ejercicio(8, "raise from",
    lambda: ...,  # (load_json('{"a": 1}'), type_del_error_capturado)
    ({"a": 1}, "ValueError"),
)


# Ejercicio 9: Validador con excepciones
# Crea validate_email(email) que retorne el email si es válido.
# Debe tener "@" y al menos un "." después del "@".
# Si no, lanza ValueError con mensaje descriptivo.

def validate_email(email):
    ...  # tu solución aquí

ejercicio(9, "validate_email",
    lambda: ...,  # (validate_email("a@b.com"), error_para_invalido)
    ("a@b.com", "ValueError"),
)


# Ejercicio 10: ExceptionGroup (Python 3.11+)
# Crea validate_all(data: dict) que valide múltiples campos.
# Recolecta TODOS los errores y lánzalos juntos con ExceptionGroup.

def validate_all(data):
    ...  # tu solución aquí

ejercicio(10, "ExceptionGroup",
    lambda: ...,
    "pendiente — implementa validate_all",
)


# ============================================================
print(f"\n{'=' * 50}")
print(f"  RESULTADO: {passed}/{total} ejercicios correctos")
print(f"{'=' * 50}")
if passed == total:
    print("  ¡Perfecto! Todos los ejercicios completados.")
else:
    print(f"  Te faltan {total - passed} ejercicios. ¡Sigue intentando!")
