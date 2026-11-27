from domain.entities.character import Character
from domain.repositories import CharacterRepository


class ListCharacters:
    def __init__(self, repository: CharacterRepository):
        self.repository = repository

    def execute(self) -> list[Character]:
        return self.repository.list_all()
