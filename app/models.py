from database import Base
from domain.enums import CharacterStatus, ItemType, Rarity, Status
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SAEnum
from sqlalchemy.sql import func


class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    power = Column(Integer, nullable=False)
    status = Column(SAEnum(CharacterStatus), nullable=False)


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    item_type = Column(SAEnum(ItemType), nullable=False)
    rarity = Column(SAEnum(Rarity), nullable=False)
    power = Column(Integer)
    status = Column(SAEnum(Status), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    time_required = Column(Integer)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=True)
