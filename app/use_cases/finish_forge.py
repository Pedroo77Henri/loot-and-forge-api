from datetime import datetime, timezone
from random import randint
from domain.entities.item import Item
from domain.enums import Status
from domain.repositories import ItemRepository


def random_power() -> int:
    return randint(80, 100)


def utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)


class FinishForge:
    def __init__(self, repository: ItemRepository, roll_power=random_power, clock=utc_now):
        self.repository = repository
        self.roll_power = roll_power
        self.clock = clock

    def execute(self) -> list[Item]:
        now = self.clock()
        forging = self.repository.list_all(status=Status.FORGING)
        finished = []
        for item in forging:
            if item.is_forge_complete(now):
                item.finish_forging(power=self.roll_power())
                self.repository.save(item)
                finished.append(item)
        return finished
