class Calculator:
    def add(self, a, b):
        """Adds two numbers and returns the result."""
        result = a + b
        return result

    def subtract(self, a, b):
        """Subtracts the second number from the first and returns the result."""
        result = a - b
        return result

    def multiply(self, a, b):
        """Multiplies two numbers and returns the result."""
        result = a * b
        return result

    def divide(self, a, b):
        """Divides the first number by the second and returns the result.
        Raises a ValueError if the second number is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        else:
            result = a / b
            return result

    def power(self, base, exponent):
        """Raises the base to the power of the exponent and returns the result."""
        result = base ** exponent
        return result

    def modulus(self, a, b):
        """Calculates the modulus of two numbers and returns the result."""
        result = a % b
        return result
