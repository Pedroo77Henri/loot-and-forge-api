from abc import ABC, abstractmethod
from domain.entities.item import Item
from domain.enums import ItemType, Rarity


class ItemRepository(ABC):

    @abstractmethod
    def save(self, item: Item) -> Item:
        pass

    @abstractmethod
    def get_by_id(self, item_id: int) -> Item | None:
        pass

    @abstractmethod
    def list_all(
        self,
        item_type: ItemType | None = None,
        rarity: Rarity | None = None,
        order_by: str | None = None,
        direction: str | None = None,
    ) -> list[Item]:
        pass

    @abstractmethod
    def delete(self, item: Item) -> None:
        pass
