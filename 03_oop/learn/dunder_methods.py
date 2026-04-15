# ============================================================
#  DUNDER METHODS (métodos mágicos)
#  Permiten que tus clases se comporten como tipos nativos.
# ============================================================


class Money:
    def __init__(self, amount: float, currency: str = "USD"):
        self.amount = amount
        self.currency = currency

    # Representación para debug
    def __repr__(self):
        return f"Money({self.amount}, {self.currency!r})"

    # Representación para usuario
    def __str__(self):
        return f"${self.amount:,.2f} {self.currency}"

    # Operadores aritméticos
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError(f"No se puede sumar {self.currency} + {other.currency}")
        return Money(self.amount + other.amount, self.currency)

    def __mul__(self, factor):
        return Money(self.amount * factor, self.currency)

    # Comparación
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        return self.amount < other.amount

    # Para usar como clave de dict o en sets
    def __hash__(self):
        return hash((self.amount, self.currency))

    # Hacer la clase "contenedor"
    def __bool__(self):
        return self.amount > 0

    # len() — ejemplo: cantidad de dígitos
    def __len__(self):
        return len(str(int(abs(self.amount))))


a = Money(100, "USD")
b = Money(50, "USD")

print(a + b)       # $150.00 USD
print(a * 3)       # $300.00 USD
print(a > b)       # True
print(bool(Money(0)))  # False
print(sorted([b, a]))  # [Money(50, 'USD'), Money(100, 'USD')]
