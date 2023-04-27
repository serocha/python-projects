# a simple command line calculator
# displays an ASCII art 'calculator' to show result, max 25 characters
# may be worth revisiting to make a simple GUI
#
# playing around with docstring hints
from art import logo, display1, display2


class Calculator:
    def __init__(self):
        self._a: float = 0
        self._b: float = 0
        self._result: float = 0
        self._operator: str = ""
        self._operations: dict = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
        }

    def get_a(self) -> float:
        return self._a

    def get_b(self) -> float:
        return self._b

    def get_result(self) -> float:
        return self._result

    def get_operator(self) -> str:
        return self._operator

    def get_operations(self) -> dict:
        return self._operations

    def set_a(self, a: float) -> None:
        self._a = a

    def set_b(self, b: float) -> None:
        self._b = b

    def set_result(self, result: float) -> None:
        self._result = result

    def set_operator(self, operator: str) -> None:
        self._operator = operator

    # def set_operations(self, operations: dict) -> None:
    #     self._operations = operations

    # basic calc methods
    def add(self, a: float, b: float) -> float:
        """Adds two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subracts two numbers."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplies two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divides two numbers."""
        return a / b

    # app methods
    def get_input(self) -> None:
        """Prepares user input for calculation."""
        if self.get_result() == 0:
            self.set_a(float(input("Enter the first number: ")))
        else:
            self.set_a(self.get_result())  # assign old result to a for continued operations
            print(self.get_a())
        print("\nOperations:")
        for key in self.get_operations().keys():
            print(key)
        print()
        self.set_operator(input("Pick an operation: "))
        self.set_b(float(input("\nEnter the second number: ")))

    def calc(self) -> None:
        """Performs calculation based on internal state."""
        operator = self.get_operator()
        operations = self.get_operations()
        a = self.get_a()
        b = self.get_b()
            
        self.set_result(operations[operator](a, b))

    def should_continue(self) -> bool:
        usr_input = input("Perform a new operation? [y/n] ").lower()
        if usr_input.startswith('n'):
            return False
        else:
            return True

    def print_result(self) -> None:
        result_str = f"{self.get_a()} {self.get_operator()} {self.get_b()} = {self.get_result()}"
        result_spacing = 25 - len(result_str)  # must be a more straightforward method
        final_str = "| | " + result_str.ljust(len(result_str) + result_spacing) + "| |"
        print(display1 + final_str + display2)

    def run(self) -> None:
        flag = True
        print(logo)

        while flag:
            print()
            self.get_input()
            self.calc()
            self.print_result()
            flag = self.should_continue()
            if flag:
                usr_input = input("Continue with previous result? [y/n] ").lower()
                if usr_input.startswith('n'):
                    self.set_result(0)
        print("\nExiting...")

calculator = Calculator()
calculator.run()