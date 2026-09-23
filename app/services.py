from models import Item, Status
import repository

def create_item(db, payload):
    new_item = Item(
        name=payload.name,
        item_type=payload.item_type,
        rarity=payload.rarity,
        power=payload.power,
        status=Status.READY
    )
    return repository.create_item(db, new_item)