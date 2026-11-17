from domain.entities.item import Item
from domain.exceptions import ItemNotFound
from domain.repositories import ItemRepository


class GetItem:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def execute(self, item_id: int) -> Item:
        item = self.repository.get_by_id(item_id)
        if item is None:
            raise ItemNotFound(f"Item {item_id} não encontrado")
        return item
