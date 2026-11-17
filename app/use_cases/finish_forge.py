from random import randint
from domain.entities.item import Item
from domain.enums import Status
from domain.repositories import ItemRepository


def random_power() -> int:
    return randint(80, 100)


class FinishForge:
    def __init__(self, repository: ItemRepository, roll_power=random_power):
        self.repository = repository
        self.roll_power = roll_power

    def execute(self) -> list[Item]:
        forging = self.repository.list_all(status=Status.FORGING)
        for item in forging:
            item.finish_forging(power=self.roll_power())
            self.repository.save(item)
        return forging
