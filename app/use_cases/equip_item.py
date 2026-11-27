from domain.entities.item import Item
from domain.exceptions import CharacterNotFound, ItemNotFound
from domain.repositories import CharacterRepository, ItemRepository


class EquipItem:
    def __init__(self, character_repository: CharacterRepository, item_repository: ItemRepository):
        self.character_repository = character_repository
        self.item_repository = item_repository

    def execute(self, character_id: int, item_id: int) -> Item:
        character = self.character_repository.get_by_id(character_id)
        if character is None:
            raise CharacterNotFound(f"Personagem {character_id} não encontrado")
        item = self.item_repository.get_by_id(item_id)
        if item is None:
            raise ItemNotFound(f"Item {item_id} não encontrado")
        character.equip(item)
        return self.item_repository.save(item)
