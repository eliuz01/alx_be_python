class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        It prints the class attribute calculation_type before multiplying.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
