from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Item, Status, Rarity, ItemType
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class CreateItemSchema(BaseModel):
    name: str
    item_type: ItemType
    rarity: Rarity
    power: int

@router.post("/itens")
def create_item(info: CreateItemSchema, db: Session = Depends(get_db)):
    name_info = info.name
    item_type_info = info.item_type
    rarity_info = info.rarity
    power_info = info.power

    new_item = Item(
        name=name_info,
        item_type=item_type_info,
        rarity=rarity_info,
        power=power_info,
        status=Status.READY
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return {
            "message": "Item created",
            "name": name_info,
            "item_type": item_type_info,
            "rarity": rarity_info,
            "power": power_info,
            "status": Status.READY
        }
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error saving item to database")


class ForgeItemSchema(BaseModel):
    name: str
    time_required: int
    item_type: ItemType
    rarity: Rarity

@router.post("/itens/forjar", status_code=202)
def forge_item(informacao: ForgeItemSchema, db: Session = Depends(get_db)):
    input_name = informacao.name
    input_time = informacao.time_required

    new_item = Item(
        name=input_name,
        time_required=input_time,
        status=Status.FORGING,
        item_type=ItemType,
        rarity=Rarity,
        power=None
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return {
            "message": "Item placed in forge successfully",
            "item": {
                "id": new_item.id,
                "name": new_item.name,
                "status": new_item.status.value,
                "created_at": new_item.created_at
            }
        }
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error saving item to forge")


@router.get("/itens/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/itens")
def get_itens(item_type: str = None, item_rarity: str = None, order_by: str = None, direction: str = None, db: Session = Depends(get_db)): 
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


@router.delete("/itens/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    try:
        db.delete(item)
        db.commit()
        return {"message": f"Item '{item.name}' removed successfully"}
    except Exception:
        raise HTTPException(status_code=500, detail="Error removing item")