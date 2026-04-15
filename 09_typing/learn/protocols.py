# ============================================================
#  PROTOCOL — duck typing con type checking
#  "Si camina como pato y suena como pato, es un Pato"
# ============================================================
from typing import Protocol, runtime_checkable


@runtime_checkable
class Drawable(Protocol):
    """Cualquier objeto que tenga un método draw()."""
    def draw(self) -> str: ...


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self) -> str:
        return f"○ (r={self.radius})"


class Square:
    def __init__(self, side: float):
        self.side = side

    def draw(self) -> str:
        return f"□ (s={self.side})"


class Text:
    def __init__(self, content: str):
        self.content = content

    def draw(self) -> str:
        return f'"{self.content}"'


# No necesitamos herencia — solo tener draw()
def render(shapes: list[Drawable]) -> str:
    return " | ".join(s.draw() for s in shapes)


canvas: list[Drawable] = [Circle(5), Square(3), Text("hola")]
print(render(canvas))
# ○ (r=5) | □ (s=3) | "hola"

# runtime_checkable permite isinstance()
print(f"\n¿Circle es Drawable? {isinstance(Circle(1), Drawable)}")
print(f"¿str es Drawable? {isinstance('hello', Drawable)}")
