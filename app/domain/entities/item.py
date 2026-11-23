from dataclasses import dataclass
from datetime import datetime, timedelta
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
    character_id: int | None = None

    def is_forge_complete(self, now: datetime) -> bool:
        if self.status != Status.FORGING:
            return False
        if self.created_at is None or self.time_required is None:
            return False
        return now >= self.created_at + timedelta(seconds=self.time_required)

    def finish_forging(self, power: int):
        if self.status != Status.FORGING:
            raise ItemNotForging(f"O item {self.name} não está em forja")
        self.power = power
        self.status = Status.READY
