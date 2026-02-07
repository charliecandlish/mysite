import math

class ScientificCalculator:
    """A simple scientific calculator supporting basic and trigonometric operations."""

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def power(self, a: float, b: float) -> float:
        return a ** b

    def sqrt(self, x: float) -> float:
        if x < 0:
            raise ValueError("Cannot take square root of negative number.")
        return math.sqrt(x)

    def sin(self, x: float) -> float:
        return math.sin(x)

    def cos(self, x: float) -> float:
        return math.cos(x)

    def tan(self, x: float) -> float:
        return math.tan(x)

    def log(self, x: float, base: float = math.e) -> float:
        return math.log(x, base)
