import pytest
from domain.entities.character import Character
from domain.entities.item import Item
from domain.enums import CharacterStatus, ItemType, Rarity, Status
from domain.exceptions import CharacterNotFound, ItemNotFound, ItemNotReady
from fakes import FakeCharacterRepository, FakeItemRepository
from use_cases.create_character import CreateCharacter
from use_cases.equip_item import EquipItem
from use_cases.get_character import GetCharacter
from use_cases.list_characters import ListCharacters


def novo_item(status=Status.READY):
    return Item(name="Espada", item_type=ItemType.WEAPON,
                rarity=Rarity.EPIC, status=status, power=50)


def test_create_character_nasce_ativo_e_salvo():
    repo = FakeCharacterRepository()

    personagem = CreateCharacter(repo).execute(name="Arthas", power=100)

    assert personagem.status == CharacterStatus.ACTIVE
    assert repo.get_by_id(personagem.id) is personagem


def test_list_characters_devolve_todos():
    repo = FakeCharacterRepository()
    repo.save(Character(name="Arthas", power=100))
    repo.save(Character(name="Jaina", power=90))

    assert [c.name for c in ListCharacters(repo).execute()] == ["Arthas", "Jaina"]


def test_get_character_traz_os_itens_do_personagem():
    personagens, itens = FakeCharacterRepository(), FakeItemRepository()
    arthas = personagens.save(Character(name="Arthas", power=100))
    espada = itens.save(novo_item())
    itens.save(novo_item())
    espada.character_id = arthas.id

    detalhes = GetCharacter(personagens, itens).execute(arthas.id)

    assert detalhes.character is arthas
    assert detalhes.items == [espada]


def test_get_character_inexistente_lanca_character_not_found():
    with pytest.raises(CharacterNotFound):
        GetCharacter(FakeCharacterRepository(), FakeItemRepository()).execute(999)


def test_equip_item_salva_o_dono():
    personagens, itens = FakeCharacterRepository(), FakeItemRepository()
    arthas = personagens.save(Character(name="Arthas", power=100))
    espada = itens.save(novo_item())

    EquipItem(personagens, itens).execute(arthas.id, espada.id)

    assert itens.get_by_id(espada.id).character_id == arthas.id


def test_equip_item_inexistente_lanca_item_not_found():
    personagens = FakeCharacterRepository()
    arthas = personagens.save(Character(name="Arthas", power=100))

    with pytest.raises(ItemNotFound):
        EquipItem(personagens, FakeItemRepository()).execute(arthas.id, 999)


def test_equip_item_em_forja_lanca_item_not_ready():
    personagens, itens = FakeCharacterRepository(), FakeItemRepository()
    arthas = personagens.save(Character(name="Arthas", power=100))
    machado = itens.save(novo_item(status=Status.FORGING))

    with pytest.raises(ItemNotReady):
        EquipItem(personagens, itens).execute(arthas.id, machado.id)
