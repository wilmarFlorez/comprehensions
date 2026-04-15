# ============================================================
#  CLOSURES
#  Una función interna que "recuerda" las variables del scope externo
#  incluso después de que la función externa termina.
# ============================================================

def make_multiplier(factor):
    """Retorna una función que multiplica por `factor`."""
    def multiply(n):
        return n * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

# Caso práctico: generador de loggers con prefijo
def make_logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log

info = make_logger("INFO")
error = make_logger("ERROR")

info("Servidor iniciado")      # [INFO] Servidor iniciado
error("Conexión fallida")      # [ERROR] Conexión fallida
