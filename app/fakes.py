from domain.entities.character import Character
from domain.entities.item import Item
from domain.repositories import CharacterRepository, ItemRepository


class FakeItemRepository(ItemRepository):
    def __init__(self):
        self.items = {}
        self.next_id = 1

    def save(self, item: Item) -> Item:
        if item.id is None:
            item.id = self.next_id
            self.next_id += 1
        self.items[item.id] = item
        return item

    def get_by_id(self, item_id: int) -> Item | None:
        return self.items.get(item_id)

    def list_all(self, item_type=None, rarity=None, order_by=None, direction=None,
                 status=None, character_id=None) -> list[Item]:
        itens = list(self.items.values())
        if status:
            itens = [i for i in itens if i.status == status]
        if character_id is not None:
            itens = [i for i in itens if i.character_id == character_id]
        return itens

    def delete(self, item: Item) -> None:
        self.items.pop(item.id, None)


class FakeCharacterRepository(CharacterRepository):
    def __init__(self):
        self.characters = {}
        self.next_id = 1

    def save(self, character: Character) -> Character:
        if character.id is None:
            character.id = self.next_id
            self.next_id += 1
        self.characters[character.id] = character
        return character

    def get_by_id(self, character_id: int) -> Character | None:
        return self.characters.get(character_id)

    def list_all(self) -> list[Character]:
        return list(self.characters.values())
