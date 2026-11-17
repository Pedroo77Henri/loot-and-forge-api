from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from domain.repositories import ItemRepository
from infrastructure.repositories.item_repository import SqlAlchemyItemRepository


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_item_repository(db: Session = Depends(get_db)) -> ItemRepository:
    return SqlAlchemyItemRepository(db)
