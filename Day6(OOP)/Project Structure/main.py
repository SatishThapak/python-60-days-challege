from fruit import Fruit

def run():
    banana = Fruit("Banana", "Yellow")
    print(banana.describe())

# Note: if __name__ == "__main__": is the gatekeeper that makes your files flexible — usable as both modules and standalone scripts

if __name__ == "__main__":
    run()
