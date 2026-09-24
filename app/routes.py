from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Item, Status, Rarity, ItemType
from pydantic import BaseModel
import services


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
    return services.create_item(db, info)


class ForgeItemSchema(BaseModel):
    name: str
    time_required: int
    item_type: ItemType
    rarity: Rarity

@router.post("/itens/forjar", status_code=202)
def forge_item(informacao: ForgeItemSchema, db: Session = Depends(get_db)):
    return services.forge_item(db, informacao)


@router.get("/itens/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    return services.get_item_by_id(db, item_id)

@router.get("/itens")
def get_itens(item_type: str = None, item_rarity: str = None, order_by: str = None, direction: str = None, db: Session = Depends(get_db)): 
    return services.get_all_items(db, item_type, item_rarity, order_by, direction)


@router.delete("/itens/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return services.delete_item(db, item_id)