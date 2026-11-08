from dataclasses import dataclass
from datetime import datetime
from domain.enums import ItemType, Rarity, Status


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
