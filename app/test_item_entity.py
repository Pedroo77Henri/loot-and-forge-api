import pytest
from datetime import datetime
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


INICIO = datetime(2026, 1, 1, 12, 0, 0)


def item_em_forja(segundos=30):
    return Item(
        name="Machado",
        item_type=ItemType.WEAPON,
        rarity=Rarity.LEGENDARY,
        status=Status.FORGING,
        time_required=segundos,
        created_at=INICIO,
    )


def test_forja_ainda_nao_terminou():
    item = item_em_forja(segundos=30)

    assert item.is_forge_complete(now=datetime(2026, 1, 1, 12, 0, 29)) is False


def test_forja_terminou_quando_o_tempo_passou():
    item = item_em_forja(segundos=30)

    assert item.is_forge_complete(now=datetime(2026, 1, 1, 12, 0, 30)) is True


def test_item_pronto_nunca_esta_com_forja_completa():
    item = item_em_forja()
    item.status = Status.READY

    assert item.is_forge_complete(now=datetime(2030, 1, 1)) is False
