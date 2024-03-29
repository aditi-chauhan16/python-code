class Factorial:
    def __init__(self, n):
        self.n = n

    def calculate(self):
        result = 1
        for i in range(1, self.n + 1):
            result *= i
        return result

# Example usage:
factorial_instance = Factorial(5)
result = factorial_instance.calculate()
print(result)  # Output will be 120 (5!)
