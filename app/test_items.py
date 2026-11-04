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