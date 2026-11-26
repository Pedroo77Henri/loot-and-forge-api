from domain.entities.character import Character
from domain.repositories import CharacterRepository


class CreateCharacter:
    def __init__(self, repository: CharacterRepository):
        self.repository = repository

    def execute(self, name: str, power: int) -> Character:
        character = Character(name=name, power=power)
        return self.repository.save(character)
