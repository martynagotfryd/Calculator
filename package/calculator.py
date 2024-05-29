class Calculator:
    def __init__(self):
        self.number1 = None
        self.number2 = None
        self.operation = None
        self.result = None

    def set_values(self, number1, number2, operation):
        self.number1 = number1
        self.number2 = number2
        self.operation = operation

    def calculate(self):
        if self.operation == 'add':
            self.result = self.number1 + self.number2
        elif self.operation == 'subtract':
            self.result = self.number1 - self.number2
        elif self.operation == 'multiply':
            self.result = self.number1 * self.number2
        elif self.operation == 'divide':
            if self.number2 != 0:
                self.result = self.number1 / self.number2
            else:
                self.result = 'Error! Division by zero.'

        return self.result