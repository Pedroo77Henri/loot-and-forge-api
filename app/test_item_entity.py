import pytest
from domain.entities.item import Item
from domain.enums import ItemType, Rarity, Status
from domain.exceptions import ItemNotForging


def test_finalizar_forja():
    item = Item(
        name="Espada",
        item_type=ItemType.WEAPON,
        rarity=Rarity.EPIC,
        status=Status.FORGING,
    )

    item.finish_forging(power=90)

    assert item.power == 90
    assert item.status == Status.READY


def test_finalizar_forja_de_item_pronto_da_erro():
    item = Item(
        name="Escudo",
        item_type=ItemType.ARMOR,
        rarity=Rarity.RARE,
        status=Status.READY,
        power=95,
    )

    with pytest.raises(ItemNotForging):
        item.finish_forging(power=80)

    assert item.power == 95
