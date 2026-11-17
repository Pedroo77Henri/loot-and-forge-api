from domain.entities.item import Item
from domain.enums import ItemType, Rarity, Status
from fakes import FakeItemRepository
from use_cases.finish_forge import FinishForge, random_power


def poder_fixo():
    return 90


def test_finish_forge_termina_so_os_itens_em_forja():
    repo = FakeItemRepository()
    em_forja = repo.save(Item(name="Machado", item_type=ItemType.WEAPON,
                              rarity=Rarity.LEGENDARY, status=Status.FORGING))
    pronto = repo.save(Item(name="Escudo", item_type=ItemType.ARMOR,
                            rarity=Rarity.RARE, status=Status.READY, power=40))

    finalizados = FinishForge(repo, roll_power=poder_fixo).execute()

    assert finalizados == [em_forja]
    assert repo.get_by_id(em_forja.id).status == Status.READY
    assert repo.get_by_id(em_forja.id).power == 90
    assert repo.get_by_id(pronto.id).power == 40


def test_finish_forge_sem_itens_em_forja_nao_faz_nada():
    assert FinishForge(FakeItemRepository()).execute() == []


def test_random_power_fica_entre_80_e_100():
    for _ in range(100):
        assert 80 <= random_power() <= 100
