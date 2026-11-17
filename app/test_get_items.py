import pytest
from domain.entities.item import Item
from domain.enums import ItemType, Rarity, Status
from domain.exceptions import ItemNotFound
from fakes import FakeItemRepository
from use_cases.get_item import GetItem
from use_cases.get_items import GetItems


def novo_item(name="Espada"):
    return Item(name=name, item_type=ItemType.WEAPON,
                rarity=Rarity.EPIC, status=Status.READY, power=50)


def test_get_item_devolve_item_existente():
    repo = FakeItemRepository()
    item = repo.save(novo_item())

    encontrado = GetItem(repo).execute(item.id)

    assert encontrado is item


def test_get_item_inexistente_lanca_item_not_found():
    with pytest.raises(ItemNotFound):
        GetItem(FakeItemRepository()).execute(999)


def test_get_items_devolve_todos():
    repo = FakeItemRepository()
    repo.save(novo_item("Espada"))
    repo.save(novo_item("Escudo"))

    itens = GetItems(repo).execute()

    assert [i.name for i in itens] == ["Espada", "Escudo"]


def test_get_items_vazio_devolve_lista_vazia():
    assert GetItems(FakeItemRepository()).execute() == []
