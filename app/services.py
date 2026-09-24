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

def forge_item(db, payload):
    forge_item = Item(
        name=payload.name,
        time_required=payload.time_required,
        status=Status.FORGING,
        item_type=payload.item_type,
        rarity=payload.rarity,
        power=None
    )
    return repository.forge_item(db, forge_item)

def get_all_items(db, item_type=None, item_rarity=None, order_by=None, direction=None):
    return repository.get_all_items(db, item_type, item_rarity, order_by, direction)

def get_item_by_id(db, item_id: int):
    return repository.get_item_by_id(db, item_id)

def delete_item(db, payload):
    return repository.delete_item(db, payload)
