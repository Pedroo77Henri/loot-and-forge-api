import pytest
from domain.entities.item import Item
from domain.enums import ItemType, Rarity, Status
from domain.exceptions import ItemNotFound
from fakes import FakeItemRepository
from use_cases.delete_item import DeleteItem


def test_delete_item_remove_item_existente():
    repo = FakeItemRepository()
    item = repo.save(Item(name="Espada", item_type=ItemType.WEAPON,
                          rarity=Rarity.EPIC, status=Status.READY, power=50))
    use_case = DeleteItem(repo)

    apagado = use_case.execute(item.id)

    assert apagado.id == item.id
    assert repo.get_by_id(item.id) is None


def test_delete_item_inexistente_lanca_item_not_found():
    repo = FakeItemRepository()
    use_case = DeleteItem(repo)

    with pytest.raises(ItemNotFound):
        use_case.execute(999)
