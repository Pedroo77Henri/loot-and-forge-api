def test_criar_item(client):
    payload = {
        "name": "Espada Longa",
        "item_type": "Weapon",
        "rarity": "Common",
        "power": 50
    }

    response = client.post("/itens", json=payload)

    assert response.status_code == 200
    assert response.json()["name"] == "Espada Longa"

def test_forjar_item(client):
    payload = {
        "name": "Espada Longa",
        "time_required": 10,
        "item_type": "Weapon",
        "rarity": "Common"
    }
    response = client.post("/itens/forjar", json=payload)

    assert response.status_code == 202
    assert response.json()["status"] == "Forging"

def test_buscar_item_por_id(client):
    payload = {
        "name": "Espada Longa",
        "item_type": "Weapon",
        "rarity": "Common",
        "power": 50
    }
    item_criado = client.post("/itens", json=payload).json()

    response = client.get(f"/itens/{item_criado['id']}")

    assert response.status_code == 200
    assert response.json()["id"] == item_criado["id"]

def test_deleate_item(client):
    payload = {
        "name": "Espada Longa",
        "item_type": "Weapon",
        "rarity": "Common",
        "power": 50
    }
    item_criado = client.post("/itens", json=payload).json()

    response = client.delete(f"/itens/{item_criado['id']}")

    assert response.status_code == 200

def test_listar_itens(client):
    payload = {
        "name": "Espada Longa",
        "item_type": "Weapon",
        "rarity": "Common",
        "power": 50
    }
    item_criado = client.post("/itens", json=payload).json()

    response = client.get("/itens")

    assert response.status_code == 200
    ids_retornados = [item["id"] for item in response.json()]
    assert item_criado["id"] in ids_retornados

def test_filtrar_por_tipo(client):
    payload = {
        "name": "Escudo de Ferro",
        "item_type": "Armor",
        "rarity": "Common",
        "power": 30
    }
    client.post("/itens", json=payload)

    response = client.get("/itens", params={"item_type": "ARMOR"})

    assert response.status_code == 200
    for item in response.json():
        assert item["item_type"] == "Armor"