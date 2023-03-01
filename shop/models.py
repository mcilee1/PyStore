
class Product:
    def __init__(self, name: str, brand: str, model: str, price: int = 0, category=None, color: str = None, memory: int = 0):
        self.name = name
        self.color = color
        self.memory = memory
        self.brand = brand
        self.price = price
        self.model = model
        self.categoy = category

    def __repr__(self):
        return self.name

class Category:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name