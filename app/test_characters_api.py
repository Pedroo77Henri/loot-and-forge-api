def criar_personagem(client):
    return client.post("/personagens", json={"name": "Arthas", "power": 100}).json()


def criar_item(client):
    payload = {"name": "Espada", "item_type": "Weapon", "rarity": "Epic", "power": 50}
    return client.post("/itens", json=payload).json()


def forjar_item(client):
    payload = {"name": "Machado", "item_type": "Weapon", "rarity": "Epic", "time_required": 600}
    return client.post("/itens/forjar", json=payload).json()


def test_criar_personagem(client):
    response = client.post("/personagens", json={"name": "Arthas", "power": 100})

    assert response.status_code == 200
    assert response.json()["status"] == "Active"


def test_equipar_e_buscar_personagem_com_itens(client):
    personagem = criar_personagem(client)
    item = criar_item(client)

    equipar = client.post(f"/personagens/{personagem['id']}/equipar/{item['id']}")
    response = client.get(f"/personagens/{personagem['id']}")

    assert equipar.status_code == 200
    assert response.status_code == 200
    assert [i["id"] for i in response.json()["items"]] == [item["id"]]


def test_equipar_item_em_forja_devolve_400(client):
    personagem = criar_personagem(client)
    item = forjar_item(client)

    response = client.post(f"/personagens/{personagem['id']}/equipar/{item['id']}")

    assert response.status_code == 400


def test_buscar_personagem_inexistente_devolve_404(client):
    response = client.get("/personagens/999999")

    assert response.status_code == 404
