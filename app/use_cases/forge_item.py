from domain.entities.item import Item
from domain.enums import ItemType, Rarity, Status
from domain.repositories import ItemRepository


class ForgeItem:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def execute(self, name: str, item_type: ItemType, rarity: Rarity, time_required: int) -> Item:
        item = Item(
            name=name,
            item_type=item_type,
            rarity=rarity,
            time_required=time_required,
            status=Status.FORGING,
        )
        return self.repository.save(item)
