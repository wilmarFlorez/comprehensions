# ============================================================
#  FACTORY & REGISTRY — crear objetos sin if/elif chains
# ============================================================
from dataclasses import dataclass


# Registry pattern — registrar clases por nombre
_parsers: dict[str, type] = {}

def register(ext: str):
    """Decorator que registra un parser para una extensión."""
    def decorator(cls):
        _parsers[ext] = cls
        return cls
    return decorator


def get_parser(filename: str):
    ext = "." + filename.rsplit(".", 1)[-1]
    parser_cls = _parsers.get(ext)
    if parser_cls is None:
        raise ValueError(f"No hay parser para {ext}")
    return parser_cls()


# Parsers registrados con el decorator
@register(".json")
class JsonParser:
    def parse(self, content: str) -> dict:
        import json
        return json.loads(content)

    def __repr__(self):
        return "JsonParser()"


@register(".csv")
class CsvParser:
    def parse(self, content: str) -> list[list[str]]:
        return [line.split(",") for line in content.strip().split("\n")]

    def __repr__(self):
        return "CsvParser()"


@register(".txt")
class TextParser:
    def parse(self, content: str) -> list[str]:
        return content.strip().split("\n")

    def __repr__(self):
        return "TextParser()"


# Uso
for filename in ["data.json", "users.csv", "notes.txt"]:
    parser = get_parser(filename)
    print(f"{filename:12} -> {parser}")

print(f"\nRegistrados: {list(_parsers.keys())}")

# Parsear algo real
json_parser = get_parser("config.json")
data = json_parser.parse('{"host": "localhost", "port": 8080}')
print(f"Parseado: {data}")
