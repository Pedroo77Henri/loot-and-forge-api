from dataclasses import dataclass
from domain.entities.item import Item
from domain.enums import CharacterStatus, Status
from domain.exceptions import CharacterInactive, ItemNotReady


@dataclass
class Character:
    name: str
    power: int
    status: CharacterStatus = CharacterStatus.ACTIVE
    id: int | None = None

    def equip(self, item: Item):
        if self.status != CharacterStatus.ACTIVE:
            raise CharacterInactive(f"O personagem {self.name} está inativo")
        if item.status != Status.READY:
            raise ItemNotReady(f"O item {item.name} ainda não está pronto")
        item.character_id = self.id
