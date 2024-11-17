class FindOneProductResponse:
    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price