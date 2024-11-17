from uuid import UUID
from common.domain.value_object.value_object import ValueObject
from ..errors.invalid_product_id import invalid_product_id_error


class ProductId(ValueObject):
    def __init__(self, id: UUID) -> None:
        super().__init__(id)
        self.validate()

    @property
    def id(self) -> UUID:
        return self.value

    def validate(self) -> None:
        if not isinstance(self.id, UUID):
            raise invalid_product_id_error()

    def __eq__(self, other: "ProductId") -> bool:
        return self.value == other.id
