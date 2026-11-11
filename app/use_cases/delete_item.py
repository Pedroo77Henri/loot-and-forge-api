from domain.exceptions import ItemNotFound
from domain.repositories import ItemRepository


class DeleteItem:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def execute(self, item_id: int):
        item = self.repository.get_by_id(item_id)
        if item is None:
            raise ItemNotFound(f"Item {item_id} não encontrado")
        self.repository.delete(item)
        return item
