from enum import Enum, auto
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum as SAEnum
from sqlalchemy.sql import func


class ItemType(Enum):
    WEAPON = "Weapon"
    ARMOR = "Armor"
    POTION = "Potion"
    SCROLL = "Scroll"

class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

class Status(Enum):
    READY = "Ready"
    FORGING = "Forging"

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