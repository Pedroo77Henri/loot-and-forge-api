from abc import ABC, abstractmethod
from domain.entities.character import Character
from domain.entities.item import Item
from domain.enums import ItemType, Rarity, Status


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
        status: Status | None = None,
        character_id: int | None = None,
    ) -> list[Item]:
        pass

    @abstractmethod
    def delete(self, item: Item) -> None:
        pass


class CharacterRepository(ABC):

    @abstractmethod
    def save(self, character: Character) -> Character:
        pass

    @abstractmethod
    def get_by_id(self, character_id: int) -> Character | None:
        pass

    @abstractmethod
    def list_all(self) -> list[Character]:
        pass
