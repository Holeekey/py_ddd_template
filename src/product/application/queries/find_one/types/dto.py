from uuid import UUID


class FindOneProductDto:
    def __init__(self, id: UUID):
        self.id = id
