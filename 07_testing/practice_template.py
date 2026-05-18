# ============================================================
#  PRÁCTICA — TESTING
#  Ejecuta: python -m pytest 07_testing/practice.py -v
#  Implementa las funciones para que los tests pasen.
# ============================================================
import pytest

# --- FUNCIONES A IMPLEMENTAR ---

# 1. Crea fizzbuzz(n): retorna "Fizz" si divisible por 3,
# "Buzz" si por 5, "FizzBuzz" si por ambos, str(n) sino.
def fizzbuzz(n):
    ...


# 2. Crea flatten(lst): aplana un nivel de listas anidadas.
# flatten([1, [2, 3], [4]]) -> [1, 2, 3, 4]
def flatten(lst):
    ...


# 3. Crea count_words(text): retorna dict con conteo de palabras (lowercase).
# count_words("Hola hola MUNDO") -> {"hola": 2, "mundo": 1}
def count_words(text):
    ...


# 4. Crea chunk(lst, size): divide lista en sublistas de tamaño size.
# chunk([1,2,3,4,5], 2) -> [[1,2], [3,4], [5]]
def chunk(lst, size):
    ...


# 5. Crea RingBuffer(capacity) con append() y to_list().
# Al llenarse, sobrescribe los más antiguos.
class RingBuffer:
    ...


# --- TESTS (NO MODIFICAR) ---

class TestFizzBuzz:
    def test_number(self):
        assert fizzbuzz(1) == "1"
        assert fizzbuzz(7) == "7"

    def test_fizz(self):
        assert fizzbuzz(3) == "Fizz"
        assert fizzbuzz(9) == "Fizz"

    def test_buzz(self):
        assert fizzbuzz(5) == "Buzz"
        assert fizzbuzz(10) == "Buzz"

    def test_fizzbuzz(self):
        assert fizzbuzz(15) == "FizzBuzz"
        assert fizzbuzz(30) == "FizzBuzz"

    @pytest.mark.parametrize("n,expected", [
        (1, "1"), (3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz"), (45, "FizzBuzz"),
    ])
    def test_parametrized(self, n, expected):
        assert fizzbuzz(n) == expected


class TestFlatten:
    def test_empty(self):
        assert flatten([]) == []

    def test_flat(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_nested(self):
        assert flatten([1, [2, 3], [4, 5]]) == [1, 2, 3, 4, 5]

    def test_mixed(self):
        assert flatten([[1], 2, [3, 4]]) == [1, 2, 3, 4]


class TestCountWords:
    def test_simple(self):
        assert count_words("hola mundo") == {"hola": 1, "mundo": 1}

    def test_repeated(self):
        assert count_words("Hola hola HOLA") == {"hola": 3}

    def test_empty(self):
        assert count_words("") == {}


class TestChunk:
    def test_even(self):
        assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_remainder(self):
        assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_single(self):
        assert chunk([1, 2, 3], 1) == [[1], [2], [3]]

    def test_larger_than_list(self):
        assert chunk([1, 2], 5) == [[1, 2]]


class TestRingBuffer:
    def test_basic(self):
        rb = RingBuffer(3)
        rb.append(1)
        rb.append(2)
        assert rb.to_list() == [1, 2]

    def test_overflow(self):
        rb = RingBuffer(3)
        for i in range(5):
            rb.append(i)
        assert rb.to_list() == [2, 3, 4]

    def test_single_capacity(self):
        rb = RingBuffer(1)
        rb.append("a")
        rb.append("b")
        assert rb.to_list() == ["b"]
