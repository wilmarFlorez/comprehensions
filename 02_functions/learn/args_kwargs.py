# ============================================================
#  *args y **kwargs
#  Permiten crear funciones con número variable de argumentos.
# ============================================================

# *args — tupla de argumentos posicionales
def total(*prices):
    return sum(prices)

print(total(10, 20, 30))         # 60
print(total(5, 15))              # 20


# **kwargs — diccionario de argumentos con nombre
def build_profile(**info):
    return {k: v for k, v in info.items()}

print(build_profile(name="Alice", role="dev", level="senior"))


# Combinados: obligatorio + *args + **kwargs
def log(level, *messages, **meta):
    prefix = f"[{level.upper()}]"
    body = " ".join(messages)
    extras = " | ".join(f"{k}={v}" for k, v in meta.items())
    print(f"{prefix} {body}" + (f" ({extras})" if extras else ""))

log("info", "Servidor", "iniciado", port=8080, host="localhost")
# [INFO] Servidor iniciado (port=8080 | host=localhost)


# Desempaquetar con * y **
def greet(name, age, city):
    print(f"{name}, {age} años, de {city}")

data = ("Alice", 30, "Bogotá")
greet(*data)

data_dict = {"name": "Bob", "age": 25, "city": "Lima"}
greet(**data_dict)
