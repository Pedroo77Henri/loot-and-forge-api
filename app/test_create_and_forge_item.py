from domain.enums import ItemType, Rarity, Status
from fakes import FakeItemRepository
from use_cases.create_item import CreateItem
from use_cases.forge_item import ForgeItem


def test_create_item_nasce_pronto():
    repo = FakeItemRepository()
    use_case = CreateItem(repo)

    item = use_case.execute(name="Espada", item_type=ItemType.WEAPON,
                            rarity=Rarity.EPIC, power=70)

    assert item.status == Status.READY
    assert item.power == 70
    assert repo.get_by_id(item.id) is item


def test_forge_item_nasce_em_forja_sem_poder():
    repo = FakeItemRepository()
    use_case = ForgeItem(repo)

    item = use_case.execute(name="Machado", item_type=ItemType.WEAPON,
                            rarity=Rarity.LEGENDARY, time_required=30)

    assert item.status == Status.FORGING
    assert item.power is None
    assert item.time_required == 30
    assert repo.get_by_id(item.id) is item
