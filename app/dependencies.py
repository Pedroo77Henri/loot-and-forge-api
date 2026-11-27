from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from domain.repositories import CharacterRepository, ItemRepository
from infrastructure.repositories.character_repository import SqlAlchemyCharacterRepository
from infrastructure.repositories.item_repository import SqlAlchemyItemRepository


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_item_repository(db: Session = Depends(get_db)) -> ItemRepository:
    return SqlAlchemyItemRepository(db)


def get_character_repository(db: Session = Depends(get_db)) -> CharacterRepository:
    return SqlAlchemyCharacterRepository(db)
