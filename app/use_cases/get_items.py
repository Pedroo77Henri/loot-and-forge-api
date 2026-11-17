from domain.entities.item import Item
from domain.enums import ItemType, Rarity
from domain.repositories import ItemRepository


class GetItems:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def execute(
        self,
        item_type: ItemType | None = None,
        rarity: Rarity | None = None,
        order_by: str | None = None,
        direction: str | None = None,
    ) -> list[Item]:
        return self.repository.list_all(item_type, rarity, order_by, direction)
