class SimpleNumber:

    def __init__(self, num):
        val = self.is_number(num)
        
        self.x = val
        
    def is_number(self, x):
        try:
            val = float(x)
        except ValueError:
            print("That's not a float number!")

        return val
        
    def add(self, y):
        result = self.x + y

        return result

    def multiply(self, y):
        result = self.x * self.is_number(y)

        return result
