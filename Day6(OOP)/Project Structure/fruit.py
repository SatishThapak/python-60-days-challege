class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def describe(self):
        return f"This fruit is a {self.name} and its color is {self.color}."

if __name__ == "__main__":
    # Demo code (only runs if fruit.py is executed directly)
    apple = Fruit("Apple", "Red")
    print(apple.describe())
