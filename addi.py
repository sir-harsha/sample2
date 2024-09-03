class SimpleCalculator:
    def __init__(self):
        pass
    
    def add(self, a, b):
        return a + b
    
    def get_number(self, prompt):
        try:
            return int(input(prompt))
        except ValueError:
            print('Invalid input. Please enter an integer.')
            return None
        
    def execute(self):
        num1 = self.get_number("Enter the first number: ")
        num2 = self.get_number("Enter the second number: ")
        if num1 is None or num2 is None:
            return
        result =self.add(num1, num2)
        print(f"Result: {result}")
        
if __name__ == '__main__':
    calc = SimpleCalculator()
    calc.execute()
