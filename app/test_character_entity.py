import pytest
from domain.entities.character import Character
from domain.entities.item import Item
from domain.enums import CharacterStatus, ItemType, Rarity, Status
from domain.exceptions import CharacterInactive, ItemNotReady


def novo_item(status=Status.READY):
    return Item(name="Espada", item_type=ItemType.WEAPON,
                rarity=Rarity.EPIC, status=status, power=50)


def test_personagem_nasce_ativo():
    personagem = Character(name="Arthas", power=100)

    assert personagem.status == CharacterStatus.ACTIVE


def test_equipar_item_pronto():
    personagem = Character(name="Arthas", power=100, id=1)
    item = novo_item()

    personagem.equip(item)

    assert item.character_id == 1


def test_equipar_item_em_forja_da_erro():
    personagem = Character(name="Arthas", power=100, id=1)
    item = novo_item(status=Status.FORGING)

    with pytest.raises(ItemNotReady):
        personagem.equip(item)

    assert item.character_id is None


def test_personagem_inativo_nao_equipa():
    personagem = Character(name="Arthas", power=100, id=1,
                           status=CharacterStatus.INACTIVE)
    item = novo_item()

    with pytest.raises(CharacterInactive):
        personagem.equip(item)

    assert item.character_id is None


def test_equipar_item_de_outro_personagem_transfere_o_dono():
    item = novo_item()
    Character(name="Arthas", power=100, id=1).equip(item)

    Character(name="Jaina", power=90, id=2).equip(item)

    assert item.character_id == 2
