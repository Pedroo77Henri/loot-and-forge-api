from models import Item
from sqlalchemy.orm import Session
from fastapi import HTTPException

def forge_item(db: Session, item: Item):
    try:
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error forging item")
    
def create_item(db: Session, item: Item):
    try:
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error saving item to database")

def delete_item(db: Session, item: Item):
    try:
        db.delete(item)
        db.commit()
        return item
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error removing item")

def get_all_items(db: Session, item_type: str = None, item_rarity: str = None, order_by: str = None, direction: str = None):
    query = db.query(Item)
    if item_type:
        query = query.filter(Item.item_type == item_type)
    if item_rarity:
        query = query.filter(Item.rarity == item_rarity)
    if order_by:
        if order_by == "power":
            column = Item.power
        elif order_by == "created_at":
            column = Item.created_at                
        if direction == "desc":
                query = query.order_by(column.desc())
        else:
            query = query.order_by(column.asc())
    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="No items found")    
    return results

def get_item_by_id(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    return item