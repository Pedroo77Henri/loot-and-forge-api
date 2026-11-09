from dataclasses import dataclass
from datetime import datetime
from domain.enums import ItemType, Rarity, Status
from domain.exceptions import ItemNotForging


@dataclass
class Item:
    name: str
    item_type: ItemType
    rarity: Rarity
    status: Status
    power: int | None = None
    time_required: int | None = None
    id: int | None = None
    created_at: datetime | None = None

    def finish_forging(self, power: int):
        if self.status != Status.FORGING:
            raise ItemNotForging(f"O item {self.name} não está em forja")
        self.power = power
        self.status = Status.READY
