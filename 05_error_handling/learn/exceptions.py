# ============================================================
#  EXCEPCIONES — try/except/else/finally y excepciones custom
# ============================================================


# try/except/else/finally — flujo completo
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  ⚠ División por cero")
        return None
    except TypeError as e:
        print(f"  ⚠ Tipo inválido: {e}")
        return None
    else:
        # Solo se ejecuta si NO hubo excepción
        print(f"  ✓ {a}/{b} = {result}")
        return result
    finally:
        # SIEMPRE se ejecuta (limpieza)
        print("  → Operación terminada")


safe_divide(10, 3)
safe_divide(10, 0)
safe_divide("a", 2)


# Excepciones personalizadas
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")


def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("age", "debe ser un entero")
    if age < 0 or age > 150:
        raise ValidationError("age", f"valor fuera de rango: {age}")
    return age


# Capturar la excepción custom
print()
for value in [25, -5, "abc", 200]:
    try:
        validate_age(value)
        print(f"  ✓ {value} es válido")
    except ValidationError as e:
        print(f"  ✗ {e}")


# Encadenar excepciones con `raise from`
def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError(f"No se pudo cargar config: {path}") from e


print()
try:
    load_config("/no/existe.toml")
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Causa: {e.__cause__}")
