class SimpleNumber:

    def __init__(self, num):
        try:
            val = float(num)
        except ValueError:
            print("That's not a float number!")
        
        self.x = num
  
    def add(self, y):
        result = self.x * y

        return result

    def multiply(self, y):
        result = self.x * y

        return result
