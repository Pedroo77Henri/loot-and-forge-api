import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from domain.entities.item import Item
from domain.enums import ItemType, Rarity, Status
from infrastructure.repositories.item_repository import SqlAlchemyItemRepository


@pytest.fixture
def repo():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(bind=engine)
    session = sessionmaker(bind=engine)()
    yield SqlAlchemyItemRepository(session)
    session.close()


def novo_item(**dados):
    padrao = dict(
        name="Espada",
        item_type=ItemType.WEAPON,
        rarity=Rarity.EPIC,
        status=Status.READY,
        power=50,
    )
    padrao.update(dados)
    return Item(**padrao)


def test_save_preenche_id_e_created_at(repo):
    salvo = repo.save(novo_item())

    assert salvo.id is not None
    assert salvo.created_at is not None


def test_get_by_id_inexistente_devolve_none(repo):
    assert repo.get_by_id(999) is None


def test_save_atualiza_item_existente(repo):
    item = repo.save(novo_item(status=Status.FORGING, power=None))

    item.finish_forging(power=90)
    repo.save(item)

    do_banco = repo.get_by_id(item.id)
    assert do_banco.power == 90
    assert do_banco.status == Status.READY


def test_list_all_filtra_por_tipo(repo):
    repo.save(novo_item(name="Espada", item_type=ItemType.WEAPON))
    repo.save(novo_item(name="Escudo", item_type=ItemType.ARMOR))

    resultado = repo.list_all(item_type=ItemType.ARMOR)

    assert [i.name for i in resultado] == ["Escudo"]


def test_list_all_vazio_devolve_lista_vazia(repo):
    assert repo.list_all() == []


def test_delete_remove_item(repo):
    item = repo.save(novo_item())

    repo.delete(item)

    assert repo.get_by_id(item.id) is None
