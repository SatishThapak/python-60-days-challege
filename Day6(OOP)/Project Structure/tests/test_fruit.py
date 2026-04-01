import unittest
from fruit import Fruit

class TestFruit(unittest.TestCase):
    def test_describe(self):
        apple = Fruit("Apple", "Red")
        self.assertEqual(apple.describe(), "This fruit is a Apple and its color is Red")

if __name__ == "__main__":
    unittest.main()
