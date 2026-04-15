# ============================================================
#  STRATEGY PATTERN — cambiar comportamiento en runtime
#  En Python no necesitas clases: una función es suficiente.
# ============================================================


# Con funciones (forma pytónica)
def price_regular(amount: float) -> float:
    return amount

def price_member(amount: float) -> float:
    return amount * 0.9  # 10% descuento

def price_vip(amount: float) -> float:
    return amount * 0.8  # 20% descuento


type PriceStrategy = type[price_regular]  # Callable[[float], float]

strategies: dict[str, PriceStrategy] = {
    "regular": price_regular,
    "member": price_member,
    "vip": price_vip,
}


def checkout(amount: float, customer_type: str) -> float:
    strategy = strategies.get(customer_type, price_regular)
    return strategy(amount)


print("Regular:", checkout(100, "regular"))  # 100.0
print("Member:", checkout(100, "member"))    # 90.0
print("VIP:", checkout(100, "vip"))          # 80.0


# ============================================================
#  OBSERVER PATTERN — notificar cambios
# ============================================================

class EventEmitter:
    def __init__(self):
        self._listeners: dict[str, list] = {}

    def on(self, event: str, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event: str, *args, **kwargs):
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)


# Uso
store = EventEmitter()

store.on("sale", lambda item, price: print(f"  📧 Email: {item} vendido por ${price}"))
store.on("sale", lambda item, price: print("  📊 Analytics: venta registrada"))
store.on("sale", lambda item, price: print(f"  📦 Inventario: {item} -1"))

print("\nVenta registrada:")
store.emit("sale", "Laptop", 999)
