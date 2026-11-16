from domain.entities.item import Item
from domain.enums import ItemType, Rarity, Status
from domain.repositories import ItemRepository


class CreateItem:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def execute(self, name: str, item_type: ItemType, rarity: Rarity, power: int) -> Item:
        item = Item(
            name=name,
            item_type=item_type,
            rarity=rarity,
            power=power,
            status=Status.READY,
        )
        return self.repository.save(item)
