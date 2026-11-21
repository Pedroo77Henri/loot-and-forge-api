from datetime import datetime
from domain.entities.item import Item
from domain.enums import ItemType, Rarity, Status
from fakes import FakeItemRepository
from use_cases.finish_forge import FinishForge, random_power

INICIO = datetime(2026, 1, 1, 12, 0, 0)


def poder_fixo():
    return 90


def relogio_fixo():
    return datetime(2026, 1, 1, 12, 1, 0)


def item_em_forja(name, segundos):
    return Item(name=name, item_type=ItemType.WEAPON, rarity=Rarity.LEGENDARY,
                status=Status.FORGING, time_required=segundos, created_at=INICIO)


def test_finish_forge_termina_so_os_itens_com_tempo_esgotado():
    repo = FakeItemRepository()
    terminou = repo.save(item_em_forja("Machado", segundos=30))
    ainda_forjando = repo.save(item_em_forja("Martelo", segundos=600))
    pronto = repo.save(Item(name="Escudo", item_type=ItemType.ARMOR,
                            rarity=Rarity.RARE, status=Status.READY, power=40))

    finalizados = FinishForge(repo, roll_power=poder_fixo, clock=relogio_fixo).execute()

    assert finalizados == [terminou]
    assert repo.get_by_id(terminou.id).status == Status.READY
    assert repo.get_by_id(terminou.id).power == 90
    assert repo.get_by_id(ainda_forjando.id).status == Status.FORGING
    assert repo.get_by_id(pronto.id).power == 40


def test_finish_forge_sem_itens_em_forja_nao_faz_nada():
    assert FinishForge(FakeItemRepository()).execute() == []


def test_random_power_fica_entre_80_e_100():
    for _ in range(100):
        assert 80 <= random_power() <= 100
