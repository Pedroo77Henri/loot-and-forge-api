from dataclasses import dataclass
from domain.entities.character import Character
from domain.entities.item import Item
from domain.exceptions import CharacterNotFound
from domain.repositories import CharacterRepository, ItemRepository


@dataclass
class CharacterDetails:
    character: Character
    items: list[Item]


class GetCharacter:
    def __init__(self, character_repository: CharacterRepository, item_repository: ItemRepository):
        self.character_repository = character_repository
        self.item_repository = item_repository

    def execute(self, character_id: int) -> CharacterDetails:
        character = self.character_repository.get_by_id(character_id)
        if character is None:
            raise CharacterNotFound(f"Personagem {character_id} não encontrado")
        items = self.item_repository.list_all(character_id=character_id)
        return CharacterDetails(character=character, items=items)
