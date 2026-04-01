class Fruit:
    def __init__(self, name: str, color: str):
        """
        Initialize a Fruit object with a name and color.
        
        Parameters:
        name (str): The name of the fruit
        color (str): The color of the fruit
        """
        self.name = name
        self.color = color
    
    def describe(self):
        """
        Print a description of the fruit.
        """
        print(f"This fruit is a {self.name} and its color is {self.color}.")

# Example usage
if __name__ == "__main__":
    # Create an object of Fruit
    apple = Fruit("Apple", "Red")
    
    # Call the describe method
    apple.describe()
